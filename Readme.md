Hi ! This is [@YogyaChugh](https://github.com/YogyaChugh)!

<h1>WELCOME TO MY REPO !</h1>

I have made this game for educational purposes only and it's inspired from Monopoly ! License attached in Repo


![landing_page](https://github.com/user-attachments/assets/4936e8ab-5422-4918-a1af-39bd0bb4c96b)


FOR CODERS
=

The arrangement and structure of each file and how everything works is explained below as well as proper
comments have been added in respective files (except json - cause not possible)!

>**NOTE:** &nbsp;Assets/Images at the google drive link have been generated partially (some google) by ChatGPT and acc. to the
      rules, are not under any copyright issues.

<br>

LOGIC
=

The Game is structured in a way to allow maps/boards to be stored online at the google drive whereas, keeping the other files
for building assets, running game and the main game interface locally packaged with the app.
This allows small apk size and also updating the google drive automatically updates the game because it checks for update
whenever internet is on !

The remote files contain information ranging from list of permanent files to store, or temporary files and settings for asset
creation locally !
The asset creation files are python files with information on how to build each card/board/any asset and where to save,etc..

Along with that a main file (also other code files if set) which will run the logic of that map is packaged. This is done 
cause there could be varying logics of each board/map.

>Asset Creation and Builder logic is kept locally to reduce data usage while downloading

Whenever user downloads the map, the files are downloaded, stored temporarily, assets are built and permanent files required
for functioning of that map are saved, temporary files deleted. The map is then tested (this one not implemented yet) and then
map is downloaded once and for all (unless user deletes it from storage) which can be played anytime triggering the main file
downloaded earlier.


>More information on how everything works with details are in the docs ! This is just to give a general idea of how the game functions !

THANK YOU !
=

Contact:- yogya.developer@gmail.com
