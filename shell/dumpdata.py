import os
os.system("python ../manage.py dumpdata knowledge.Category >>../data/Category.json")
os.system("python ../manage.py dumpdata auth.Group >>../data/Group.json")
os.system("python ../manage.py dumpdata user.User>>../data/User.json")
os.system("python ../manage.py dumpdata knowledge.DocumentStatus>>../data/DocumentStatus.json")
os.system("python ../manage.py dumpdata knowledge.Document>>../data/Document.json")
