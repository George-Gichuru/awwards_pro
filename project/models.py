from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=300, default="No Bio..", blank=True)
    name = models.CharField(max_length=60,blank=True)
    country = models.CharField(max_length=60,blank=True)
    prof_pic = CloudinaryField('image')

    def __str__(self):
        return f"{self.user.username}"


class Post(models.Model):
    projectname = models.CharField(max_length=155)
    website = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    picture = CloudinaryField('image')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.projectname)

    def delete_post(self):
        self.delete()

    def save_post(self):
        self.save()

    @classmethod
    def search_post(cls,search_term):
        
        posts = cls.objects.filter( name__icontains=search_term)
        return posts

    @classmethod
    def posts(cls):
        return cls.objects.all()

class Rate(models.Model):
    design = models.IntegerField(null=True,default=0)
    usability = models.IntegerField(null=True,default=0)
    content = models.IntegerField(null=True,default=0)
    creativity = models.IntegerField(null=True,default=0)
    total =  models.FloatField(max_length=8, blank=True,null=True,default=0)
    user = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='rate',null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} Rate'

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    
