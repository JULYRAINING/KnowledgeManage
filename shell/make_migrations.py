import os
os.system("python ../manage.py makemigrations knowledge")
os.system("python ../manage.py makemigrations user")
os.system("python ../manage.py makemigrations")

os.system("python ../manage.py migrate")




