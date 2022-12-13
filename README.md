<img src="/food-pickle.png" alt="kidney icon" width="200" height="200" style="">

# Welcome to UtahValleyPickleBall!

App Name : utahvalleypickleball

IS Section 2 Group 4
Development Team:

- Ellie Richardson
- Rachel Daniel
- Brooke Woodland
- Justin Brown

## Product Description:

Utah Valley Pickle Ball is designed as an open-source website for pickleball lovers in Utah Valley to share court locations and information about each court easily with one another.

## Technologies Used:

- [Python/Django](https://www.djangoproject.com/)
- [Postgresql](https://www.postgresql.org/)

## Installation:

1. [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download)
2. Dependencies - install all dependencies outlined in the requirements.txt file using "pip" e.g. `pip install django`
3. Database - Create a new postgres database
4. Environment Variables - Create a file called ".env" in the project's root directory (it is already included in .gitignore). When hosting, these environment variables are implemented and encrypted on the host and not in the codebase as a .env file. The .env is used only in the development environment. Here is a list of the environment variables you need to include in the .env:

- DEBUG = <debug_option> "on" or "off"
- SECRET_KEY = <django_secret_key>
- GOOGLE_MAPS_API_KEY = <the_google_maps_api_key>
- DB_PASSWORD = <postgres_database_password> For the database specifically
- DB_NAME = <postgres_database_name>

5. Migrations - In the terminal, run `python manage.py makemigrations`, then run `python manage.py migrate`
6. To start server, run `python manage.py runserver`

## Contributors:

Rachel Daniel<br>
Full Stack Developer<br>
[Rachel's LinkedIn](https://www.linkedin.com/in/rachel-daniel1/)<br>
[Rachel's Github](https://github.com/rachel-daniel)

Brooke Woodland<br>
Full Stack Developer<br>
[Brooke's LinkedIn](https://www.linkedin.com/in/brooke-woodland/)<br>
[Brooke's Github](https://github.com/wb385334)

Ellie Richardson<br>
Full Stack Developer<br>
[Ellie's LinkedIn](https://www.linkedin.com/in/elizabethhaws/)<br>
[Ellie's Github](https://github.com/egrich17)

Justin Brown<br>
Full Stack Developer<br>
[Justin's LinkedIn](https://linkedin.com/in/justin~j~brown/)<br>
[Justin's Github](https://github.com/justinbrown11)