[![Build Status](https://travis-ci.com/Siphesihle1/ai_shopping_system.svg?branch=master)](https://travis-ci.com/Siphesihle1/ai_shopping_system) [![Coverage Status](https://coveralls.io/repos/github/Siphesihle1/ai_shopping_system/badge.svg)](https://coveralls.io/github/Siphesihle1/ai_shopping_system)

# AI Shopping System
This is a mutli-agent shopping system similar to a recommendation engine. This system studies the user's search patterns, search history and purchase history and uses this information to provide the user with customised search results across various product categories.

URL: http://148.100.79.67:8080

# Steps to run the app on your local machine
1. Clone the repo <br>
```
git clone https://github.com/Siphesihle1/ai_shopping_system
cd ai_shopping_system
```

2. Create and activate a python environment (you need to have python and virtualenv installed): <br>

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

3. Add the the following lines to <code>./.git/info/exlude</code> or <code>.\\.git\info\exclude</code> <br>

Windows:
```
.\venv\
.\django_project\__pycache__\
.\ecommerce\__pycache__\
.\ecommerce\migrations\__pycache__\
```

Linux:
```
./venv/
./django_project/__pycache__/
./ecommerce/__pycache__/
./ecommerce/migrations/__pycache__/
```

4. Install all the required dependencies <br>
```
pip install -r requirements.txt
```

5. Go to settings.py and change the database connection and host details
   - Change DATABASES["HOST"] from 'localhost' to '148.100.79.67'
   - Change ALLOWED_HOSTS[0] from '148.100.86.67' to 'localhost'

6. Run <code>python manage.py runserver localhost:PORT</code>

# To push your changes to the repo do the following:
1. Go to settings.py and change the database connection and host details
   - Change DATABASES["HOST"] from '148.100.79.67' to 'localhost'
   - Change ALLOWED_HOSTS[0] from 'localhost' to '148.100.79.67'

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

**Before making any changes, run <code>git pull</code> first to merge your local repository with the remote, otherwise you'll create a merge conflict.**

# Database Connection Details
- HOST : 148.100.79.67
- ENGINE : django.db.backends.postgresql_psycopg2
- NAME : ai_shopping_system
- USER : dbadmin
- PASSWORD : admin12345
- PORT : 5432
