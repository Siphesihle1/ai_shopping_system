# AI Shopping System
This is a mutli-agent shopping system similar to a recommendation engine. This system studies the user's search patterns, search history and purchase history and uses this information to provide the user with customised search results across various product categories.


URL: http://148.100.76.106:8080


# Steps to run the app on your local machine
1. Clone the repo
2. Create and activate a python environment: <br>

Linux:
```
virtualenv venv
source venv/bin/activate
```

Windows:
```
virtualenv venv
.\venv\bin\activate
```

3. Go to the project directory and install all the required dependencies
```
pip install -r requirements.txt
```


5. Go to settings.py and change the database connection and host details
   - Change DATABASES["HOST"] from 'localhost' to '148.100.76.106'
   - Change ALLOWED_HOSTS[0] from '148.100.76.106' to 'localhost'

6. Run <code>python manage.py runserver localhost:PORT</code>

# To push your changes to the repo do the following:
1. Go to settings.py and change the database connection and host details
   - Change DATABASES["HOST"] from '148.100.76.106' to 'localhost'
   - Change ALLOWED_HOSTS[0] from 'localhost' to '148.100.76.106'

2. Stage your changes <br>
```
git add *
```

3. Commit your changes <br>
```
git commit -m <comment>
# <comment> should describe the changes you made
# e.g Removed line 5 in <file>
```

4. Push your changes to the repository <br>
```
git push origin master
```

4. Go to setting.py and change the database connection details
   - Change 'localhost' to '148.100.79.67'


**Don't forget to push your latest changes to the repo**

# Database Connection Details
- HOST : 148.100.76.106
- ENGINE : django.db.backends.postgresql_psycopg2
- NAME : ai_shopping_system
- USER : dbadmin
- PASSWORD : admin12345
- PORT : 5432
