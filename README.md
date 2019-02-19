I am a novice developer.
Here you can see my project, which I did for the purpose of learning
and mastering skills.

Comments to the code in Russian, so that it would be easy to understand not
for people who do not speak English, because first of all this will be read
by Russians.

This is a small blog where an admin can post,
and users can write comments to them and rate them (like).
There is a feedback form that sends feedback to the email administrator.
Users can edit their profile, add a photo,
view profiles of other users.

The main logic is written in Python-3.6.7, Django 11.20.0
Postgres is used to implement a case-insensitive search.
instead of standard SQLite

The site is deployed on Heroku <https://maks-blog.herokuapp.com/>
Since Heroku does not store static files and files for a long time
users, used Content Delivery Network - Amazon S3.
Settings in settings.py made with the above written.
For dynamism, some parts are made in JavaScript.

Another part of the site is implemented for the administrator, where he can
manage posts, comments, likes, user profiles,
view what was sent as feedback.

The list of what is installed in the deployment environment is in the file
requirements.txt
The Python version is in the runtime.txt file.
The Procfile file is used to run a project on heroku.
README.RU - file with the description in Russian.
