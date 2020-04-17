#python 3.7
#django 3.0.3
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Tweet, User, Topic
from django.contrib.auth import authenticate, login, logout




def index(request):#function for if someone goes to the index page
    if request.POST:#if something in the page was updated...
        if "inputUsername" in request.POST.keys():#if someone submitted a username...
            user = authenticate(username=request.POST['inputUsername'],password=request.POST['inputPassword'])#how does the authenticate function get user information? do i have to use the django user object?
            if user is not None:#if the information is correct...
                login(request, user)#login the user
        elif 'logout' in request.POST.keys():#if someone pressed the button to log out...
            logout(request)#logout the user

    if request.user.is_authenticated:#if the users information has been authenticated...(something went wrong here)
        loggedIn = True#Boolean value that will determine what message/abilities appear at the top of the screen
    else:
        loggedIn = False

        
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:10]#Data value that contains the 10 most recent tweets
    context = {'latest_tweet_list': latest_tweet_list, 'loggedIn':loggedIn, 'user':request.user,}#arraylist of objects necessary in the template
    return render(request, 'fwitter/index.html', context)#sends objects to the template

def user(request, user_id):
    user = User.objects.get(pk=user_id)#picks out the user from the given user id
    return render(request, 'fwitter/user.html', {'user':user})#send the users information to te template

def tweet(request, tweet_id):
    tweet = Tweet.objects.get(pk=tweet_id)#picks out a tweet from the given tweet id
    return render(request, 'fwitter/tweet.html', {'tweet':tweet})#send the tweet information to the template

def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)#retrieves user information if valid
    return render(request, 'fwitter/detail.html', {'user': user})#sends the user information to the template

def topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    return render(request, 'fwitter/topic.html', {'topic':topic})
    
