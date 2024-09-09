
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
The game is run using a Pygame event within a While loop. The While loop runs continuously whilst the game is running and includes all of the collision events, input events, game states and the timer event. The collision events were used quite a lot in the game and the Pygame Rect module has a [collidepoint](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidepoint) function which checks whether a point is present within the Rect object. The pygame sprites include a Rect object so the collidepoint function can be used quite seamlessly with the sprites I've made. I used the collidepoint function for all of the buttons on each of the screens and using that would allow me to change the screens/exit the program if the button is clicked. The other time I use the collidepoint function is during the game to record when the duck or fish sprite is clicked. If the collidepoint function returns true during the game when one of the game sprite is clicked the score will increase/decrease depending on which sprite is clicked and the gameSprite clicked parameter can also be set to true to ensure that the user can only click each sprite once every 500ms. For the user input 

### Finishing Touches

## The Database
For the database I used:
* SQlite3: https://www.sqlite.org/

### Introduction
In the sqlite database I created a table called scores, which had id, name and score columns. I created three queries for the project.

## The Website:
For the website I used:
* Flask: https://flask.palletsprojects.com/en/3.0.x/
* HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
* CSS: https://developer.mozilla.org/en-US/docs/Web/CSS

### Introduction
For the website, I just created a simple outline with HTML to begin with and then I added the CSS styling on top of that.
