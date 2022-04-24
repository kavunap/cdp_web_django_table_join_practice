from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
	path('create', views.create, name='create'),
    path('detail/<int:book_id>/', views.detail, name='detail'),
    path('edit/<int:book_id>', views.edit, name='edit'),
    path('delete/<int:book_id>', views.delete, name='delete'),
    path('__debug__/', include('debug_toolbar.urls')),
]
