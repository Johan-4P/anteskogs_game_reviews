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
| Register | 

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
| Home Page | ![Home Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-home-desktop.png) |
| Reviews Page | ![Reviews Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-reviews-desktop.png) |
| About Page | ![About Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-about-desktop.png) |
| Upload Games Page | ![Upload Games Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-upload-game-desktop.png) |
| Your Games Page | ![Your Games Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-your_games-desktop.png) |
| Thank You Page | ![Thank You Desktop Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-thank-desktop.png) |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-home-mobile.png) |
| Reviews Page | ![Reviews Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-reviews-mobile.png) |
| About Page | ![About Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-about-mobil.png) |
| Upload Games Page | ![Upload Games Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-upload-mobile.png) |
| Your Games Page | ![Your Games Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-your-mobile.png) |
| Thank You Page | ![Thank You Mobile Lighthouse Testing](media\media\images\testing-img\lighthouse\lgh-thank-mobile.png) |



## Automated Testing



### Coverage Testing

| Coverage for | Total | Evidence |
| :---| :--- | :--- |

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I can | So that | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| Open a Review | User | Click on a review | I can read the full text. | After you navigate to the reviews page you will see the games lined up,
 if you click on the title you will see the content of that game. |[Navbar](media\media\images\testing-img\navbar.png), [Game-Detail](media\media\images\testing-img\game-detail.png) |
 | Account Registration | User | Register an account | I can leave a comment. | In the Game-Detail view at the bottom its a form you can fill out and submit to leave a comment. | [Comment Section](media\media\images\testing-img\leave-comment.png) |
 | Modify or delete comment on a review | User | Modify or Delete my comment | I can be involved in the conversation. | When you have submitted a comment you will be abel to see our comment and you can alter it or delete it. | [Edit or Delete](media\media\images\testing-img\delete-edit.png) |
 | CRUD Part One | User | Create, Read, Update and Delete my content | I can manage my own content | When the user is log in he/she can Create, Update and Delete all content that he/she is owner of. | [Create-Comment](media\media\images\testing-img\create-comment.png), [Confirmation-Edit-Comment](media\media\images\testing-img\confirmation-edit-comment.png), [Delete-comment](media\media\images\testing-img\delete-comment.png) |
 | CRUD Part Two | User | Create, Read, Update and Delete my content | I can manage my own content | When the user is log in he/she can Create, Update and Delete all content that he/she is owner of. | [Upload a Game](media\media\images\testing-img\create-game.png), [Confirmation-Upload](media\media\images\testing-img\confirmation-upload.png), 


### Full Testing

Full testing was performed on the following devices:


Testing was also performed using the following browsers:

* Chrome

Additional testing was carried out by friends and family on a variety of devices and screens.

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| :--- | :--- | :--- | :--- | :--- |
| **NAVBAR** |


## Bugs

### Solved Bugs

| No | Bug | How I solved the issue | Evidence |
|:--- | :--- | :--- | :---: |


### Known Bugs

| No | Bug | Evidence |
|:--- | :--- | :---: |