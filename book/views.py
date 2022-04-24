from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.db import connection

def index(request):
    data = Book.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/index.html', params)


def create(request):
    params = {
        'form': BlogForm(),
    }
    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        blog = Blog(title=title, content=content)
        blog.save()
        messages.add_message(request, messages.SUCCESS, "Blog created succesfully")    # 追加
        return redirect(to='/blog')
    return render(request, 'blog/create.html', params)

def detail():
    pass

def delete():
    pass

def edit():
    pass

def variations(request):
    data = Variation.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/variations.html', params)

def users(request):
    data = User.objects.all()
    params = {
        'data': data,
    }
    return render(request, 'book/users.html', params)

def books(request):
    data = Book.objects.all().select_related('user')
    params = {
        'data': data,
    }
    return render(request, 'book/index.html', params)

def user_detail(request, user_id): 
    user = User.objects.get(id=user_id)
    user_books=user.books.prefetch_related('variation_set')
    params = {
        'user': user,
        'user_books':user_books
    }
    print(connection.queries)
    return render(request, 'book/user_detail.html', params)
