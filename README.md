# Craft It With Pip


- Link to deployed site - [https://craft-it-with-pip-52cf6a8ea2e2.herokuapp.com/](https://craft-it-with-pip-52cf6a8ea2e2.herokuapp.com/)
- Link to GitHub repository - [https://github.com/coatespeter/craft-it-pp5](https://github.com/coatespeter/craft-it-pp5)

## Table of Contents

- [Craft It With Pip](#craft-it-with-pip)
  - [Table of Contents](#table-of-contents)
  - [Wireframes](#wireframes)
  - [Post and Comment Relationship Diagram](#post-and-comment-relationship-diagram)
  - [User Stories](#user-stories)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Future Features](#future-features)
  - [Setting up Django](#setting-up-django)
  - [Deploying to Heroku](#deploying-to-heroku)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)
  - [](#)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Libraries \& Frameworks](#libraries--frameworks)
    - [Acknowledgements](#acknowledgements)

## Wireframes

- At the beginning of the project, I made up some rough wireframes to give me an idea of what I wanted the site to look like. I used draw.io to create these wireframes. I made a wireframe for the home page and the about page.

![home]()
![about]()

## Post and Comment Relationship Diagram

- Initial plan

![post and comment relationship model]()

![post model]()

![comment model]()

## User Stories

- 

## Features

- 
  
![next]()
![prev]()

- Navbar - 

![navbar]()

- login status - When site usere are or are not logged in to the site, there is a banner below the buttons which will tell them their status.

![logged in]()
![not logged in]()

- 

![]()

- Register Page

![register]()

- Login Page

![login]()

- Logout Page

![logout]()

- 

![listings]()

- Authentication for comments.

![auth](static/images/authentication.png)

- Comments box

![comments]()

- 

![]()

- Contact admin form

![contact admin]()

- 

![default image]()

- Category images - Each category has its own image to represent it. By selecting the category when a post is being created, the listing image will appear as a default for the category.

![category images]()
![category images]()
![category images]()
![category images]()

## Technologies Used

- HTML - The project uses HTML to create the structure of the site.
- CSS - The project uses CSS to style the site.
- JavaScript - JavaScript was used to link the buttons to functionality
- Python - The project uses Python to create the backend of the site.
- Django - The project uses Django as the web framework.
- Heroku - The project is deployed on Heroku.
- Git - The project uses Git for version control.
- GitHub - The project uses GitHub to store the code and to plan the project.
- Postgres - The project uses Postgres as the database.
- Bootstrap - The project uses Bootstrap to style the site.
- Google Fonts - The project uses Google Fonts to import the font used in the site.
- ElephantSQL - The project uses ElephantSQL to host the database.
- Draw.io - The project uses Draw.io to create the wireframe.
- Cloudinary - The project uses Cloudinary to host the images.

## Future Features

- 

## Setting up Django

- Firstly, I installed all the relevant packages necessary for this site. These were, Django Gunicorn, Psycopg2, Django Heroku, Django Crispy Forms, Pillow, Cloudinary, DJ Database URL, and Whitenoise.
- I then created a new Django project and app.
- I migrated the database and created a superuser.
- I created a Procfile and a requirements.txt file.
- I created an admin account.
- I then created the models for the site and migrated the database again.
- I used Elephantsql to host the database and connected it to the site vis a newly created instance.
- I linked the database to the site using the DJ Database URL package.
- I then created the views and urls for the site.
- I then created the templates for the site.
- I then created the static files for the site.
- I then created the forms for the site.
- I logged into Heroku and created a new app. This app was linked via GitHub to my code base. I was able to deploy early on Heroku and keep an eye out for any bugs during the build process by redeploying the app and making sure everything was working as expected.
- I added the necessary config vars to Heroku to connect the database and the cloudinary image hosting.
  
## Deploying to Heroku

- Firstly, I created a new app on Heroku.
- I then connected the app to my GitHub repository.
- I then added the necessary config vars to Heroku to connect the database and the cloudinary image hosting.
- In the deploy section, I was able to manually deploy the app and keep an eye out for any bugs during the build process by redeploying the app and making sure everything was working as expected.

## Testing

### Manual Testing

|        Component     |       Test       |     Expected Result.      |           Actual Result         |
|----------------------|------------------|---------------------------|---------------------------------|
| Home page display as expected | Click on Home | Home page displayed | Home page with job listings and images visible. **PASS**  |
| About page link working | Selected About link | About page to display | About page displayed. **PASS** |
| About page displays | Click on About | About page to display as expected | About page displayed paragraph about the site and the table to contact admin. **PASS** |
| Form to register interest | Fill in all form fields | Alert renders on admin about page | Alert appeared on admin and about page. **PASS** |
| Form fields | Skip completing form fields | Alert to please fill in field.  | Alert appeared to fill in field. **PASS** |
| Email form field | Fill in email in incorrect format | Alert to include @ in email | Alert appeared to include @ for email. **PASS** |
| Work list display | Click on home | List of blog posts appears as 6 per page | List of work post displayed as 6 per page. **PASS** |
| Next and Prev Buttons | Work as expected | Next brings to next page, prev brings to previous | Next brought to next page, previous brought to previous lisings. **PASS** |
| Full Listing display | On click of listing title in blog list full listing display | Full listing displays | Full listing displayed. **PASS** |
| Comment Counter | Scroll to comment section | Shows users a small graphic with number of comments | Displays correctly. **PASS** |
| Log in Prompt | To display when not log in | Message display in like and comment to prompt a log in | Messaged displayed to visitor to log in to interact with post. **PASS** |
| Like Log in Prompt Link Working | Link to sign in page working | User brought to sign in page when clicked | User is brought to log in page when link. **PASS** |
| Comment | Site User can leave a comment | User can leave a comment and receive confirmation | Member placed comment and received notification that comment is awaiting approval. **PASS** |
| Not logged in Comment | If not logged in cannot comment | Message displaying to prompt visitor to log in if they want to leave a comment | Message displayed to visitor to sign in to leave comment. **PASS** |
| Comment Log in Link | Link working | On click of link user brought to sign in page | User clicked log in link and brought to log in page. **PASS** |
| Edit Comment | Can only edit own comment | Only users own comment can be edited | User could only edit their comment and receive an alert to state they did so. **PASS** |
| Delete Comment | Users can delete own comments | Users can delete comment once confirmation received | User could delete a comment they left once confirming they were happy to do so. **PASS** |
| Sign Up Form | Working as expected | New user created as a result | All fields of form completed and new user created. **PASS** |
| Log In Link on Sign Up page | Link working | On click log in link brings to log in page | User brought to log in page once clicked. **PASS** |
| Sign In Field Validation | Field Validation | Alert user if field missed | Field missed on completing form and alert received to fill in missing field. **PASS** |
| Password Validation | Password | Alert raised if criteria not met | Alert raised as a result of not matching password or too similar to user name. **PASS** |
| Log In Form | Allows user to sign in | User can sign in and gain full functionality of blog | User signed in successfully when correct credentials supplied. **PASS** |
| Sign Up Link on Log In Page | Link working | On click brought to sign up page | User brought to log in page once clicked. **PASS** |
| Sign Out | User can sign out | Sign out successfully and asked to confirm | User could sign out once they confirmed that was their intention. **PASS**|

## Bugs

![bugs]()

- I 

![code fix]()

![message tag]()

![message fix]()
- 
- 
- 
![overspill]()
![overspill-fix]()

![wave]()

## Credits

### Content

- The content for this site was inspired by the Code Institute Django project "I think therefore I blog".
- I used some Django educational material for some help with the setup of a Django-based site. [Django Tutorial](https://www.youtube.com/watch?v=oU9kN13-Xbs&t=269s)

### Media

- The images used in this site were obtained from [Unsplash]().
- Font - The font I used called Madina One was obtained from [Google Fonts]().
- Data storage - The data for this site is managed using [ElephantSQL]().

### Libraries & Frameworks

- The site uses the [Django web framework](https://www.djangoproject.com/).
- The site uses the [Bootstrap framework](https://getbootstrap.com/).

### Acknowledgements

- 