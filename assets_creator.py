from PIL import Image, ImageDraw, ImageFont
import os, copy

def round_corners(im,radius): #One of the 3 things taken from Chatgpt - Rest code self written
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new('L', im.size, 255)
    w, h = im.size

    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))

    im.putalpha(alpha)
    return im

def reduce_opacity(img, opacity): #One of the 3 things taken from Chatgpt - Rest code self written
    """Adjust image opacity (0 to 1)"""
    assert 0 <= opacity <= 1, "Opacity must be between 0 and 1."
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    alpha = img.split()[3]
    alpha = alpha.point(lambda p: p * opacity)
    img.putalpha(alpha)
    return img

def is_shorty(a):
    text = a[1]
    temp_font = a[3]
    temp_image = Image.new('RGB',(1,1))
    temp_draw = ImageDraw.Draw(temp_image)
    text = a[1]
    box = temp_draw.textbbox((0,0),text,temp_font)
    width = box[2] - box[0]
    return width

def text_working(a,img,text_img,details,i):
    os.environ['text_var'] = str(int(os.environ.get('text_var')) + 1)
    shorten = False
    if a[-2]:
        shorten = True
    if str(a[0][0]).isdigit():
        return a
    else:
        def is_short(text):
            temp_font = a[3]
            temp_image = Image.new('RGB',(1,1))
            temp_draw = ImageDraw.Draw(temp_image)
            text = a[1]
            box = temp_draw.textbbox((0,0),text,temp_font)
            width = box[2] - box[0]
            return width
        others = details.get('others')
        if others[i].get('shorten') == shorten:
            extra_text = ""
            while (details.get('main').get('dimensions')[0] - (is_short(a[1])+others[i].get('margin')[0]+others[i].get('margin')[2]))<0 and len(a[1].split())!=1:
                textji = a[1].split()
                a[1] = " ".join(textji[0:-1])
                if extra_text=="":
                    extra_text = textji[-1] + extra_text
                else:
                    extra_text = textji[-1] + " " + extra_text
            if (len(a[1].split())==1):
                while (details.get('main').get('dimensions')[0] - (is_short(a[1])+others[i].get('margin')[0]+others[i].get('margin')[2]))<0:
                    textji = a[1][0:len(a[1])//2]
                    textji2 = a[1][len(a[1])//2:]
                    a[1] = textji
                    if extra_text=="":
                        extra_text = "-" + textji2 + extra_text
                    else:
                        extra_text = "-" + textji2 + " " + extra_text
            if extra_text!="":
                b = copy.deepcopy(a)
                b[1] = extra_text
                b[0][1] += others[i].get('spacing')
                text_img.text(*text_working(b,img,text_img,details,i))
        if a[0][0]=='center':
            a[0][0] = (img.size[0] - is_short(a[1]))/2
        elif a[0][0]=='left':
            a[0][0] = 0
        elif a[0][0]=='right':
            a[0][0] = img.size[0] - is_short(a[1])

        if a[0][1]=='center':
            a[0][1] = (img.size[1] - is_short(a[1]))/2
        elif a[0][1]=='top':
            a[0][1] = 0
        elif a[0][1]=='bottom':
            a[0][1] = img.size[1] - is_short(a[1])
        return a

def create_asset(structure):
    details = structure
    if details.get('main').get('type')=="color":
        img = Image.new('RGB',details.get('main').get('dimensions'),details.get('main').get('color'))
    else:
        img = Image.new('RGB',(400,400),(255,255,255))
    drawimg = ImageDraw.Draw(img)
    border_color = details.get('main').get('border_color')
    border_thickness = details.get('main').get('border_width')
    def draw_strict_border(draw, width, height, border_thickness, color): #One of the 3 functions (only functions) taken from chatgpt ! was too lazy sry
        for i in range(border_thickness):
            draw.rectangle(
                [i, i, width - 1 - i, height - 1 - i],
                outline=color
            )
    draw_strict_border(drawimg,*details.get('main').get('dimensions'), border_thickness, border_color)
    others = details.get('others')
    for i in others:
        reqs = i.get('reqs')
        text_img = Image.new('RGBA',details.get('main').get('dimensions'),(255,255,255,0))
        text_img_drawn = ImageDraw.Draw(text_img)
        position = (0,0)
        if i.get('type')=='text':
            os.environ['text_var'] = str(0)
            a = reqs
            temp_font = a[3]
            temp_image = Image.new('RGB',(1,1))
            temp_draw = ImageDraw.Draw(temp_image)
            text = a[1]
            box = temp_draw.textbbox((0,0),text,temp_font)
            height = box[3] - box[1]
            width = box[2] - box[0]

            text_img_drawn.text(*text_working(a,text_img,text_img_drawn,details,others.index(i)))
            if i.get('margin'):
                if reqs[0][1]<i.get('margin')[1]:
                    reqs[0][1] = i.get('margin')[1]
                if height + reqs[0][1] > structure.get('main').get('dimensions')[1]-i.get('margin')[3]:
                    reqs[0][1] = structure.get('main').get('dimensions')[1]-i.get('margin')[3]
                if reqs[0][0]<i.get('margin')[0]:
                    reqs[0][0] = i.get('margin')[0]
                if width + reqs[0][0] > structure.get('main').get('dimensions')[0]-i.get('margin')[2]:
                    reqs[0][0] = structure.get('main').get('dimensions')[0]-i.get('margin')[2]

            if (len(others)-1)!=others.index(i) and details.get('main').get('self_distance')!=None:
                if others[others.index(i)+1].get('type')=='text':
                    tempbot = others[others.index(i)+1].get('reqs')[0][1]
                    if type(tempbot)==str:
                        wdi = is_shorty(others[others.index(i)+1].get('reqs'))
                        if (tempbot=="center"):
                            gg = (details.get('main').get('dimensions')[1])//2
                        elif (tempbot=='top'):
                            gg = 0
                        elif (tempbot=="bottom"):
                            gg = details.get('main').get('dimensions'[1]) - wdi
                    n = 1
                    while (height*int(os.environ.get('text_var')) + others[others.index(i)].get('spacing')*(int(os.environ.get('text_var'))-1) +a[0][1]>gg):
                        print(others[others.index(i)+1]['reqs'][0][1])
                        print(gg)
                        if n==1:
                            others[others.index(i)+1]['reqs'][0][1] = gg + others[others.index(i)].get('spacing')
                            n+=1
                        else:
                            others[others.index(i)+1]['reqs'][0][1] += others[others.index(i)].get('spacing')
                        gg = others[others.index(i)+1]['reqs'][0][1]
            
        elif i.get('type')=='rectangle':
            text_img_drawn.rectangle(*reqs)
        elif i.get('type')=='line':
            text_img_drawn.line(*reqs)
        elif i.get('type')=='ellipse':
            text_img_drawn.ellipse(*reqs)
        elif i.get('type')=='polygon':
            text_img_drawn.polygon(*reqs)
        elif i.get('type')=='point':
            text_img_drawn.point(*reqs)
        elif i.get('type')=='arc':
            text_img_drawn.arc(*reqs)
        elif i.get('type')=='chord':
            text_img_drawn.chord(*reqs)
        elif i.get('type')=='pieslice':
            text_img_drawn.pieslice(*reqs)
        elif i.get('type')=='textbbox':
            text_img_drawn.textbbox(*reqs)
        elif i.get('type')=='textlength':
            text_img_drawn.textlength(*reqs)
        elif i.get('type')=='bitmap':
            text_img_drawn.bitmap(*reqs)
        elif i.get('type')=='image':
            small_img = Image.open(i.get('location'))
            if i.get('rotate'):
                small_img = small_img.rotate(i.get('rotate'),expand=True)
            if i.get('crop'):
                small_img = small_img.crop(*i.get('crop'))
            if i.get('round_corners'):
                small_img = round_corners(small_img,i.get('round_corners'))
            if i.get('scale'):
                small_img = small_img.resize(*i.get('scale'))
            if i.get('opacity'):
                small_img = reduce_opacity(small_img,*i.get('opacity'))
            wid,hei = small_img.size
            a = list(i.get('position'))
            if a[0]=='center':
                a[0] = (details.get('main').get('dimensions')[0] - wid)//2
            elif a[0]=='left':
                a[0] = 0
            elif a[0]=='right':
                a[0] = details.get('main').get('dimensions')[0] - wid

            if a[1]=='center':
                a[1] = (details.get('main').get('dimensions')[1] - hei)//2
            elif a[1]=='top':
                a[1] = 0
            elif a[1]=='bottom':
                a[1] = details.get('main').get('dimensions')[1] - hei

            img.paste(small_img,tuple(a),small_img)


        if i.get('rotate'):
            text_img = text_img.rotate(i.get('rotate'),expand=True)
        if i.get('crop'):
            text_img = text_img.crop(*i.get('crop'))
        if i.get('round_corners'):
            text_img = round_corners(text_img,i.get('round_corners'))
        if i.get('scale'):
            text_img = text_img.resize(*i.get('scale'))
        if i.get('opacity'):
            text_img = reduce_opacity(text_img,*i.get('opacity'))
        bg_width,bg_height = img.size
        front_width,front_height = text_img.size
        position = ((bg_width - front_width)//2,(bg_height - front_height)//2)
        img.paste(text_img,position,text_img)

    temp = details.get('main')
    if temp.get('rotate'):
        img = img.rotate(temp.get('rotate'),expand=True)
    if temp.get('crop'):
        img = img.crop(*temp.get('crop'))
    if temp.get('round_corners'):
        img = round_corners(img,temp.get('round_corners'))
    if temp.get('scale'):
        img = img.resize(*temp.get('scale'))
    if temp.get('opacity'):
        img = reduce_opacity(img,*temp.get('opacity'))
    return img