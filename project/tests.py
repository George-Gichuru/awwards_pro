from django.test import TestCase
from project.models import Profile, Post, Rate

class TestModel(TestCase):
   def test_create_user(self):
    user = Profile.objects.create_user(username='new user', email='newuser@gmail.com', password1='password', password2='password')
    user.save()
    
    self.assertEqual(str(user), 'newuser')
    
   def test_create_post(self):
    user = Post.objects.create_user(username='newuser', email='newuser@gmail.com', password1='password', password2='password')
    user.save()
    post = Post.objects.create(user=user, image='', 
                               caption='test image', )
    post.save()
    
    self.assertEqual(str(post), 'newuser')
    
   def test_create_rate(self):
    user = ratings.objects.create_user(username='newuser', email='newuser@gmail.com', password1='password', password2='password')
    user.save()
    post = Post.objects.create(user=user, image='', 
                               caption='test image', )
    post.save()
    
    ratings = Rate.objects.create(user=user, post=post, body='just commented')
    ratings.save()
    self.assertEqual(str(ratings), 'just commented')

    


   