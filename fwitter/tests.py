import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Tweet


class TweetModelTests(TestCase):

    def test_was_published_recently_with_future_tweet(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_tweet = Tweet(pub_date=time)
        self.assertIs(future_tweet.was_published_recently(), False)
