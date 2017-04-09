import os
os.system("python manage.py loaddata data/Group.json")
os.system("python manage.py loaddata data/User.json")
os.system("python manage.py loaddata data/Category.json")

os.system("python manage.py loaddata data/DocumentStatus.json")
os.system("python manage.py loaddata data/Document.json")
