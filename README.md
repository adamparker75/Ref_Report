<div align="center">

# _**Ref Report**_

</div> 

<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_main_image.jpg">
</p>


## _**About**_


This application was designed as a tool for use by Amateur referees. My son is keen to become a referee, 
and we found that other than writing the details in a notebook which are prone to being lost or misplaced,
there was nothing else of use to him to keep a record of the match details. I wanted to design a tool to help
him and other referrees to make a record of the game they have just taken charge of as soon as they get back
to the dressing room. <br>
Users are able to register a new account, login to their account where they can submit a new report, view all 
existing reports and also edit and delete reports as necessary. <br>

The deployed website can be viewed here - [Ref Report](https://adamp-ref-report.herokuapp.com/)


## _**UX**_ 

The application was designed to be easy and straight forward to use. I created a simple homepage with a small
amount of information about the application, and also a link for new users to register an account. <br>
The application is easy to navigate by either using the menu links in the header, or using the side navigation bar on smaller
devices. <br>
I designed the application to have a consistent look to each page, the forms are the same throughout whether logging in or 
submitting a report, and each page has a familiar feel to it.

### _**Target Audience**_ 

The application is aimed at but not restricted to the following users :

* Young amateur referees.
* Senior amateur referees.
* Referee assessors.
* Football coaches who wish to keep a record of their matches.
* Football fans to keep a track of their favourite team.

### _**User Stories**_

As a referee, I want to register for an account, so that I can begin to submit my match reports.

As a referee, I want to login to my account, so that I can view and submit reports.

As a referee, I want to submit a report on a match I have just referee'd, so that I can store the details as they are fresh 
in my mind.

As a referee, I want to view my previous submitted reports, so they can help me submit the match details to the league.

As a referee, I want to edit my reports, so I can change any details that may be incorrect.

As a referee, I want to delete my reports, so I can only keep the reports that haven't been submitted to the league.

As an administrator, I want to view all users reports, so I can moderate what has been submitted.

As a football coach, I want to store match reports of the team I coach, so I can keep a track of the team throughout the season.

As a football fan, I want a place to keep a record of my favourite team, so I can look back at how they have played over the season.

As a user, I want to be notified if my login information is incorrect, so I can input the correct details and log in to my account.

## _**Wireframes**_

### _**Home Page**_
<br>
<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_homepage.png">
</p>
<br>

### _**Registration Page**_
<br>
<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_register.png">
</p>
<br>

### _**Login Page**_
<br>
<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_login.png">
</p>
<br>

### _**Reports Page**_
<br>
<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_reports.png">
</p>
<br>

### _**Submit Report Page**_
<br>
<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_submit.png">
</p>
<br>

### _**Tablet View**_
<br>
<p align="center">
  <img width="400" height="600" src="static/files/ref_report_wireframe_tablet.png">
</p>
<br>

### _**Smartphone View**_
<br>
<p align="center">
  <img width="260" height="600" src="static/files/ref_report_wireframe_mobile.png">
</p>
<br>

## _**Features**_

* **Navigation Bar** - The navigation bar is consistent across the site, it uses [Materialize CSS](https://materializecss.com/) to make it beahave responsively 
on smaller devices.

* **Side Navigation Bar** - When viewed on smaller devices the links in the navigation bar, appear from the left when the 
hamburger menu is pressed.

* **Modal Pop Up** - The links to the log in and registration page utilise a modal pop up when viewed on smaller devices.

* **Collapsible Accordion** - The reports page utilises a collapsible from [Materialize CSS](https://materializecss.com/) when viewing the reports.

* **Submit Report** - Allows users to submit a match report to the database.

* **View Report** - Users can view a list of their reports and expand them to diaplay all of the details.

* **Edit / Delete Buttons** - Users have the option to edit or delete any of their reports.

### _**Features left to implement**_



## _**Technologies Used**_

[HTML](https://en.wikipedia.org/wiki/HTML5) - Provides the content and structure of the templates.

[CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used to provide some of the styling.

[Materialize CSS](https://materializecss.com/) - Used to create a number of the html elements such as the forms, the collapsible and the pop up modal. It was also used to make the application responsive. 

[Python](https://www.python.org/) - Used to code the flask application.

[Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework used to create the application.

[Werkzeug Security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) - Used for the users password security.

[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Used as a templating language with flask and python

[MongoDB](https://www.mongodb.com/) - Used to create the databases and store the users data.

[jQuery](https://jquery.com/) - Used with Materialize CSS to enable the collapsible accordion, and modal pop up.

[Google Fonts](https://fonts.google.com/) - The application utilises the Lato font.

[Font Awesome](https://fontawesome.com/) - Used for the icons throughout the application.

[Git](www.github.com) - Used for version control, and tracking changes in the repository.

[Heroku](https://www.heroku.com/) - The platform used to deploy the application.

## _**Testing**_

A lot of the testing was carried out using the developer tools in Google Chrome, I did this so that I could test whilst I was devloping the application
and make changes as I went along. It also helped me test the application on smaller devices and to ensure it was responsive. 
I also used tools such as [W3C Markup Validation Service](https://validator.w3.org/) to ensure my code was correct and had no errors.

### _**User Story Tests**_

**1. Register for an account**

i.   Open the application. <br>
ii.  Does the home page appear? <br>
iii. Are the menu links visible in the navigation bar? <br>
iv.  Click on the **register** menu link. <br>
v.   Does the register an account page open? <br>
vi.  Click the register button, does the required field message appear? <br>
vii. Fill out the fields correctly and click register. <br>
vii. Do you go to the home page and a flashed message appears saying you have successfully registered? <br>
ix.  Click log out then click the register link again. Click on the link to the login page underneath the form. Do you go to the login page? <br>
x. Fill out the form with a username that already exists. Does a flashed message appear advising the username is taken?

**1a. Register for an account on mobile device**

i.   Click on the hamburger menu link. Does the side navigation bar appear?<br>
ii.  Click the register link, does a pop up modal form appear? <br>
iii. Follow steps 6-9 above. <br>

**All tests performed and no errors found.**

**2. Log in to your account**

i.   Click the login link in the navigation bar. Does the login page appear? <br>
ii.  Click the login button, does the required field message appear? <br>
iii. Fill out the fields correctly and click log in. <br>
iv.  Does the My reports page open? <br>
v.   Click log out and fill an incorrect username in, does a flashed message appear saying the username or password is incorrect? <br>
vi.  Click log out and fill an incorrect password in, does a flashed message appear saying the username or password is incorrect? <br>
vii. CLick the Register account link underneath the form, does this take you to the register page?

**2a Log in to your account on a smaller device**

i.   Click on the hamburger menu link. Does the side navigation bar appear?<br>
ii.  Click the log in link, does a pop up modal form appear? <br>
iii. Follow steps 2-7 above. <br>

**All tests performed and no errors found.**