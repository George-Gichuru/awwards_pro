## AWWWARDS

The application will allow a USER to post a project he/she has created and get it reviewed by his/her peers.

## Author Information

Written by George Gichuru.

## Endpoints

- Get all posts: 'https://awwwardsapp.herokuapp.com/api/posts/' : Method = 'GET'

## Installation

Clone the repository
Create a virtual environment
Install Django and other requirements in my requirements.txt file in your repository folder
Run the IP address on the browser

## User Stories

These are the behaviours/features that the application implements for use by a user.

As a user I would like to:

- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View my profile page.


## Behaviour Driven Development

| Behavior                | Input description | Output description                                  |
| ----------------------- | ----------------- | --------------------------------------------------- |
| View Site      |  click on project site  | The project will be displayed when clicked           |
| Search users            | Username          | Results will be displayed on the results page       |
| Login, Signup or Logout | Email, Password   | User will be either loggedin, registered, loggedout |
| edit profile | click on the user at the top right of the navbar | Redirected where one can be able to edit their profile |
| view project  | click on the view project button |  Redirected to a page where you can rate the projects usability,design,content and creativity |
| Submit your own project | Top right at the navbar(this can only be visual if the user is authenticated) | your created project |

## SetUp / Installation Requirements

### Prerequisites

- python3.10.4
- pip
- virtualenv

## Running the Application

- Creating the virtual environment

        $ python3.10.4 -m venv --without-pip env
        $ source env/bin/activate

- Installing Django

        $ python3.10.4 -m pip install Django
        $ python3.10.4 -m pip install cloudnary
        $ python3.10.4 -m pip install psycopg2

## Technologies Used

- Python3.10.4
- Django
- Bootstrap
- Javascript

Live Link: > https://awwwardsapp.herokuapp.com/

## Known Bugs 

The search functionality

## Contact Information

To reach me, email me at: > gichurugeorge092@gmail.com


License
MIT License

Copyright (c) [2022] [**George Gichuru**]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.