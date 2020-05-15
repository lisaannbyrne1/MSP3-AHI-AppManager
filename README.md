# Client/Vet Appointments Manager

## Stream Three Project: Data Centric Development Milestone Project

### Demo
A live demo can be found <a href="https://ahi-task-manager.herokuapp.com/">here</a>

![Demo](https://github.com/lisaannbyrne1/MSP3-AHI-TaskManager/blob/master/static/demo/demo.gif "=Demo")

### UX

#### User stories
As a staff member, I expect to be able to create, edit, update, and delete accounts, appointments, and appointment purposes. 
As a vet, I expect to be able to view, edit and update appointments assigned to me for my clients. 

#### Strategy
The goal of this app is to make it as easy as possible for veterinary practice administrators or vets to create, view, update and delete appointments for their clients. 

#### Scope
This app will be aimed at veterinary practices, primary at administrative staff but will also be user friendly for vets themselves. 

#### Structure
This is a multipage app which includes a navigation with dropdown menus and simple page footer.  Each subsequent page is accessible through the app home page and allows users to create, update and deleted records as it is linked to MongoDB database. 

#### Skeleton
Desktop and mobile wireframes have been created <a href="https://github.com/lisaannbyrne1/MSP3-AHI-TaskManager/blob/master/static/wireframe/wireframe.pdf">click here</a>

#### Surface
The background of the page is white with the navigation and footer sections in green to provide definition. The font for the navigation and footer is white which stands out against the green background.  Each of the buttons are also coloured in green to stand out on the white background and provide synchronicity.  The font in the body of the app is black for clear and easy reading. 

#### Technologies
* HTML
* CSS/Materialize
* JavaScript/jQuery
* Python + Flask
* Mongo DB

### Features
The main features of this page are that it follows the users to interact with the database through CRUD.  It allows users to create, read, update, and delete records to and from the database. 

#### Features Left to Implement
In the future, I would like to include a log in page for clients to view and reschedule their appointments directly through the app. 

#### Testing
The app was tested against the criteria set out in the user stories and the criteria was met in each case. Then went on to test the app against CRUD functionality across all pages on the app. Across the app the user can view records, add records, edit records and delete records. During testing a bug in the code was found when trying to create a new appointment purpose, on review of this code I noticed there was a typo in the redirect on submit page.  The app was testing across several browsers including, Chrome, Firefox, Safari and Edge. Finally, I tested the app for mobile compatibility. During testing I found media queries were essential for the app to display and function correctly on mobile device of all sizes. It works best to display expanded data in 2 columns on desktop and 1 on mobile. 

#### Deployment
This app is manually deployed through Heroku and was deployed through the master branch. I choose manually deployed to allow me to commit and test changes before deployed to the real site.

### Credits


#### Content 
The data contents of this app and database is fictional for example purposes.

#### Media
This app does not require any images. 

#### Acknowledgements
I received inspiration from several sources for this project, they included feedback from users both internal and external to my current employer.   
