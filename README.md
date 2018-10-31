# django-admin-panel

**Task - Python Developer**

Based on the Django freamework, write a simple generating module so-called "admin site" like the default one available in the Django. The interface should be simple and minimalistic.

__The module should meet the following requirements:__

- Ability to add models (migrated to the database) to the implemented admin site
- The view with list of models added to it
- View of all objects of a given model (List View)
- Ability to add, update, delete an object (Create, Update, Delete View)
- All views, along with their corresponding URLs, should be generated automatically.
- Plug in the plugin under any user-selected root url
- Access to the admin site should be limited to users with appropriate permissions
- At the discretion, views can share the API (Django REST Framework) or be rendered to HTML.
- The solution should be sent as a link to the project's repository and contain readme and requirements.txt files with the pip requirements
- The project should be prepared entirely in English, the use of branches and well-written commit is an additional advantage.

__Launching the project:__

- Go to the myadminpanel folder (django-admin-panel/myadminpanel)
- Open CMD
- Run command: python manage.py migrate
- Run command: python manage.py makemigrations adminpanel, polls
- Run command: python manage.py migrate
- Run command: python manage.py createsuperuser
- Create an admin account
- Log in to the admin account
- In the browser, go to the website http://127.0.0.1:8000/adminpanel/

__Models:__

MyAdminPanel:
- model_name - CharField(default='', blank=False, max_length=100)
- app_name - CharField(default='', blank=False, max_length=100)

Author:
- first_name - CharField(max_length=50)
- second_name - CharField(max_length=50)
- date_of_birth - DateField('date of birth')

Book:
- author - ForeignKey(Author)
- title - CharField(max_length=100)
- publishing_house - CharField(max_length=50)
- year - IntegerField(default=2000)
- city - CharField(max_length=50)
- country - CharField(max_length=50)
- genre - CharField(max_length=50)
- isbn - CharField(max_length=13)

Question:
- question_text - CharField(max_length=200)
- pub_date - DateTimeField('date published')

Choice:
- question - ForeignKey(Question)
- choice_text - CharField(max_length=200)
- votes - IntegerField(default=0)
