<div align="center">

# _**Ref Report**_

</div> 

<p align="center">
    <img width="600" height="400" src="static/files/ref_report_wireframe_main_image.jpg">
</p>


## _**About**_


This website was designed as a tool for use by Amateur referees. My son is keen to become a referee, 
and we found that other than writing the details in a notebook which are prone to being lost or misplaced,
there was nothing else of use to him to keep a record of the match details. I wanted to design a tool to help
him and other referrees to make a record of the game they have just taken charge of as soon as they get back
to the dressing room. <br>
Users are able to register a new account, login to their account where they can submit a new report, view all 
existing reports and also edit and delete reports as necessary. <br>

The deployed website can be viewed here - [Ref Report](https://adamp-ref-report.herokuapp.com/)


## _**UX**_ 

The site was designed to be easy and straight forward to use. I created a simple homepage with a small
amount of information about how the site works, and also a link for new users to register an account. <br>
The website is easy to navigate by either using the menu links in the header, or using the side navigation bar on smaller
devices. <br>
I designed the site to have a consistent look to each page, the forms are the same throughout whether logging in or 
submitting a report, and each page has a familiar feel to it.

### _**Target Audience**_ 

The website is aimed at but not restricted to the following users :

* Young amateur referees.
* Senior amateur referees.
* Referee assessors.
* Football coaches who wish to keep a record of their matches.
* Football fans to keep a track of their favourite team.

### _**User Stories**_

1. As a referee, I want to register for an account, so that I can begin to submit my match reports.

2. As a referee, I want to login to my account, so that I can view and submit reports.

3. As a referee, I want to submit a report on a match I have just referee'd, so that I can store the details as they are fresh 
in my mind.

4. As a referee, I want to view my previous submitted reports, so they can help me submit the match details to the league.

5. As a referee, I want to edit my reports, so I can change any details that may be incorrect.

6. As a referee, I want to delete my reports, so I can only keep the reports that haven't been submitted to the league.

7. As an administrator, I want to view all users reports, so I can moderate what has been submitted.

8. As a football coach, I want to store match reports of the team I coach, so I can keep a track of the team throughout the season.

9. As a football fan, I want a place to keep a record of my favourite team, so I can look back at how they have played over the season.

10. As a user, I want to be notified if my login information is incorrect, so I can input the correct details and log in to my account.

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

[Materialize CSS](https://materializecss.com/) - Used to create a number of the html elements such as the forms, the collapsible and the pop up modal. It was also used to make the website responsive. 

[Python](https://www.python.org/) - Used to code the flask application.

[Flask](https://flask.palletsprojects.com/en/1.1.x/) - A micro web framework used to create the application.

[Werkzeug Security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/) - Used for the users password security.

[Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Used as a templating language with flask and python

[MongoDB](https://www.mongodb.com/) - Used to create the databases and store the users data.

[jQuery](https://jquery.com/) - Used with Materialize CSS to enable the collapsible accordion, and modal pop up.

[Google Fonts](https://fonts.google.com/) - The website utilises the Lato font.

[Font Awesome](https://fontawesome.com/) - Used for the icons throughout the website.

[Git](www.github.com) - Used for version control, and tracking changes in the repository.

[Heroku](https://www.heroku.com/) - The platform used to deploy the website.

## _**Testing**_

A lot of the testing was carried out using the developer tools in Google Chrome, I did this so that I could test whilst I was devloping the website
and make changes as I went along. It also helped me test the website on smaller devices and to ensure it was responsive. 
I also used tools such as [W3C Markup Validation Service](https://validator.w3.org/) to ensure my code was correct and had no errors.

### _**User Story Tests**_

**User Story 1. Register for an account**

i.   Open the website. <br>
ii.  Does the home page appear? <br>
iii. Are the menu links visible in the navigation bar? <br>
iv.  Click on the **register** menu link. <br>
v.   Does the register an account page open? <br>
vi.  Click the register button, does the required field message appear? <br>
vii. Fill out the fields correctly and click register. <br>
viii. Do you go to the home page and a flashed message appears saying you have successfully registered? <br>
ix. Click log out then click the register link again. Click on the link to the login page underneath the form. Do you go to the login page? <br>
x. Fill out the form with a username that already exists. Does a flashed message appear advising the username is taken?

**User Story 1a. Register for an account on mobile device**

i.   Click on the hamburger menu link. Does the side navigation bar appear?<br>
ii.  Click the register link, does a pop up modal form appear? <br>
iii. Follow steps 6-10 above. <br>

**All tests performed and no errors found.**

**User Stories 2 & 10. Log in to your account**

i.   Click the **log in** link in the navigation bar. Does the login page appear? <br>
ii.  Click the log in button, does the required field message appear? <br>
iii. Fill out the fields correctly and click log in. <br>
iv.  Does the My reports page open? <br>
v.   Click log out and fill an incorrect username in, does a flashed message appear saying the username or password is incorrect? <br>
vi.  Click log out and fill an incorrect password in, does a flashed message appear saying the username or password is incorrect? <br>
vii. CLick the Register account link underneath the form, does this take you to the register page?

**User Story 2a Log in to your account on a smaller device**

i.   Click on the hamburger menu link. Does the side navigation bar appear?<br>
ii.  Click the log in link, does a pop up modal form appear? <br>
iii. Follow steps 2-7 above. <br>

**All tests performed and no errors found.**

**User Story 3. Submit a report**

i.   When logged in, click the **Submit Report** link in the navigation bar. Does the submit report page open? <br>
ii.  Click the submit report button, does the required field message appear? <br>
iii. Fill in all the text fields on the form. <br>
iv.  Click on the date field, does a date selector appear? Once the date is chosen does the correct date appear in the field? <br>
v.   Click the Match Type field, do 4 options appear? Once selected does the correct option appear in that field? <br>
vi.  Once all fields are populated, click the submit report button. Dores a flashed message appear saying report added succesfully? <br>
vii. Have you been redirected to the My reports page? Check to see if the report is added to the bottom of the reports section. <br>

**All tests performed and no errors found.**

**User Story 4. View Reports**

i.   Log in to a registered account. <br>
ii.  Are you directed to the My Reports page once logged in? <br>
iii. Does a list of reports appear? <br>
iv.  Click on a report, does the report expand to show more information?<br>
v.   Is the report clear and legible? <br>
vi.  Click on the report header, does the report collapse? <br>
vii. Click on another report, are the details different to the previous report? <br>
viii. Type a relevant word in the search field and click search, do any reports appear? <br>
ix.  Click reset, do all reports appear? <br>

**All tests performed and no errors found.**

**User Story 5. Edit a report**

i.   Log in to a registered account. <br> 
ii.  Are you directed to the My Reports page once logged in? <br>
iii. Does a list of reports appear? <br>
iv.  Click on a report, does the report expand to show more information?<br>
v.   Does the edit report button appear at the bottom of the report? <br>
vi.  Click the edit report button page, does the edit report page appear with the fields already filled? <br>
vii. Make changes to the report. And click edit report.<br>
viii. Are you directed back to the My reports page? <br>
ix.  Check the report to ensure the changes have been saved. <br>
x.   Click edit on another report. At the bottom of the edit report form click cancel. <br>
xi.  Are you directed back to the My reports page? <br> 

**All tests performed and no errors found.**

**User Story 6. Delete Reports**

i.   Log in to a registered account. <br> 
ii.  In the My Reports page, click on a report to expand it. <br>
iii. Click on the Delete Report button, does a modal pop up confirming you want to delete the report? <br>
iv.  Click cancel, are you directed back to the My Reports page? <br>
v.   Expand a report and click delete report again. <br>
vi.  Click delete report in the pop up modal, are you directed back to the My Reports page? <br> 
vii. Has the report you deletd been removed from the My Reports page? <br>

**All tests performed and no errors found.**

**User Story 7. Administrator Reports**

i.   Log in using an Administrator account.<br>
ii.  Are you directed to the My Reports page once logged in? <br>
iii. Can the All Reports link be viewed in the navigation bar? <br>
iv.  Click on the All Reports link, are you taken to the All Reports page? <br>
v.   Expand each report in turn, have they been submitted by different users? <br>
vi.  Are the edit and delete buttons only available on the reports submitted by Admin? <br>

**All tests performed and no errors found.**

**User Stories 8 & 9. Football Fan / Coach**

i.   Register a new account. <br>
ii.  Click the Submit Report Link. <br>
iii. Complete a report on your favourite team / Team that you coach. <br>
iv.  Check the My Reports page to ensure the report is there. <br>
v.   Log out of your account. <br>
vi.  Log back in and expand the report to check the details. <br>
vii. Submit another report. <br>
vii. Check the My Reports page to ensure more than one report is now showing. 

**All tests performed and no errors found.**

**The website was tested using a Microsoft Surface Pro on Windows 10, on the following browsers**

* Google Chrome - 