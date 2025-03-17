# Anteskogs Game Reviews - Testing

![Anteskog's Game Reviews](media\media\images\mock-up1.png)




[Visit Anteskog's Game Reviews Here](https://anteskogs-game-reviews-c55343667d70.herokuapp.com/)

Testing was ongoing throughout the entire build. During development I made use of Googles Developer Tools to ensure everything was working as expected and to assist me with troubleshooting when things didn't work as they should.

I have gone through each page of the site using the Chrome Developer Tools to ensure each page is responsive on a variety of different screen sizes and devices, as well as manually testing this using a variety of devices in person.

---

## Validation Testing

### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home | Pass | [Home](media\media\images\testing-img\w3c\vw3-one.png) |
| Reviews | Pass | [Reviews-list](media\media\images\testing-img\w3c\vw3-list.png) |
| About | Pass | [About](media\media\images\testing-img\w3c\vw3-about.png) |

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| CSS | Pass | [CSS](media\media\images\testing-img\w3c\css.png) |



### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python.

| File | Result | Evidence |
| :--- | :--- | :---: |
| ** Anteskog's Game Review** |
| game-reviews/settings.py | Pass | [settings.py validation](media\media\images\testing-img\pep8\pep8-settings.py.png) |
| game-reviews/Urls.py | Pass | [urls.py validation](media\media\images\testing-img\pep8\pep8-gv-urls.png) |
| **Reviews** |
| reviews/admin.py | Pass | [admin.py validation](media\media\images\testing-img\pep8\pep8-admin-reviews.png) |
| reviews/apps.py | Pass | [apps.py](media\media\images\testing-img\pep8\pep8-reviews-apps.png) |
| reviews/forms.py | Pass | [forms.py](media\media\images\testing-img\pep8\pep8-reviews-forms.png) |
| reviews/models.py | Pass | [models.py](media\media\images\testing-img\pep8\pep8-models-py-reviews.png) |
| reviews/urls.py | Pass | [urls.py](media\media\images\testing-img\pep8\pep8-reviews-urls.png) |
| reviews/views.py | Pass | [views.py](media\media\images\testing-img\pep8\pep8-views.py-reviews.png) |
| **About** |
| about/admin.py | Pass | [admin.py](media\media\images\testing-img\pep8\pep8-about-admin.png) |
| about/apps.py | Pass | [apps.py](media\media\images\testing-img\pep8\pep8-about-apps.png) |
| about/forms.py | Pass | [forms.py](media\media\images\testing-img\pep8\pep8-about-forms.png) |
| about/models.py | Pass | [models.py](media\media\images\testing-img\pep8\pep8-models-about.png) |
| about/urls.py | Pass | [urls.py](media\media\images\testing-img\pep8\pep8-about-urls.png) |
| about/views.py | Pass | [views.py](media\media\images\testing-img\pep8\pep8-about-views.png) |
| **User_Games** |
| user_games/apps.py | Pass | [apps.py](media\media\images\testing-img\pep8\pep8-user_games-apps.png) |
| user_games/forms.py | Pass | [forms.py](media\media\images\testing-img\pep8\pep8-user_games-forms.png) |
| user_games/models.py | Pass | [models.py](media\media\images\testing-img\pep8\pep8-user_games-models.png) |
| user_games/urls.py | Pass | [urls.py](media\media\images\testing-img\pep8\pep8-user_games-urls.png) |
| user_games/views.py | Pass | [views.py](media\media\images\testing-img\pep8\pep8-user_games-views.png) |


### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\home-desk.png) |
| Reviews Page | ![Reviews Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\reviews-desk.png) |
| Reviews-detail | ![Reviews-Detail desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\details-desk.png) |
| About Page | ![About Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\about-desk.png) |
| Upload Games Page | ![Upload Games Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\upload-desk.png) |
| Your Games Page | ![Your Games Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\your-games-desk.png) |
| Thank You Page | ![Thank You Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\thank-desk.png) |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\home-mobile.png) |
| Reviews Page | ![Reviews Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\reviews-mobile.png) |
| Reviews-detail | ![Reviews-Detail desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\detail-mobile.png) |
| About Page | ![About Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\about-mobile.png) |
| Upload Games Page | ![Upload Games Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\upload-mobile.png) |
| Your Games Page | ![Your Games Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\your-games-mobile.png) |
| Thank You Page | ![Thank You Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\thank-mobile.png) |



## Automated Testing



### Coverage Testing

| Coverage for | Total | Evidence |
| :---| :--- | :--- |

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I can | So that | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| Open a Review | User | Click on a review | I can read the full text. | After you navigate to the reviews page you will see the games lined up, if you click on the title you will see the content of that game. |[Navbar](media\media\images\testing-img\navbar.png), [Game-Detail](media\media\images\testing-img\game-detail.png) |
 | Account Registration | User | Register an account | I can leave a comment. | In the Game-Detail view at the bottom its a form you can fill out and submit to leave a comment. | [Comment Section](media\media\images\testing-img\leave-comment.png) |
 | Modify or delete comment on a review | User | Modify or Delete my comment | I can be involved in the conversation. | When you have submitted a comment you will be abel to see our comment and you can alter it or delete it. | [Edit or Delete](media\media\images\testing-img\delete-edit.png) |
 | CRUD Part One | User | Create, Read, Update and Delete my content | I can manage my own content | When the user is log in he/she can Create, Update and Delete all content that he/she is owner of. | [Create-Comment](media\media\images\testing-img\create-comment.png), [Confirmation-Edit-Comment](media\media\images\testing-img\confirmation-edit-comment.png), [Delete-comment](media\media\images\testing-img\delete-comment.png) |
 | CRUD Part Two | User | Create, Read, Update and Delete my content | I can manage my own content | When the user is log in he/she can Create, Update and Delete all content that he/she is owner of. | [Upload a Game](media\media\images\testing-img\create-game.png), [Confirmation-Upload](media\media\images\testing-img\confirmation-upload.png), 


### Full Testing

Full testing was performed on the following devices:
* Laptop:
    * Asus Tuf Gaming F15 15.6 inch screen.
* Mobile Devices:
    * Samsung galaxy 22 ultra.

Testing was also performed using the following browsers:

* Chrome

Additional testing was carried out by friends and family on a variety of devices and screens.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **NAVBAR** |
| The sites logo **Anteskog's** | Redirects you to home page | Clicked logo | Redirected to home page | Pass |
| Reviews | Takes you to the reviews page | Clicked Reviews | Taken to reviews page | Pass |
| About | Takes you to the about page | Clicked About | Taken to about page | Pass |
| Register | Takes you to register form | Clicked register | Taken to register form | Pass |
| Login | Takes you to login form | Clicked login | Taken to login form | Pass |
| **If Logged in** |
| Upload a Game | Takes you to upload games form | Clicked upload a game | Taken to upload a games form | Pass |
| **Home Page** |
| Explore Reviews Button | Takes you to reviews page | Clicked explore reviews | Taken to reviews page | Pass |
| Upload a Game Button | Takes you to upload games form | Clicked upload a game | Taken to upload a games form | Pass |
| About Button | Takes you to the about page | Clicked About | Taken to about page | Pass |
| **Reviews Page** |
| Six's Post is shown with clickable title | When you click a title you goes to game-detail page | Clicked title | Taken to a game-detail view | Pass |
| | Test to click all titles so all work as they should | Click all titles | all worked | Pass |
| **Game-detail view** |
| If scrolled down you will see a comment form, if filled out you will se a message thats tells you it worked and a box with your comment shows up with two buttons | Filled out form and click "Submit comment" | a text comes up with text "Comment submitted and awaiting approval | Pass |
| Comments button edit | If clicked you will be taken to a page with a form with your comment and you will be able to edit it | Click edit | A form with my texts appear and i can edit | Pass |
| Delete comment button 1 | If clicked a popup box will appear with text "Delete Comment - Are your sure you want to delete this comment? and two buttons 'CANCEL and DELETE' i click Cancel and go back to current page | Click cancel | The box disappear | Pass |
| Delete comment button 2 | If clicked a popup box will appear with text "Delete Comment - Are your sure you want to delete this comment? and two buttons 'CANCEL and DELETE' i click Delete and a text with text " Comment successfully Deleted" will show | Click delete | The comment has been deleted and a text is shown | Pass |
| If **Owner** of the game  you will see two buttons Delete and Edit  | If you click edit you goes to upload a game form there you can now edit your game | Click "Edit" | Taken to upload a game | Pass |
| **Owner** Delete button 1 | If clicked a popup box will appear with text "Delete Game - Are your sure you want to delete this game? and two buttons 'CANCEL and DELETE' i click Cancel and go back to current page | Click cancel | The box disappear | Pass |
| **Owner** Delete button 2 | If clicked a popup box will appear with text "Delete game - Are your sure you want to delete this game? and two buttons 'CANCEL and DELETE' i click Delete and a text with text " Game successfully Deleted" will show | Click delete | The game has been deleted and a text is shown | Pass |
| **About Page** |
| Ask questions form | Fill out the form and you will be redirected to the thanks page | Filled out the form and press submit button | Was taken to a thank you page | Pass |
| **Upload a Game** | Shows a form to fill out with Title, Image, Content, Status and Excerpt | If correct a game will load up on the site | filled out the form | A new game shows on the site | Pass |
| **Your Games** **(If logged in)** |
| A page with your games will show | if new to the site you don't have any games, it shows a text and button with text 'upload a Game' | I click the button | Taken to upload a game form | Pass |
| All titles a clickable | Click on all titles to know they are working | Click all titles | All worked as expected | Pass |



## Bugs

### Solved Bugs

| No | Bug | How I solved the issue | Evidence |
|:--- | :--- | :--- | :---: |
| 1 | crispy_forms_tags is not a registered tag library | Added crispy_forms and crispy_bootstrap5 to INSTALLED_APPS in settings.py and configured CRISPY_TEMPLATE_PACK |
| 2 | Background image not displaying | Corrected the file path in CSS to use forward slashes and ensured the image is in the correct directory |
| 3 | URL namespace 'user_games' isn't unique | Ensured the namespace for user_games is unique across the project |
| 4 | Comments not showing pending approval status | Updated the view and template to include pending comments and their count |

### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |
| 1 | Pagination may yield inconsistent results with an unordered object_list |