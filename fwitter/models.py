import datetime
from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=200)#data field for user's username
    first_name = models.CharField(max_length=200)#data field for users first name
    last_name = models.CharField(max_length=200)#data field for user's last name
    password = models.CharField(max_length=200)#data field for user's last name
    def __str__(self):
        return self.username#displays username if asked for

class Topic(models.Model):
    topic_text = models.CharField(max_length=200)#data field for a topic
    def __str__(self):
        return self.topic_text#displays topic if asked for

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#connects user with a tweet
    tweet_text = models.CharField(max_length=200)#data field for a tweet
    pub_date = models.DateTimeField('date published')#gets the time of when the tweet was made
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)#connects topics with a tweet
    def __str__(self):
        return self.tweet_text#displays tweet if asked for
    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()#displays if tweet was posted recently if asked for
        

