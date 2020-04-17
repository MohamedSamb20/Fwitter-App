from django.urls import path

from . import views

app_name='fwitter'
urlpatterns = [
    path('', views.index, name='index'),#goes to the basic index page if no specifiers are made
    path('<int:user_id>/userposts', views.user, name='user'),#goes to the page with the tweets of a specific user
    path('<int:tweet_id>/tweet', views.tweet, name='tweet'),#goes to the page of a specific tweet
    path('<int:user_id>/details', views.detail, name='detail'),#goes to a users page
    path('topics/<int:topic_id>', views.topic, name='topic')#goes to page with topics 
]
