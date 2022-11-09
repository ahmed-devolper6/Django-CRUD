from django.urls import path , include
from .views import all_post , add_post ,edit_post, single_post

app_name = 'crud'

urlpatterns = [
    path('',all_post,name='all_post'),
    path('<int:id>',single_post,name='single_post'),
    path('add',add_post,name='add_post'),
    path('edit/<int:id>',edit_post,name='edit_post'),
]
