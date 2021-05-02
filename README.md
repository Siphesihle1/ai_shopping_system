# ai_shopping_system
This is a mutli-agent shopping system similar to a recommendation engine. This system studies the user's search patterns, search history and purchase history and uses this information to provide the user with customised search results across various product categories.

# Steps to run the app on your local machine
1. Clone the repo
2. Create and activate a python environment: <br>
   Linux:
   <code>virtualenv venv</code>
   <code>source venv/bin/activate</code>
   <br>
   Windows:
   <code>virtualenv venv</code>
   <code>.\venv\bin\activate</code>

3. Go to the project directory and install all the required dependencies
  <code>pip install -r requirements</code>

4. Go to setting.py and change the database connection details
  - Change 'localhost' to '148.100.79.67'

# Database Connection Details
- HOST : 148.100.79.67
- ENGINE : django.db.backends.postgresql_psycopg2
- NAME : ai_shopping_system
- PASSWORD : admin12345
- PORT : 5432
