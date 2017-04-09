import os
os.system("python manage.py makemigrations knowledge")
os.system("python manage.py makemigrations user")
os.system("python manage.py makemigrations")

os.system("python manage.py migrate")



os.system("python manage.py loaddata data/Group.json")
os.system("python manage.py loaddata data/User.json")
os.system("python manage.py loaddata data/Category.json")
os.system("python manage.py loaddata data/DocumentStatus.json")
os.system("python manage.py loaddata data/Document.json")

os.system("python manage.py runserver")
