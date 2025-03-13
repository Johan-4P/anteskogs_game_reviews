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
| ** Reviews ** |
| reviews/admin.py | Pass | [admin.py validation](media\media\images\testing-img\pep8\pep8-admin-reviews.png) |
| reviews/apps.py | Pass | [apps.py](media\media\images\testing-img\pep8\pep8-reviews-apps.png) |
| reviews/forms.py | Pass | [forms.py](media\media\images\testing-img\pep8\pep8-reviews-forms.png) |
| reviews/models.py | Pass | [models.py](media\media\images\testing-img\pep8\pep8-models-py-reviews.png) |
| reviews/urls.py | Pass | [urls.py](media\media\images\testing-img\pep8\pep8-reviews-urls.png) |
| reviews/views.py | Pass | [views.py](media\media\images\testing-img\pep8\pep8-views.py-reviews.png) |
| ** About ** |
| about/admin.py | Pass | [admin.py](media\media\images\testing-img\pep8\pep8-about-admin.png) |
| about/apps.py | Pass | [apps.py](media\media\images\testing-img\pep8\pep8-about-apps.png) |
| about/forms.py | Pass | [forms.py](media\media\images\testing-img\pep8\pep8-about-forms.png) |


### Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

| Page | Result |
| :--- | :--- |


#### Mobile Results

| Page | Result |
| :--- | :--- |




## Automated Testing



### Coverage Testing

| Coverage for | Total | Evidence |
| :---| :--- | :--- |

## Manual Testing

### Testing User Stories

| User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |


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