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
I started off the project by creating a 3x3 grid and I found that if I used the Pygame [Rect](https://www.pygame.org/docs/ref/rect.html) object to create 9 smaller squares, I could find the specific x/y coordinates to create a grid. To achieve this I used two For loops so that I wasn't repeating code and I also used used the Pygame [Draw](https://www.pygame.org/docs/ref/draw.html) module to draw the grid to the screen. 

### Creating Sprites

### Creating the Different Screens

### Programming the Game Logic

### Programming User Input

### Finishing Touches

## The Database
For the database I used:
* SQlite3: https://www.sqlite.org/

In the sqlite database I created a table called scores, which had id, name and score columns. I created three queries for the project.

## The Website:
For the website I used:
* Flask: https://flask.palletsprojects.com/en/3.0.x/
* HTML: https://developer.mozilla.org/en-US/docs/Web/HTML
* CSS: https://developer.mozilla.org/en-US/docs/Web/CSS

### Introduction
For the website, I just created a simple outline with HTML to begin with and then I added the CSS styling on top of that.
