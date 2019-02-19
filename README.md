I am a novice developer.<br/>
Here you can see my project, which I did for the purpose of learning<br/>
and mastering skills.

Comments to the code in Russian, so that it would be easy to understand not<br/>
for people who do not speak English, because first of all this will be read<br/>
by Russians.

This is a small blog where an admin can post,<br/>
and users can write comments to them and rate them (like).<br/>
There is a feedback form that sends feedback to the email administrator.<br/>
Users can edit their profile, add a photo,<br/>
view profiles of other users.

The main logic is written in Python-3.6.7, Django 11.20.0<br/>
Postgres is used to implement a case-insensitive search.<br/>
instead of standard SQLite

The site is deployed on Heroku <https://maks-blog.herokuapp.com/><br/>
Since Heroku does not store static files and files for a long time<br/>
users, used Content Delivery Network - Amazon S3.<br/>
Settings in settings.py made with the above written.<br/>
For dynamism, some parts are made in JavaScript.

Another part of the site is implemented for the administrator, where he can<br/>
manage posts, comments, likes, user profiles,<br/>
view what was sent as feedback.

The list of what is installed in the deployment environment is in the file<br/>
requirements.txt<br/>
The Python version is in the runtime.txt file.<br/>
The Procfile file is used to run a project on heroku.<br/>
README.RU - file with the description in Russian.
