import copy
import os

from PIL import Image, ImageDraw


def round_corners(
    im, radius
):  # One of the 3 things taken from Chatgpt - Rest code self written
    circle = Image.new("L", (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)

    alpha = Image.new("L", im.size, 255)
    w, h = im.size
    t1 = radius * 2
    t2 = w - radius
    t3 = h - radius

    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle.crop((radius, radius, t1, t1)), (t2, t3))

    im.putalpha(alpha)
    return im


def reduce_opacity(
    img, opacity
):  # One of the 3 things taken from Chatgpt - Rest code self written
    """Adjust image opacity (0 to 1)"""
    assert 0 <= opacity <= 1, "Opacity must be between 0 and 1."
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    alpha = img.split()[3]
    alpha = alpha.point(lambda p: p * opacity)
    img.putalpha(alpha)
    return img


def is_shorty(a):
    # Returns the width based on the 'reqs' tuple provided
    # (cause it's a text, it's assumed that [0] is the coordinates,
    # [1] is the text, [2] is the color and [3] is the font)
    text = a[1]
    temp_font = a[3]
    temp_image = Image.new("RGB", (1, 1))
    temp_draw = ImageDraw.Draw(temp_image)
    text = a[1]
    box = temp_draw.textbbox((0, 0), text, temp_font)
    width = box[2] - box[0]
    return width


def text_working(a, img, text_img, details, i):
    # Primarily, returns the positions of the text after judging diff
    # parameters like center,left,top,bottom,right and shorten and spacing
    # But if the text is oversized respective to the asset dimensions,
    # it adds the new cropped text to the image provided
    # a -> 'refs' , img -> Temporary image,
    # text_img -> Temporary image drawn object ,
    # details-> structure details,
    # i-> Index of the text in the others dict of structure
    os.environ["text_var"] = str(
        int(os.environ.get("text_var")) + 1
    )  # For checking of number of recursive calls
    shorten = False
    if a[-2]:
        shorten = True

    def is_short(text):  # Returns width of text
        temp_font = a[3]
        temp_image = Image.new("RGB", (1, 1))
        temp_draw = ImageDraw.Draw(temp_image)
        text = a[1]
        box = temp_draw.textbbox((0, 0), text, temp_font)
        width = box[2] - box[0]
        return width

    others = details.get("others")  # Dictionary of text,images,etc... to add
    if (
        others[i].get("shorten") == shorten
    ):  # If shortening/auto adjusting of text is ON
        extra_text = ""

        # Do it till the text is oversized
        ttt = others[i].get("margin")
        while (
            details.get("main").get("dimensions")[0]
            - (is_short(a[1]) + ttt[0] + ttt[2])
        ) < 0 and len(a[1].split()) != 1:
            textji = a[1].split()
            a[1] = " ".join(textji[0:-1])
            # Just adds the additional text to extra_text
            if extra_text == "":
                extra_text = textji[-1] + extra_text
            else:
                extra_text = textji[-1] + " " + extra_text

        # This is for 1 loooong word taking being oversized
        if len(a[1].split()) == 1:
            # Almost same to above one !
            while (
                details.get("main").get("dimensions")[0]
                - (
                    is_short(a[1])
                    + others[i].get("margin")[0]
                    + others[i].get("margin")[2]
                )
            ) < 0:
                textji = a[1][0 : len(a[1]) // 2]
                textji2 = a[1][(len(a[1]) // 2) : len(a[1])]
                a[1] = textji
                if extra_text == "":
                    extra_text = "-" + textji2 + extra_text
                else:
                    extra_text = "-" + textji2 + " " + extra_text

        # Adds the extra text to the lower to the image
        if extra_text != "":
            b = copy.deepcopy(a)
            b[1] = extra_text
            b[0][1] += others[i].get("spacing")
            text_img.text(*text_working(b, img, text_img, details, i))

    if (
        str(a[0][0]).isdigit() and str(a[0][1]).isdigit()
    ):  # What if both coordinates are numbers
        return a

    # Auto fetches the coordinates based on the string
    if a[0][0] == "center":
        a[0][0] = (img.size[0] - is_short(a[1])) / 2
    elif a[0][0] == "left":
        a[0][0] = 0
    elif a[0][0] == "right":
        a[0][0] = img.size[0] - is_short(a[1])
    if a[0][1] == "center":
        a[0][1] = (img.size[1] - is_short(a[1])) / 2
    elif a[0][1] == "top":
        a[0][1] = 0
    elif a[0][1] == "bottom":
        a[0][1] = img.size[1] - is_short(a[1])
    return a


def create_asset(structure):
    details = structure

    # Could be color background or image background
    if details.get("main").get("type") == "color":
        img = Image.new(
            "RGBA",
            details.get("main").get("dimensions"),
            details.get("main").get("color"),
        )
    else:  # Means Image
        img = Image.new(
            "RGBA", details.get("main").get("dimensions"), (255, 255, 255, 1)
        )

    drawimg = ImageDraw.Draw(img)
    border_color = details.get("main").get("border_color")
    border_thickness = details.get("main").get("border_width")

    # Draws the border
    def draw_strict_border(
        draw, width, height, border_thickness, color
    ):  # One of the 3 functions (only functions)
        # taken from chatgpt ! was too lazy sry

        for i in range(border_thickness):
            tempagain1 = width - 1 - i
            tempagain2 = height - 1 - i
            draw.rectangle([i, i, tempagain1, tempagain2], outline=color)

    againtemp = details.get("main").get("dimensions")
    draw_strict_border(drawimg, *againtemp, border_thickness, border_color)

    others = details.get("others")
    # Loops through each entity meaning text,images,etc...
    # in the others var in structure of that type
    for i in others:
        reqs = i.get("reqs")
        text_img = Image.new(
            "RGBA", details.get("main").get("dimensions"), (255, 255, 255, 0)
        )  # Temp image for blitting it on the main image/color photo
        text_img_drawn = ImageDraw.Draw(text_img)  # Drawn on canvas
        position = (0, 0)
        if i.get("type") == "text":
            os.environ["text_var"] = str(0)
            a = reqs
            temp_font = a[3]
            temp_image = Image.new("RGB", (1, 1))
            temp_draw = ImageDraw.Draw(temp_image)
            text = a[1]
            box = temp_draw.textbbox((0, 0), text, temp_font)
            height = box[3] - box[1]
            width = box[2] - box[0]

            ss = text_img_drawn
            text_img_drawn.text(
                *text_working(a, text_img, ss, details, others.index(i))
            )  # Draws it man

            # Margin is resolved here ! Too basic to explain
            gtemp = structure.get("main").get("dimensions")
            if i.get("margin"):
                if reqs[0][1] < i.get("margin")[1]:
                    reqs[0][1] = i.get("margin")[1]
                if (
                    height + reqs[0][1]
                    > gtemp.get("dimensions")[1] - i.get("margin")[3]
                ):
                    reqs[0][1] = gtemp[1] - i.get("margin")[3]
                if reqs[0][0] < i.get("margin")[0]:
                    reqs[0][0] = i.get("margin")[0]
                if width + reqs[0][0] > gtemp[0] - i.get("margin")[2]:
                    reqs[0][0] = gtemp[0] - i.get("margin")[2]

            # This one just self distances based on the setting as in
            # "self_distance" if something is overlaping other entity
            te = details.get("main")
            if (len(others) - 1) != others.index(i) and te.get(
                "self_distance"
            ) is not None:
                if others[others.index(i) + 1].get("type") == "text":
                    tempbot = others[others.index(i) + 1].get("reqs")[0][1]
                    if isinstance(tempbot, str):
                        wdi = is_shorty(
                            others[others.index(i) + 1].get("reqs")
                        )  # What if the dimensions contain string like
                        # center,top,etc.. and not number

                        det = details.get("main").get("dimensions")

                        if tempbot == "center":
                            gg = (det[1]) // 2
                        elif tempbot == "top":
                            gg = 0
                        elif tempbot == "bottom":
                            gg = det[1] - wdi
                    n = 1

                    # This applies the spacing
                    while (
                        height * int(os.environ.get("text_var"))
                        + others[others.index(i)].get("spacing")
                        * (int(os.environ.get("text_var")) - 1)
                        + a[0][1]
                        > gg
                    ):
                        temporary = others[others.index(i) + 1]
                        othertemp = others[others.index(i)]
                        # First time its set directly and second time, added !
                        temptemp = othertemp.get("spacing")
                        if n == 1:
                            temporary["reqs"][0][1] = gg + temptemp
                            n += 1
                        else:
                            temporary["reqs"][0][1] += othertemp.get("spacing")
                        gg = temporary["reqs"][0][1]

        # All other types
        elif i.get("type") == "rectangle":
            text_img_drawn.rectangle(*reqs)
        elif i.get("type") == "line":
            text_img_drawn.line(*reqs)
        elif i.get("type") == "ellipse":
            text_img_drawn.ellipse(*reqs)
        elif i.get("type") == "polygon":
            text_img_drawn.polygon(*reqs)
        elif i.get("type") == "point":
            text_img_drawn.point(*reqs)
        elif i.get("type") == "arc":
            text_img_drawn.arc(*reqs)
        elif i.get("type") == "chord":
            text_img_drawn.chord(*reqs)
        elif i.get("type") == "pieslice":
            text_img_drawn.pieslice(*reqs)
        elif i.get("type") == "textbbox":
            text_img_drawn.textbbox(*reqs)
        elif i.get("type") == "textlength":
            text_img_drawn.textlength(*reqs)
        elif i.get("type") == "bitmap":
            text_img_drawn.bitmap(*reqs)
        elif i.get("type") == "image":
            small_img = Image.open(i.get("location"))

            # New image altering
            if i.get("rotate"):
                small_img = small_img.rotate(i.get("rotate"), expand=True)
            if i.get("crop"):
                small_img = small_img.crop(*i.get("crop"))
            if i.get("round_corners"):
                small_img = round_corners(small_img, i.get("round_corners"))
            if i.get("scale"):
                small_img = small_img.resize(*i.get("scale"))
            if i.get("opacity"):
                small_img = reduce_opacity(small_img, *i.get("opacity"))
            wid, hei = small_img.size
            a = list(i.get("position"))
            if a[0] == "center":
                a[0] = (details.get("main").get("dimensions")[0] - wid) // 2
            elif a[0] == "left":
                a[0] = 0
            elif a[0] == "right":
                a[0] = details.get("main").get("dimensions")[0] - wid

            if a[1] == "center":
                a[1] = (details.get("main").get("dimensions")[1] - hei) // 2
            elif a[1] == "top":
                a[1] = 0
            elif a[1] == "bottom":
                a[1] = details.get("main").get("dimensions")[1] - hei

            img.paste(small_img, tuple(a), small_img)

        # Applies to all and alters the temporary image,i.e., text_img
        if i.get("rotate"):
            text_img = text_img.rotate(i.get("rotate"), expand=True)
        if i.get("crop"):
            text_img = text_img.crop(*i.get("crop"))
        if i.get("round_corners"):
            text_img = round_corners(text_img, i.get("round_corners"))
        if i.get("scale"):
            text_img = text_img.resize(*i.get("scale"))
        if i.get("opacity"):
            text_img = reduce_opacity(text_img, *i.get("opacity"))
        bg_width, bg_height = img.size
        front_width, front_height = text_img.size
        w = bg_width - front_width
        h = bg_height - front_height
        position = (w // 2, h // 2)

        # Calculates the new position and then pastes the temp
        # image cause dimensions alter based on the alterations applied
        img.paste(text_img, position, text_img)

    # Alterations to the main background !
    temp = details.get("main")
    if temp.get("rotate"):
        img = img.rotate(temp.get("rotate"), expand=True)
    if temp.get("crop"):
        img = img.crop(*temp.get("crop"))
    if temp.get("round_corners"):
        img = round_corners(img, temp.get("round_corners"))
    if temp.get("scale"):
        img = img.resize(*temp.get("scale"))
    if temp.get("opacity"):
        img = reduce_opacity(img, *temp.get("opacity"))
    return img  # Finally returns the image
