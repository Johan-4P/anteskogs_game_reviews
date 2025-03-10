# Anteskogs Game Reviews

![Anteskog's Game Reviews](media\media\images\mock-up1.png)


Anteskog's Game Reviews is a full-stack website build using Django, Python, CSS. 

This was created as my third milestone project.

[Visit Anteskog's Game Reviews Here](https://anteskogs-game-reviews-c55343667d70.herokuapp.com/)



# CONTENTS

* [User Experience](#user-experience)
    * [Strategy Plane](#strategy-plane)
        * [Project Goals](#project-goals)
    * [Scope Plane](#scope-plane)
    * [Feature Planning](#feature-planning)
    * [Structure plane](#structure-plane)
        * [User Stories](#user-stories)
        * [Database Schema](#database-schema)
    * [Skeleton Plane](#skeleton-plane)
        * [Wireframes](#wireframes)
    * [Surface Plane](#surface-plane)
        * [Colour Scheme](#colour-scheme)
        * [Typography](#typography)
        * [Images](#images)
        * [Base Mockup](#base-mockup)
    *[Features](#features)
        * [General Features of the site](#general-features-of-of-the-site)
        * [Sites header and footer images](#sites-header-and-footer-images)
        * [Defensive Programming](#defensive-programming)
        * [Features for the next level](#features-for-next-version)
        * [Home Page](#home-page)
        * [Reviews Page](#reviews-page)
        * [About Page](#about-page)
        * [Admin Page for managing the site](#admin-page-for-managing-the-site)
        * [Signup Page](#signup-page)
        * [Log in page](#log-in-page)
        * [Log out page](#log-in-page)
    * [Future Implementations](#future-implementations)
    * [Accessibility](#accessibility)
    * [Technologies Used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Databas Used](#database-used)
    * [Frameworks Used](#frameworks-used)
    * [Libraries & Packages Used](#libraries--packages-used)
    * [Program Used](#program-used)
    * [Deployment & Local Development](#deployment--local-development)
        * [Heroku app setup](#heroku-app-setup)
        * [Preparation for deployment in VSCode](#preparation-for-deployment-in-vscode)
    * [Testing](#testing)
    * [Credits](#credits)
        * [Code used](#code-used)
        * [Content](#content)
        * [Media](#media)
        * [Acknowledgments](#acknowledgments)




---

## User Experience

### Strategy Plane

#### **Project Goals**

Anteskog's Game Reviews is a Review / Blog.

The sites primary audience will be people who love gaming, it will work as a community. You are abel to upload, comment and edit all of your work you put in there!.


### Scope Plane

#### **Feature Planning**

### Structure Plane

#### **User Stories**

| User Story ID | As a/an | I can | So that i can... |
| :--- | :--- | :--- | :---|
| 1 | User | click on a review | Read the full text |
| 2 | User/Admin | View comments on a individual post | Read the conversation |
| 3 | User | Register an account | Comment on a review |
| 4 | User | Leave comments on a review | Share my opinion |
| 5 | User | Modify or delete my comment | Be involved in the conversation |
| 6 | Admin | Create, Read, Update and Delete | Manage my blog content |
| 7 | Admin | Approve or disapprove comments | Filter out bad comments |



#### **Database Schema**

![Database Schema](media\media\images\erd.png)




### Skeleton Plane

#### **Wireframes**

Wireframes for the project were created using [Balsamiq](https://balsamiq.com/)

* Home Page

![Home page wireframe](media\media\images\wireframes1.png)

* Review Detail Page

![Review Detail Page](media\media\images\wireframes2.png)

* About

![About](media\media\images\wireframes3.png)


### Surface Plane

#### **Colour Scheme**

I didn't know what color i should use so i did use Google and stumble over this site https://coolors.co/ and come upp with this :

![Color](media\media\images\color.png)

#### **Typography**

All fonts were sourced from [Google Fonts](https://fonts.google.com/).
I have used [Lato](https://fonts.google.com/specimen/Lato)  and [Roboto](https://fonts.google.com/specimen/Roboto?query=Roboto) 

#### **Imagery**

All images have been found on [Wikipedia](https://www.wikipedia.org/)

## Features

### General Features of of the site

Each page of the site shares the following:

* Navbar - The navbar is the same through the site.
The Navbar with the name Anteskog' is function as a link to home page, and then 4 links when not logged in and 5 links if you are logged in.

* Footer - The footer is the same through the site.
### **Before Sign in**
#### **Home Page**

The home page of the site features a welcoming message, a picture and a list of features to explore. After that you will find four buttons that are linked to four different places Reviews, Login, Sign up and send a question (About Page).
When you are signed in and ready to go the buttons will change to the following: Explore Reviews, Logout, Upload a Game and Send a question (About Page).

#### **Review Page**
The Review Page is the *Big* page it is here all the games are gathered 6's Post's in each page.
All posts have a image and a header text that are clickable.
All have a little box bellow with example text, date, time and comments count are visible.


#### **About Page**
The About Page is a page about me. A picture of me is shown and the text about me with information, and bellow it is a form you can fill in if you want to send me a question with a Submit button.
When you have **Submit** you will go to the Thank you page.

#### **Review-Detail Page - Not Sign In**
A big header with the name of the game and a picture of the game.
Text about the game and maybe images of in game, after that the comments section begins.
If not logged in you only can read the comments but not comment on the game.

#### **Sign Up Page**
Sign up page have a welcome text and a form to fill out.

#### **Sign In Page**
Welcome text and link to Sign Up if you haven't done so.
Form for log in.

## **After Sign In**
These links are the same : **Reviews**, **About**
#### **Review-Detail Page**
I Refer to [Review-Detail Page - Not Sign In](#Review-Detail-Page--NotSign-In)
**But** After the text you will now be abel to Comment on the game and edit and delete your comment.
Are you the owner of the game it will show up an edit and delete button for the game as well.


#### **Upload a Game Page**
Is a form with Title, Upload of a image, Field of content, dropdown with Draft or Publish and a Excerpt field

#### **Your Games Page** 
Here will all your Game show up and you can click them and Edit / Delete them.


#### **Logout Page**
A simple Logout page with a question : Are you sure you want to sign out?


#### Defensive programming

#### Features for next version


### Features for the next level
### Home Page
### Reviews Page
### About Page
### Admin Page for managing the site
### Signup Page
### Log in page
### Log out page
### Future Implementations
### Accessibility
### Technologies Used
#### Languages Used
HTML, CSS, Python
#### Databas Used
[PostgreSQL](https://www.postgresql.org/) - Database.

[Heroku](https://www.heroku.com/) - Deployed site.
#### Frameworks Used
[Django](https://www.djangoproject.com/) - Version 5.1.6 - A high-level Python web framework that encourages rapid development and clean, pragmatic design.

[Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Version 5.0.1 - A framework for building responsive, mobile-first sites.
#### Libraries & Packages Used

[Django Allauth](https://django-allauth.readthedocs.io/en/latest/) - Version 65.4.1 - Used for authentication, registration & account management.

[Django Clouinary Storage](https://pypi.org/project/cloudinary/) - Version 0.3.0 - Used for Storage of pictures.

[django_crispy_forms](https://pypi.org/project/django-crispy-forms/) - Version 2.3 - provides a tag and filter that lets you quickly render forms

[gunicorn](https://pypi.org/project/gunicorn/) - Version 23.0.0 - a Python WSGI HTTP Server

[pillow](https://pypi.org/project/pillow/) - Version 11.1.0 - Python imaging library

[dj_databsae_url](https://pypi.org/project/dj-database-url/) - Version 2.3.0 - allows us to utilise the DATABASE_URL variable.

[Whitenoise](https://pypi.org/project/whitenoise/) - Version 6.9.0 - Radically simplified static file serving for Python web apps.


### Program Used

[Am I Responsive](https://ui.dev/amiresponsive) - To create the responsive images of the site on a variety of device sizes.

[Balsamiq](https://balsamiq.com/) - Used to create wireframes.

[Lucid Chart](https://www.lucidchart.com/) - Used to create the database schema

[Favicon.io](https://favicon.io/) - To create the favicon.

[Git](https://git-scm.com/) - For version control.

[GitHub](https://github.com/) - To save and store the files for this project.

[Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.

[Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

### Deployment

The project is deployed using Heroku. To deploy the project:

#### **Create the Live Database**

Got my database by email from Code institute

#### **Heroku app setup**

  1. From the [Heroku dashboard](https://dashboard.heroku.com/), click the new button in the top right corner and select create new app.
  2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
  3. Open the settings tab and create a new config var of `DATABASE_URL` and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

#### **Preparation for deployment in GitPod**

1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):

   ```bash
   pip3 install dj_database_url==0.5.0 psycopg2
   ```

2. Update your requirements.txt file with the packages just installed:

    ```bash
    pip3 freeze > requirements.txt
    ```

3. In settings.py underneath import os, add `import dj_database_url`

4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:

    (NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)

    ```python
    DATABASES = {
        'default': dj_database_url.parse('paste-elephantsql-db-url-here')
    }
    ```

5. In the terminal, run the show migrations command to confirm connection to the external database:

    ```bash
    python3 manage.py runserver
    ```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:

    ```bash
    python3 manage.py migrate
    ```

7. Create a superuser for the new database. Input a username, email and password when directed.

    ```bash
    python3 manage.py createsuperuser
    ```


8. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:

    ```bash
    pip3 install gunicorn
    pip3 freeze > requirements.txt
    ```

9. Create a `Procfile` in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):

    ```Procfile
    web: gunicorn seaside_sewing.wsgi:application
    ```

10. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:

    ```bash
    heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
    ```

11. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:

    ```python
    ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
    ```

12. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:

    ```bash
    heroku git:remote -a {app name here}
    git push heroku master
    ```

13. You should now be able to see the deployed site (without any static files as we haven't set these up yet).

14. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.

#### **Generate a SECRET KEY & Updating Debug**

1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.
2. [Django Secret Key Generator](https://djecrety.ir/) is an example of a site we could use to create our secret key. Create a new key and copy the value.
3. In Heroku settings create a new config var with a key of `SECRET_KEY`. The value will be the secret key we just created. Click add.
4. In settings.py we can now update the `SECRET_KEY` variable, asking it to get the secret key from the environment, or use an empty string in development:

    ```python
    SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
    ```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:

    ```python
    DEBUG = 'DEVELOPMENT' in os.environ
    ```

6. Save, add, commit and push these changes.

### Local Development

#### **How to Fork**

To fork the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [Anteskog's Game Reviews](https://github.com/Johan-4P/anteskogs_game_reviews).

3. Click on the fork button in the top right of the page.

#### **How to Clone**

To clone the repository:

1. Log in (or sign up) to GitHub.

2. Go to the repository for this project, [Anteskog's Game Reviews](https://github.com/Johan-4P/anteskogs_game_reviews).

3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.

4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.

5. Type the following command into the terminal `git clone` followed by the link you copied in step 3.

6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).

7. Install the packages from the requirements.txt file by running the following command in the terminal:

```bash
pip3 install -r requirements.txt
```

---

#### Preparation for deployment in VSCode

## **Testing**
Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

## **Credits**


### Code used
This project was created using methods taught in the Code Institutes **I Think Therefor I Blog**

### Content
Content on the site was mostly taken from [wikipedia](https://www.wikipedia.org/)

### Media
Content on the site was mostly taken from [wikipedia](https://www.wikipedia.org/)

and

[pinterest](https://pinterest.com/)

### Acknowledgments

* Jubril Akolade - My Code Institute Mentor.
* The Code Institute Slack - My Tutor Kay_ci