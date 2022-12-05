# TravelDream

**SITE OVERVIEW**
- - - 

TravelDream is travel blog where users can share their own travel experiences, a place to build a home for their stories and where they can also enjoy the contents created by other users and, why not, get inspired for their next adventure.

![Alternate text](/static/images/responsive.png)

You can view the deployed website [here](https://traveldream.herokuapp.com/).

**UX**
- - -

**User Goals**

- Find out the purpose of the website.
- View, create, edit and delete their own post on the website.
- View posts created by other users and being able to like and comment them.

**Site Owners goals**

- Non registered users are not able to like or comment any post.
- Comments need to be approved in order to guarantee safe contents to the users.
- Posts and comments can be controlled through the admin area to avoid an inappropriate use of the website.

**Epic and User Stories**

There are 6 EPICS and 13 USER STORIES.

1.EPIC: Set up admin page for admin to manage trips posts
- USER STORIES: 
1. As a site admin I can view the number of likes on a post so that I can see which post is more liked.(View Likes #24)
2. As a site admin I can view comments of trip posts so that I can read the commentary on a post.(View Comments #27)
3. As a site admin I can create comments of trips posts so that I can generate discussion on a post.(Create Comments #26)
4. As a site admin I can approve or disapprove comments so that I can guarantee safe contents to the users.(Approve Comments #20)
5. As a site admin I can CRUD the contents so that users can enjoy a safe use of the page.(CRUD #18)

2.EPIC: Enable users to set up an account on the website to access the full features.
- USER STORIES:
1. As a user I can create an account so that I can interact with the website with likes, comments and creating my own posts.(Create Account #16)
2. As a registered user I can login and logout of the site so that I can access my content.(LogIn/LogOut #28)

3.EPIC: Create landing page to attract users to the site.
- USER STORIES:
1. As a site admin I can provide a clear idea of what the website is about so that users know what to expect from it.(Create a Landing Page #15)

4.EPIC: Enable registered users to CRUD their own trips.

- USER STORIES:

1. As a registered user I can CRUD my own trips so that I can manage my own content.(Create Post #17)

5.EPIC: Create a trips list to provide content to users.

- USER STORIES:

1. As a user I can view a list of articles so that I can select the contents I like and see what the site’s purpose is.(View Pagination #19)

6.EPIC: Enable registered users to interact with trips posts to enhance UX.

- USER STORIES:

1. As a registered user I can like/unlike posts so that I can engage with the site content.(Like/Unlike Post #23)

2. As a registered user I can comment a post so that I can engage with the community and be involved.(Comment Post#21)

3. As a registered user I can add a picture to my post so that I can create a more visually interesting content.(Image Uploading#25)

**Strategy**

For the development of the website the Agile methodology was taken using GitHub functions which are issues, milestones, iterations and Kanban board.

1.Milestones were used to create Epics with a custom template.
2.Issues were used to create User Stories with a custom template. Eash user story has been mapped out using the Kanban board format. Each one has acceptance criteria and tasks.
Each user story was linked to an Epic.

**Structure**

The user will first see the Home Page where the purpose of the website is made clear with a brief introduction. Users can also see a list of 6 posts.

Both registered and unregistered users can read the posts, but only registered users can interact with them by leaving a comment or liking the post itself.
Post detail page contains details of the post, comments and number of likes.

The "Add a trip" page is accessible only for registered users. This page can be accessed by clicking the 'Add a trip' button in the navigation bar which is only visible for a registered user. After creating the post, Admin user must approve it before the post is displays on the site. Users are able to edit or delete their own posts by clinking the Edit/Delete button located underneath the post. These buttons are only visible to the owner of the post.

**WIREFRAMES**
- - -

**Home Page: Desktop - Not logged in view**

![Alternate text](/static/images/Home%20-%20Desktop%20-%201.png)

**Second Page: Desktop - Not logged in view**

![Alternate text](/static/images/Second%20page%20-%20Desktop.png)

**Home Page: Desktop - Logged in view**

![Alternate text](/static/images/Home-Desktop%20-%202.png)

**Post Page: Desktop - Not logged in view**

![Alternate text](/static/images/Article%20Page%20-%20Desktop%20-%201.png)

**Post Page: Desktop - Logged in view**

![Alternate text](/static/images/Article%20Page%20-%20Desktop%20-%202.png)

**Add Trip Form: Desktop**

![Alternate text](/static/images/Add%20trip%20form.png)

**Home Page: Mobile**

![Alternate text](/static/images/Home%20-%20Mobile.png)


**FEATURES**
- - -

 - Navigation menu
 
 The navigation menu is clear and consistent throughout the site to provide the users an easy navigation. Links to Home, Add a trip, Register and Sign In/Out are available. If the user is not signed in the Sign in and Register links are visible in the navbar. If the user is signed in the Sign In and Register links are replaced by a Log Out link and the Add a trip link is visible. While the Logo will be always displayed in any screen, the other links that the user can find in the bar, will switch to hamburger on tablets and mobiles.

 ![Alternate text](/static/images/navbar.png)

 - Footer

 At the bottom of the page we can find the footer with the links to direct the user to the Facebook, Instagram and Twitter pages.
 
 ![Alternate text](/static/images/footer.png)

- Home Page

1.A hero image is displayed at the top of the page with overlay text welcoming the user to the website. Right below the users can also find a short description of the purpose of the page and what they will find on it.

![Alternate Text](/static/images/home_page.png)

 - Trips section
 
 Right below the brief description of the purpose of the page, the users will find a list of six posts per page(max.) to avoid loading time issues.

 ![Alternate text](/static/images/trips_section.png)

 - Add a trip form
 
 When the users are logged in, they can see on the navigation bar the option "Add a trip". Simply by clicking on it the form opens and the user can enter all the fields to add a post and create a new content which will be displayed on the website.

 ![Alternate text](/static/images/form.png)
 
 - Post Detail page
 
 Accessed by any user simply by clicking on the post itself. The not logged in users can also read the approved comments right below the post. If the user is logged in, instead, there is another function that allows to press the Like button and leave a comment regarding the post. The comments entered here need to be reviewed by the site owner before being displayed in this post detail page.

 ![Alternate text](/static/images/post_detail.png)

 ![Alternate text](/static/images/comments_section.png)

 - Edit Post page

 The Edit post page is accessed by edit post button which is available in the post detail page and it's visible for the user's own post only so that the post can only be edited by its own user or by superuser using the admin page. If the user confirms to edit the post, will be redirected to the Home Page and a message will show below the navbar to inform that the post was succesfully edited.

 ![Alternate text](/static/images/edit_delete.png)

  - Delete Post Page

 The owner of the post also have another button abailable, which is the Delete Post button. If the user clicks on it a Delete Post page displays and asks the user for confirmation to delete the post. Users can either click on "Yes, delete post!" or cancel and go back to the Home Page. 
 If the user confirms to delete the post, will be redirected to the Home Page and a message will show below the navbar to inform that the post was deleted.

 ![Alternate text](/static/images/edit_delete.png)

   - Register Page

This page can be opened from the register button in the navigation bar. New visitors are simply asked to enter username, password and password confirmation to register. Email field can be left blank as it is optional. Once successfully registered, users will be redirected to the Home Page and have access to all the features available for registered users.

 ![Alternate text](/static/images/signup.png)

- Sign In Page

The Sign In button can be accessed to login. Username and password will be required. On successful login, users will be redirected to the Home Page and a message to inform them that they logged in successfully will be displayed under the navigation bar.

 ![Alternate text](/static/images/signin.png)

- Sign Out Page

Once a user is logged in, the Sign In button in the navigation bar will be replaced with the Logout button. If they want to logout all they need to do is simply click this button and confirm to sign out. Once again, users will be redirected to the Home Page and a message to inform them that they logged out successfully will be displayed under the navigation bar.

 ![Alternate text](/static/images/signout.png)
 

**TECHNOLOGIES USED**
- - -

- HTML: HTML has been used to give structure and content to the website.
- CSS: In order to style the content created with HTML, and give responsiveness to the pages, the CSS language has been used.
- Java Script: JS was used with Bootstrap to provide interaction on the front-end.
- Python: It was used to code the back end of the project.
- Google Fonts: I used the Kanit and sans-serif font.
- Pixabay: I used this platform for all the images displayed around the website.
- Bootstrap: Bootstrap was used to style the website, add responsiveness and interactivity.
- Cloudinary: Cloudinary was used for hosting the images.
- Balsamiq Wireframes: I used it to produce low fidelity wireframes to organise the structure of the pages.
- Gitpod was used to develop the project.
- GitHub was used to host repository.
- Heroku was used to deploy the website.
- Django was used as the main python framework for the development of the project.
- Django AllAuth was used to provide user account management functionality.
- Google Chrome Dev Tools was used to check reponsiveness.


**TESTING**
- - - 

All the pages of the website have ben tested using the developer tools in Google Chrome. The code had to be changed along the process in order to achieve the responsiveness required for the project. The preview from Gitpod helped to constantly check all the changes made.

Testing was performed using a MacBook Air (M1, 2020) on macOS Monterey with the following browsers:
- Google Chrome 102.0.5005.61
- Safari 15.3
- Mozilla Firefox 101.0.1

After testing the website I can confirm the project it's responsive in its all pages and works properly on all standard screen sizes.

The forms are working in each section of the project.
- The users can add, edit and delete eir own posts.
- Comments can be added through the comment form. To be displayed need to be approved by the owner of the website.


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
The site was deployed via Heroku. These are the steps I followed:

- In the Heroku dashboard, click "New" and then "Create new app". After that enter the app name and specify the region.

- In the Heroku dashboard click on the Resources tab
Scroll down to Add-Ons, search for and select 'Heroku Postgres'.

- In the setting tab, click on Reveal Config Vars button then copy the value for DATABASE_URL key.

- In Gitpod create a new env.py file and import the os library. Heroku Config vars need to be set accordingly including DATABASE_URL and SECRET_KEY.

- In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
- Insert the line if os.path.isfile("env.py"): import env
- Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
- Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}
- In the Gitpod terminal, migrate the change by python3 manage.py migrate.
- Login to Cloudinary and copy the API Environment variable and paste in env.py and also Config Vars in Heroku.
- In Heroku config vars add DISABLE_COLLECTSTATIC with value of '1' (this must be removed for final deployment)
- Add Cloudinary libraries to installed apps section of settings.py as per follow:

- - Add 'cloudinary_storage', before 'django.contrib.staticfiles', and 'cloudinary' right after it.

- In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.

- Set TEMPLATES_DIR just below BASE_DIR and insert TEMPLATES_DIR in TEMPLATES array 'DIRS': []

- Set ALLOWED_HOSTS as 'traveldream.herokuapp.com', 'localhost'

- Create Procfile and add the code: web gunicorn traveldream.wsgi
- On GitHub add, commit and push the changed files.
- On Heroku click on the Deploy tab, connect to GitHub and search for the repository then Connect
- Click on Deploy Branch.
- Once the development process is complete, change the debug setting to: DEBUG = False in settings.py.
- Considering for this project the summernote editor was used in Heroku add: X_FRAME_OPTIONS = 'SAMEORIGIN' to settings.py.
- In Heroku settings config vars change the DISABLE_COLLECTSTATIC value to 0.
- Click on Deploy Branch. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser.

During my work to the project, I had to migrate my database from Heroku to ElephantSQL. Here are the stpes I've taken:

- Create and account with ElephantSQL.
- Create New Instance, specify the region, select a data center near my location, click review and click "Create Instance"
- In the ElephantSQL dashboard click on the database instance name for this project(traveldream).
- In the URL section copy the database URL.
- In the env.py file replace the DATABASE_URL variable with the the relevant string from ElephantSQ.
- Run the migration command in the terminal to migrate the database structure to the newly-connected ElephantSQL database.




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