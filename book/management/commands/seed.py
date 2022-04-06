from book.models import Book
from django.contrib.auth.models import User

user1 = User.objects.create(name= "Alice")
user2 = User.objects.create(name= "Bob")
user3 = User.objects.create(name= "Cameron")

user1.books.create(title= "PythonBook").variations.create(kind= "paper book")
user1.books.create(title= "RailsGuide").variations.create(kind= "PDF")
user2.books.create(title= "RailsGuide").variations.create(kind= "PDF")
# user1.save()
# user2.save()