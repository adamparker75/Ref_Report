<div align="center">

# **Ref Report**

</div> 

<p align="center">
    <img width="600" height="400" src="static/files/ref_report_readme_main_image.jpg">
</p>

<div align="center">

## **About**

</div>


This website was designed as a tool for use by Amateur referees. My son is keen to become a referee, 
and we found that other than writing the details in a notebook which are prone to being lost or misplaced,
there was nothing else of use to him to keep a record of the match details. I wanted to design a tool to help
him and other referrees to make a record of the game they have just taken charge of as soon as they get back
to the dressing room. <br>
Users are able to register a new account, login to their account where they can submit a new report, view all 
existing reports and also edit and delete reports as necessary. <br>

The deployed website can be viewed here - [Ref Report](https://adamp-ref-report.herokuapp.com/)

<div align="center">

## **UX**

</div>

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

### _**Database**_

I used MongoDB to store the data in the following collections.

**Match Type Collection**

The match type collection was used to store the different types of match a user may referee. This was utilised on the submit report page where a user
could select the different match types on the form.

| Key in Collection | Data Type |
|-------------------|-----------|
| _id               | ObjectId()|
| match_type        | String    |

**Reports Collection**

The reports collection was used to store the data submitted by the user from the submit report form. A text index was created on this collection on the following keys
match_type, referee_name, report_fixture, and report_report. This was to enable users to search for keywords if they were looking for a particular report.

| Key in Collection | Data Type |
|-------------------|-----------|
| _id               | ObjectId()|
| referee_name      | String    |
| report_date       | String    |
| match_type        | String    |
| report_fixture    | String    |
| report_score      | String    |
| report_scorers    | String    |
| report_cautions   | String    |
| report_dismissals | String    |
| report_report     | String    |
| created_by        | String    |

**Users Collection**

The users collection is used to store a users personal information, which is submitted on the registration form.

| Key in Collection | Data Type |
|-------------------|-----------|
| _id               | ObjectId()|
| firstname         | String    |
| lastname          | String    |
| username          | String    |
| password          | String    |


<div align="center">

## **Wireframes**

</div>

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

<div align="center">

## **Features**

</div>

* **Navigation Bar** - The navigation bar is consistent across the site, it uses [Materialize CSS](https://materializecss.com/) to make it beahave responsively 
on smaller devices.

* **Side Navigation Bar** - When viewed on smaller devices the links in the navigation bar, appear from the left when the 
hamburger menu is pressed.

* **Modal Pop Up** - The links to the log in and registration page utilise a modal pop up when viewed on smaller devices.

* **Collapsible Accordion** - The reports page utilises a collapsible from [Materialize CSS](https://materializecss.com/) when viewing the reports.

* **Submit Report** - Allows users to submit a match report to the database.

* **View Report** - Users can view a list of their reports and expand them to diaplay all of the details.

* **Edit / Delete Buttons** - Users have the option to edit or delete any of their reports.

* **Search Function** - Users can search their reports using keywords, for example the name of a particular team. 

### _**Features left to implement**_

<div align="center">

## **Technologies Used**

</div>

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

<div align="center">

## **Testing**

</div>

A lot of the testing was carried out using the developer tools in Google Chrome, I did this so that I could test whilst I was devloping the website
and make changes as I went along. It also helped me test the website on smaller devices and to ensure it was responsive. 
I also used tools such as [W3C Markup Validation Service](https://validator.w3.org/) to ensure my code was correct and had no errors.

### _**User Story Tests**_

**User Story 1. Register for an account**

1. Open the website. <br>
2. Does the home page appear? <br>
3. Are the menu links visible in the navigation bar? <br>
4. Click on the **register** menu link. <br>
5. Does the register an account page open? <br>
6. Click the register button, does the required field message appear? <br>
7. Fill out the fields correctly and click register. <br>
8. Do you go to the home page and a flashed message appears saying you have successfully registered? <br>
9. Click log out then click the register link again. Click on the link to the login page underneath the form. Do you go to the login page? <br>
10. Fill out the form with a username that already exists. Does a flashed message appear advising the username is taken?

**User Story 1a. Register for an account on mobile device**

1. Click on the hamburger menu link. Does the side navigation bar appear?<br>
2. Click the register link, does a pop up modal form appear? <br>
3. Follow steps 6-10 above. <br>

**All tests performed and no errors found.**

**User Stories 2 & 10. Log in to your account**

1. Click the **log in** link in the navigation bar. Does the login page appear? <br>
2. Click the log in button, does the required field message appear? <br>
3. Fill out the fields correctly and click log in. <br>
4. Does the My reports page open? <br>
5. Click log out and fill an incorrect username in, does a flashed message appear saying the username or password is incorrect? <br>
6. Click log out and fill an incorrect password in, does a flashed message appear saying the username or password is incorrect? <br>
7. CLick the Register account link underneath the form, does this take you to the register page?

**User Story 2a. Log in to your account on a smaller device**

1. Click on the hamburger menu link. Does the side navigation bar appear?<br>
2. Click the log in link, does a pop up modal form appear? <br>
3. Follow steps 2-7 above. <br>

**All tests performed and no errors found.**

**User Story 3. Submit a report**

1. When logged in, click the **Submit Report** link in the navigation bar. Does the submit report page open? <br>
2. Click the submit report button, does the required field message appear? <br>
3. Fill in all the text fields on the form. <br>
4. Click on the date field, does a date selector appear? Once the date is chosen does the correct date appear in the field? <br>
5. Click the Match Type field, do 4 options appear? Once selected does the correct option appear in that field? <br>
6. Once all fields are populated, click the submit report button. Dores a flashed message appear saying report added succesfully? <br>
7. Have you been redirected to the My reports page? Check to see if the report is added to the bottom of the reports section. <br>

**All tests performed and no errors found.**

**User Story 4. View Reports**

1. Log in to a registered account. <br>
2. Are you directed to the My Reports page once logged in? <br>
3. Does a list of reports appear? <br>
4. Click on a report, does the report expand to show more information?<br>
5. Is the report clear and legible? <br>
6. Click on the report header, does the report collapse? <br>
7. Click on another report, are the details different to the previous report? <br>
8. Type a relevant word in the search field and click search, do any reports appear? <br>
9. Click reset, do all reports appear? <br>

**All tests performed and no errors found.**

**User Story 5. Edit a report**

1. Log in to a registered account. <br> 
2. Are you directed to the My Reports page once logged in? <br>
3. Does a list of reports appear? <br>
4. Click on a report, does the report expand to show more information?<br>
5. Does the edit report button appear at the bottom of the report? <br>
6. Click the edit report button page, does the edit report page appear with the fields already filled? <br>
7. Make changes to the report. And click edit report.<br>
8. Are you directed back to the My reports page? <br>
9. Check the report to ensure the changes have been saved. <br>
10. Click edit on another report. At the bottom of the edit report form click cancel. <br>
11. Are you directed back to the My reports page? <br> 

**All tests performed and no errors found.**

**User Story 6. Delete Reports**

1. Log in to a registered account. <br> 
2. In the My Reports page, click on a report to expand it. <br>
3. Click on the Delete Report button, does a modal pop up confirming you want to delete the report? <br>
4. Click cancel, are you directed back to the My Reports page? <br>
5. Expand a report and click delete report again. <br>
6. Click delete report in the pop up modal, are you directed back to the My Reports page? <br> 
7. Has the report you deletd been removed from the My Reports page? <br>

**All tests performed and no errors found.**

**User Story 7. Administrator Reports**

1. Log in using an Administrator account.<br>
2. Are you directed to the My Reports page once logged in? <br>
3. Can the All Reports link be viewed in the navigation bar? <br>
4. Click on the All Reports link, are you taken to the All Reports page? <br>
5. Expand each report in turn, have they been submitted by different users? <br>
6. Are the edit and delete buttons only available on the reports submitted by Admin? <br>

**All tests performed and no errors found.**

**User Stories 8 & 9. Football Fan / Coach**

1. Register a new account. <br>
2. Click the Submit Report Link. <br>
3. Complete a report on your favourite team / Team that you coach. <br>
4. Check the My Reports page to ensure the report is there. <br>
5. Log out of your account. <br>
6. Log back in and expand the report to check the details. <br>
7. Submit another report. <br>
8. Check the My Reports page to ensure more than one report is now showing. 

**All tests performed and no errors found.**

**The website was tested using a Microsoft Surface Pro on Windows 10, on the following browsers**

* Google Chrome - Version 87.0.4280.88 (Official Build) (64-bit)
* Microsoft Edge - Version 87.0.664.52 (Official build) (64-bit)
* Mozilla Firefox - Version 83.0 (64-bit)

The website functioned correctly on all of these browsers. The forms appeared correctly, all modal pop ups worked. No issues found 
on any browser.

**The website was also tested on a number of devices as listed below**

* Google Pixel 3 xl using Google Chrome on Android 11.

* Moto E5 using using Google Chrome on Android 8.1.

* Ipad 6th Generation using Safari on IOS 13.4.

* Iphone 8 using Safari on IOS 13.4.

**I used the following websites for validation of my code**

[HTML validation.](https://validator.w3.org/)

[CSS validation.](https://jigsaw.w3.org/css-validator/)

[JavaScript validation.](https://jshint.com/)

### _**Issues found in testing**_

1. The search function would not work on the All reports page when logged in as Admin. To resolve this I created 
a separate 'helper' search function, which was then called by each app route function, passing in the name of the input field
and the template name as an argument.

2. I found that any user could view the All reports page, which should only be able to be seen by Admin. To resolve this
I created a function to check if the user is an admin, then called this function in an if statement in the 
app route for All Reports, to ensure that only Admin can view this page.

3. Any users were able to edit or delete othe users reports. This was resolved by creating a check in the edit report function
to see if the logged in user was equal to the author of the report, or was Admin. If this is true, then the logged in user is able
to edit and delete their own reports.

4. When testing the log in function on a large screen, I found the process was very fiddly as there were three links or buttons to 
click before the form appeared in a modal. On larger devices I removed the modal from both the login page and registration page and made this 
a form. 

5. When a user deleted a report, I found that it was always the first report in the list that was deleted instead of the report they were
wanting to delete. This was because the delete button was targetting a modal ID. To resolve this I changed the delete button to target the 
report_ID from the database.

<div align="center">

## **Deployment**

</div>

I developed Ref report using Gitpod, GitHub is used to store the repository, and the application is deployed on Heroku.

The following steps are taken to deploy the application.

### _**Git Clone**_

1. Navigate to my GitHub repository - <https://github.com/adamparker75/Ref_Report>
2. Click the dropdown that says code. 

<p align="center">
  <img width="300 height="50" src="static/files/git_clone.JPG">
</p> 

3. To clone with HTTPS copy the URL in the box.  

<p align="center">
  <img width="300 height="50" src="static/files/git_clone_2.JPG">
</p> 

4. Open up your preferred IDE (Integrated Development Environment)
5. Change the directory to the location you want the clone to be made.
6. Type **git clone** and then paste the copied URL from step 3.
7. Press Enter and your local clone will be created.
8. In your IDE create an **env.py** file. The file should contain the following.

<p align="center">
  <img width="300" height="100" src="static/files/env_py.JPG">
</p> 

* Make sure to add in your own **Secret Key, Mongo URI and Mongo DB name**.
* You should also add the **env.py** file to **.gitignore**. 

### _**Deploying to Heroku**_

1. In your IDE create a **requirements.txt** file by typing the following. <br>
**pip3 freeze --local > requirements.txt**
2. Next create a **Procfile** by typing the following. <br>
**echo web: python app.py > Procfile**
3. Open up the Procfile and if there is a blank line at the top of the file delete it.
4. Commit and push the files to Github.
5. Navigate to Heroku and login - <https://id.heroku.com/login>
6. Click on the new button and then choose create new app.

<p align="center">
  <img width="300" src="static/files/heroku_deploy.JPG">
</p> 

7. Give the app a name, choose a region, and then click create app.

<p align="center">
  <img width="400" height="200" src="static/files/heroku_deploy_2.JPG">
</p>

8. Click connect to GitHub and then search for the repository name. Once found, click connect.

<p align="center">
  <img width="400" height="200" src="static/files/heroku_deploy_3.JPG">
</p>

8. Click the settings tab in your Heroku app and then click reveal config vars.

<p align="center">
  <img width="300" src="static/files/heroku_deploy_4.JPG">
</p>

9. Add in the same variables as the **env.py** file.

<p align="center">
  <img width="400" height="200" src="static/files/heroku_deploy_5.JPG">
</p>

10. Click back to the deploy tab, choose a branch to deploy and then click enable automatic deploys.

<p align="center">
  <img width="400" height="200" src="static/files/heroku_deploy_7.JPG">
</p>

11. Click open app at the top of the page.

<p align="center">
  <img width="300" src="static/files/heroku_deploy_6.JPG">
</p>

<div align="center">

## **Credits**

</div>

### _**Content**_

* The code for the navigation bar was taken from [Materialize CSS](https://materializecss.com/navbar.html).
* The collapsible accordion was taken from [Materialize CSS](https://materializecss.com/collapsible.html).
* The modal pop up was taken from [Materialize CSS](https://materializecss.com/modals.html).
* The search functionality was created with help from the code institute data centric module.
* The code institute mini Task Manager project tutorial was used as a reference and guide.
* The wireframes were created with [Balsamiq](https://balsamiq.com/).
* The favicon was created on [favicon-generator](https://www.favicon-generator.org/).

### _**Media**_

* All of the images used on the site were taken from [Google Images](https://www.google.com/imghp?hl=EN).

### _**Acknowledgements**_

* To my wife **Claire Parker** for helping me test the website.
* To my mentor **Reuben Ferrante** for once again guiding me through this project, and being a great help as always.