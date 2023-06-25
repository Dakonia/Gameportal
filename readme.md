# Welcome to My Project!

To get started, you need to install Django:

***pip install django***


Our project consists of two applications:

1. **news**: This is the main application that allows you to create posts, write comments on them, edit them, and more.

2. **registration**: This application handles user registration and login. Registration requires entering a password twice and an email address to receive a 4-digit activation code. The code must be entered on the website for successful registration.

## About the Project

The project allows users to create posts and leave comments on gaming-related topics.

When a comment is posted, an email notification is sent to the author. After the author approves or rejects the comment, the user receives a message indicating whether the comment was accepted or rejected.

The website includes a page that displays all the author's posts, and on the same page, the author can manage the comments received.

The project also features a weekly newsletter that sends all the posts from the past week to subscribers. To enable this feature, you will need to install Celery:

***pip install Celery***


***pip install redis***

***pip3 install -U "celery[redis]"***


To run Celery, follow these steps:

1. Start the project in one terminal:

***python manage.py runserver***


2. Start the Redis server in another terminal:

***redis-server***


3. Start Celery in a third terminal:

**celery -A RPG worker -l INFO -B***


After these steps, the system will send users a weekly email with all the new posts.

Happy coding!
