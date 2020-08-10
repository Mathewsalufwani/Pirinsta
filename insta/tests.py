from django.test import TestCase

from .models import Profile, Post
from django.contrib.auth.models import User

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='mat')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='i am tired',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='mat', user=User(username='alufwany'))
        self.profile_test.save()

        self.image_test = Post(image='default.png', name='test', caption='random', user=self.profile_test)

    