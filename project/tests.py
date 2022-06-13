from django.test import TestCase
from project.models import Profile, Post, Rate


class TestModel(TestCase):
   def test_create_profile(self):
    profile = Profile.objects.create_profile()
    profile.save()
    
    self.assertEqual(str(profile))
    
   def test_create_post(self):
    user = Post.objects.create_post()
    post.save()
    post = Post.objects.create( )
    post.save()
    
    self.assertEqual(str(post), '')
    
   def test_create_rate(self):
    user = Rate.objects.create_rate()
    user.save()
    post = Post.objects.create()
    post.save()
    
    ratings = Rate.objects.create()
    ratings.save()
    self.assertEqual(str(ratings))

    


   