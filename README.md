# CS50xFinalProject - Whack a Duck
#### Name: 
Aimee Taylor
#### Place: 
Channel Islands, Guernsey
#### Video Demo:
https://youtu.be/azQVlJNg-yQ 
#### Description:
For my final project I created a website that includes a whack a mole inspired game and a highscore table. The website was built using HTML and CSS for the frontend and Flask for the backend. The game was made using Python and the highscore table was created using SQLite3. I decided on this project because I wanted to showcase the skills that I picked up during the CS50x course. 

## The Game
For the game I used: 
* Python: https://www.python.org/
  * Pygame: https://www.pygame.org/docs/
  * Pygbag: https://pypi.org/project/pygbag/0.3.2/

### Introduction
I approached the game first when I started programming as it was the part of the project that was going to be the most complex. After researching games made in Python I found the Pygame module would be a good option to use. [Pygame](https://github.com/pygame/pygame) is a free and open source library for the development of multimedia applications, such as video games. Pygame includes tools for 2D graphics, support for different types of input and collision detection, all of which I used in different parts of my game. I then realised embedding the python game was going to be a challenge as Python needs an interpreter to run. There was also an added challenge of using Pygame as some tools that would allow you to embed Python into a website didn't support Pygame. I then found [Pygbag](https://pygame-web.github.io/wiki/pygbag/) which is a module which allows you to package Pygame code and run it on the web. 

### Creating the Grid
I started off the project by creating a 3x3 grid and I found that if I used the Pygame [Rect](https://www.pygame.org/docs/ref/rect.html) object to create 9 smaller squares (or grid cells), I could find the specific x/y coordinates to create a grid. To achieve this I used two For loops so that I wasn't repeating code and I used the Pygame [Draw](https://www.pygame.org/docs/ref/draw.html) module to draw the grid to the screen. Within that For loop I also used the Draw module to add a circle to the center of each of the grid cells and I then added the x/y coordinates of each of these circles into a list so I could use them later. The circles are where the duck and fish sprites will appear in during the game.

### Creating Sprites
I used the Pygame [Sprites](https://www.pygame.org/docs/ref/sprite.html) module to create a Class that I could use for all of the sprites in the game. The Class I created was called gameSprites and within this class I had two properties, img and clicked. img was the path to the image I created for the sprite and clicked was only used for the Duck and Fish sprites to track whether or not they had been clicked. 

### Creating the Different Screens
In the game I had 5 different screens: title screen, instruction screen, game screen, end game screen and score input. For the title screen I created three buttons: one to start the game, one to end the game and one to exit. I positioned all of the buttons in the center of the screen and I also spread them vertically across the screen. Then for the background of the title screen I picked out a colour from the [colour scheme](https://colorhunt.co/palette/1b262c0f4c753282b8bbe1fa) I found. For the instructions screen I kept the same background and added an image explaining all of the instructions and a button linking back to the title screen. The game screen was the most complex as I had to design around the grid I had already created earlier. I added a background to the grid and to the circles in the cells of the grid too. I also created a background to set the timer and score labels on and I made the screen background a lighter colour to differenciate the main game from the other 4 screens. The end game screen had a background image and on top of that I added labels to say what score the user got. The score input screen used the same background image as the previous screen and it just had an input field to add the username and a label telling the user what to do. When the user then presses enter the screen changes and a label is in the center of the screen telling the user the username has been submitted.

### Programming the Game Logic
I started off by creating the timer and score labels on the main game screen. For the timer I used the Pygame [Time](https://www.pygame.org/docs/ref/time.html) module and that allowed me to set a timer for 30 seconds and then I used a timer event to decrease the time as the game was running. For both the timer and score labels on the game screen I used the Pygame [Font](https://www.pygame.org/docs/ref/font.html) module to load a specific font I had found online that I thought would work well for the project. The timer event would then change the time on the font as the timer was running out and the score would change based on the number stored in the score variable. Next I worked on how to change the position of the duck and fish sprites. To do this I used the Time module again to check if 500ms had elapsed, if it had a random number from 0-8 would be generated for each sprite and each of those 9 numbers corresponds to a cell in the grid. I then used an If statement to check that the numbers weren't the same; If they were one of the random number would be generated again. The sprites then get assigned to their specific cell by adding the cell x/y coordinates to them using the circles list and the generated random numbers to get the right cell in the list. The sprites are then added to the screen bu using the Pygame [blit](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit) function from the [Surface](https://www.pygame.org/docs/ref/surface.html) module. This then repeats until the timer runs out. Once the timer runs out the screen changes from the main game screen to the end game screen and depending on if the score is greater than 0 or not a different message will appear. I again used the Font module for all of the text on the screen and I also used the Pygame [subsurface](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.subsurface) function to create a surface to add all of the text to and then I could move the subsurface to the correct position on the main screen without spending ages moving each bit of text. If the score is 0 or less, I added an exit button which would just end the program. If the score was greater than 0, I added a next button which would then change the screen to the score input screen. For the score input screen all the text was again added using the Font module and the only thing that was really different on this screen was that once the user has pressed enter the screen will reset and then show a message which informs the user that the username has been submitted. The last thing that happens on this screen is that an exit button is added to the screen which will then end the program.

### Handling Events
The game is run using a Pygame event within a While loop. The While loop runs continuously whilst the game is running and includes all of the collision events, input events, game states and the timer event. The collision events were used quite a lot in the game and the Pygame Rect module has a [collidepoint](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) function which checks whether a point is present within the Rect object. The pygame sprites include a Rect object so the collidepoint function can be used quite seamlessly with the sprites I've made. I used the collidepoint function and the MOUSEBUTTONDOWN event (which is one of the events in the Pygame [Event](https://www.pygame.org/docs/ref/event.html) module for all of the buttons on each of the screens and using that would allow me to change the screens/exit the program if the button is clicked. The other time I use the collidepoint function is during the game to record when the duck or fish sprite is clicked. If the collidepoint function returns true during the game when one of the game sprite is clicked the score will increase/decrease depending on which sprite is clicked and the gameSprite clicked parameter can also be set to true to ensure that the player can only click each sprite once every 500ms. For the user input I used the KEYDOWN event to check if the player is typing and this event also has a unicode attribute which I can use to add the specific key the player types to the input field and display that on the screen. I then used the K_BACKSPACE key event to allow the player to edit the user input as they are typing. The last input event that I used was the K_RETURN key event to allow the player to submit their input. To call different functions in my code I use an If/Else statement in the main While loop which checks what the value of the gameState variable is and depending on the value a different function in the code will be called. This is how I change between screens and different sections of my code. In the main While loop I use the timer event to decrease the timer and also to update the text of the timer so the player can see an accurate display of the timer on the main game screen. 

## The Database
For the database I used:
* SQlite3: https://www.sqlite.org/

### Overview
In the sqlite database I created a table called scores, which had id, name and score columns. The table is going to hold all of the scores from the players of the game and it then can be displayed on the website to show who has the high score. I only really needed three queries for this project: one to create the table, one to insert into the table and one to select the table data to display in the website.
```
CREATE TABLE scores(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, score INTEGER NOT NULL);
INSERT INTO scores (name, score) VALUES (?,?);
SELECT RANK() OVER (ORDER BY score DESC) Rank, name, score FROM scores ORDER BY score DESC;
```
### Difficulities Writing to Database
To start with the code to write to the database was located within the game code and if run in Python it worked perfectly, but I found that when the game was run via the Pygbag packager, I couldn't see the updates and from the outside it looked like nothing was getting commit to the database file. After a lot of research and experimentation I finally found that the game was writing to a copy of the database file in the Python REPL within the packager instead of the file I had locally with the rest of my project. I did find a workaround to this, but it definitely isn't the tidiest. The workaround was to get the Python game code to write the data I needed to a text file, then to download that text file from the Python REPL to the local downloads drive on my computer. From there I used my Flask code to get the file, read it and get the data from it before deleting the file from the local downloads drive. I then could update the database from the Flask code and then refresh the page on the website to see the changes to the database in the table. 

## The Website:
For the website I used:
* Flask: https://flask.palletsprojects.com/en/3.0.x/
* HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
* CSS: https://developer.mozilla.org/en-US/docs/Web/CSS

### Overview
For the website I used Flask for the backend and HTML and CSS for the frontend. Within the Flask code is a route for the homepage of the website, which in this case is the only page as well. In that route is an index function which is run when the page is loaded/reloaded. 

### Flask
I used Flask for the backend of the website and 

### HTML

### CSS
For the styling I kept it pretty simple and kept the same colour scheme as I used in the game. I made the background dark and positioned the game and highscore table in the center of the page with a light blue border to differenciate it from the background. I then found a font that I liked for the heading and once that was added the styling was done.
