# Dementia Care & Selfcare
 #### The web application allows users to view, add, and comment on posts, May 13, 2020 

#### By:
* Mary Waithera
* Dennis Mwaniki
* Maureen Wairimu
* Joseph Ng'ang'a


# DESCRIPTION
Dementia Care & Selfcare is a simple application tailored to meet the needs of dementia patients' carers. The application offers useful information regarding dementia and dementia care. The application also offers useful tips that carers can use to prevent compassion fatigue and burnout. Finally, the site allows users to share their experiences and support each other through creating and commenting on posts

## Known Bugs
* None at the moment

## Behavior Driven Development (BDD)
Behavior                 |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads  |Users scroll | Users see available posts|
|The landing page loads  |Users click on news link in the navbar|Users are directed to the news view where they can view current news and research on dementia|
|The landing page loads  |Users click on dementia care link in the navbar|Users are directed to the dementia care template where they can view care tips and other resources|
|The landing page loads  |Users click on selfcare link in the navbar|Users are directed to the selfcare template where they can view selfcare tips and other resources|
|The landing page loads  |Users click on sign in button|Users are directed to sign in/register view, users sign in if they have an account or click on the sign up link to create an account|
|The landing page loads  |Users click on profile navbar link|Users see they profiles and options to edit or upload profile image|
|The post page loads     |Users click on read and comment link|Users see full post and options to edit, delete, or comment on post|
|The landing page loads  |Users click on sign out link in the navbar|Users are logged out|

## setup /Installation Requirements
### Prerequisites
* Python version 3.6 or later
* pip
* flask
* flask-uploads
* flask-login
* flask-wtf
* flask-mail
* flask-sqlalchemy
* sqlite
First clone the repo
   ```$ git clone https://github.com/Waithera-m/dementia-care-and-selfcare.git ```

After cloning, navigate to the project:
   `` $ cd dementia-care-and-selfcare``

Set up a virtual environment

Then install all the requirements through pip:
   ```$ pip install -r requirements.txt ```

Make the file executable:
   ```$ chmod +x start.sh```

Run the application:
   ```$ ./start.sh ```

Now navigate to your browser at: ```localhost:5000```


## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  Flask is a Python microframework.The framework's templates were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the application and extensions and loop through and display pitches and navigate to different views. 

## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creators via email: njihiamary11@gmail.com, dennismwaniki67@gmail.com, nungari100@gmail.com, murimimaureen8@gmail.com

## License

[MIT License](LICENSE.md)
Copyright (c) 2020 **Joseph Nganga**, **Waithera-m**, **Maureen Wairimu**, **Dennis Mwaniki**

