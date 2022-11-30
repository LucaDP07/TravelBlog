# Flags Game

**SITE OVERVIEW**
- - - 

The Flags Game is a way to test and train the player's reaction time, while having fun.

The player has to deal with a different set of six flags every three seconds. Five of these represent the Irish flag, while the last one it's the flag of the Ivory Coast, very similar to the Irish one. The player needs to catch the Ivory Coast flag (the intruder). Everytime the player clicks on the Ivory Coast flag a point will be added to the score, and to make sure the player is paying attention, every click on the Irish flag will take away 2 points.

![Alternate text](/assets/images/Responsive.png)

You can view the deployed website [here](https://lucadp07.github.io/flags-game/).

**UX**
- - -

The website is designed for any type of screen in mind (Desktop, Smartphone and Tablet). The structure of each section is simple, user friendly and clear. The selection of colors are inspired by the Irish and Ivory Coast flag, which are the core of the game. The main board has been created to contain the instructions, the game itself and a message showing the final score. All this provides a familiar and not confusing experience to the user. 

**User Stories**

As someone who is passionate about reaction time games, I want to challenge my reflexes.

As a flags lover I would like to experience a game based on flags. 

As a random gamer I would like to experience a clear design for each section and an easy navigation through all of them.

**WIREFRAMES**
- - -

**Home Page**

![Alternate text](/assets/images/1desktop.png)

**Game Page**

![Alternate text](/assets/images/2desktop.png)

**Final Score Page**

![Alternate text](/assets/images/3desktop.png)

**Home Page: Tablet View**

![Alternate text](/assets/images/1tablet.png)

**Game Page: Tablet View**

![Alternate text](/assets/images/2tablet.png)

**Home Page: Mobile View**

![Alternate text](/assets/images/1smartphone.png)

**Game Page: Mobile View**

![Alternate text](/assets/images/2smartphone.png)


**FEATURES**
- - -

 - The Game Logo and Heading
 
 At the top of the page the user can find the logo and the heading of the game. These two features are consistent in all the sections.

 ![Alternate text](/assets/images/title.png)

- The Instructions

Here the user can find the rules of the game explained. Before starting to have fun, a quick look at the instructions will help to enjoy the game.

![Alternate Text](/assets/images/Instructions.png)

 - The Start Button
 
 Right below the logo and the heading, the user can find the Start Button. Once the player has read the instructions, can simply click on ther button to start to play. In the Game Area the button will still be there and everytime the user will ends a game, simply by clicking the button a new game will be started.

 ![Alternate text](/assets/images/StartButton.png)

 - The Board Game
 
 Once the user clicks on the Start Button, the game starts. The instructions will be replaced by a different set of six flags will be visible every 3 seconds. Five of these represent the Irish flag, while the last one it's the Ivory Coast flag, very similar to the Irish one. The player has 20 seconds to catch the Ivory Coast flag as many times as possible. Everytime the player clicks on the Ivory Coast flag a point will be added to the score, and to make sure the player is paying attention, every click on the Irish flag will take away 2 points.

 ![Alternate text](/assets/images/board.png)
 
 - The Current Score Area
 
 Under the Start Button, the user can see the Current Score Area, which will be visible only in the Game Area. The score gets updated everytime the player clicks on the right or wrong flag. In this way the user has the chance to keep track of his/her performance.

 ![Alternate text](/assets/images/CurrentScore.png)

 - The Score Area and the Timer

 Under the Board Game, the user can find a timer of 20 seconds which will help to keep track of the time left to complete the game. Also, under the timer, the player can find the resume of the games won and lost. The colors choosen for it are green and orange as a connection to the irish flag.

 ![Alternate text](/assets/images/timer.png)

  - The Final Score Message

 Once the 20 seconds are over the Game Board will display the final score which will replace the flags.

 ![Alternate text](/assets/images/ScoreMessage.png)
 

**TECHNOLOGIES USED**
- - -

- HTML: HTML has been used to give structure and content to the website.
- CSS: In order to style the content created with HTML, the CSS language has been used.
- Google Fonts: I used the Kanit and sans-serif font.
- Font Awesome: I used ther Font Awesome icons for the logo of the game located at the left of the heading.
- Pixabay: I used this platform for the images of the flags.
- Balsamiq Wireframes: I used it to produce low fidelity wireframes to organise the structure of the pages.


**TESTING**
- - - 

All the pages of the website have ben tested using the developer tools in Google Chrome. The code had to be changed along the process in order to achieve the responsiveness required for the project. The preview from Gitpod helped to constantly check all the changes made.

Testing was performed using a MacBook Air (M1, 2020) on macOS Monterey with the following browsers:
- Google Chrome 102.0.5005.61
- Safari 15.3
- Mozilla Firefox 101.0.1

After testing the website I can confirm the project it's responsive in its all pages and works properly on all standard screen sizes.

The "Play" button is working in each section of the project. 
- In the Home Page the button starts the game. 
- In the Board Game/Game Area the button reset the score and starts a new game.


- BUGS

While on GitPod I was able to see the flags flashing in the Board Game, after the deployment, the live site was not showing the same results as on GitPod. Since I was refencing my images from my css file, I had to tell the server to come out of the css folder. Sorted fixing the path.

* VALIDATOR TESTING

HTML: No errors were returned when passing through the official W3C Validator. (https://validator.w3.org/nu/#textarea).

CSS: No errors were returned when passing through the official (Jigsaw) Validator (https://jigsaw.w3.org/css-validator/validator).

JavaScript: No errors were found on the website when using [JSHint Validator]https://jshint.com/ .

Accessibility: I generated a desktop and mobile report for the deployed site through the Google Chrome Dev Tools.

 - Home Page - Mobile
 ![Alternate text](/assets/images/lighthouse.png)
 - Home Page - Desktop
 ![Alternate text](/assets/images/lighthouse_desktop.png)

 
- UNFIXED BUGS

No unfixed bugs.

**DEPLOYMENT**
- - -
The site was deployed to GitHub Pages. The steps to deploy are as follows:

1. Navigate to my Github repository: https://github.com/LucaDP07/flags-game
2. In the GitHub repository navigate to the settings tab.
3. Select the pages link from the setting menu on the left hand side.
4. After selecting the main branch, the page provides the link to the completed website
The live link can be found here: https://lucadp07.github.io/flags-game/

**CREDITS**
- - - 

**Content**

- The Heading and the Logo were inspired by the [Love Maths](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LM101+2021_T1/courseware/2d651bf3f23e48aeb9b9218871912b2e/a8ec361b95e94c25bf8a821654bd57bc/?child=first) Project.

- The Timer structure was inspired by [WEB CIFAR](https://www.youtube.com/c/WEBCIFAROfficial).

- The Score Area was inspired by the [Love Maths](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LM101+2021_T1/courseware/2d651bf3f23e48aeb9b9218871912b2e/a8ec361b95e94c25bf8a821654bd57bc/?child=first) Project.

- The Javascript code was inspired by the book [Get Coding](https://getcodingkids.com/the-book/).


**Media**

- The icon used for the logo was taken from [Font Awesome](https://fontawesome.com/).

- All fonts imported from [Google Fonts](https://fonts.google.com/).

- Screenshot under the section "site overview" was created with [Am I responsive](https://ui.dev/amiresponsive).

- Pictures used for the Game have been taken from [Pixabay](https://pixabay.com/).

- The wireframes have been created using [Balsamiq Wireframes](https://balsamiq.com/wireframes/).