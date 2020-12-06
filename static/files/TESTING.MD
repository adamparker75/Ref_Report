<div align="center">

# _**Testing**_

</div>

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