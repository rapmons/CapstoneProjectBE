from datetime import datetime
from django.db import models


class users(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    username= models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    delete= models.BooleanField(default=0)

class topic(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    name= models.CharField(max_length=100,unique=True)

class words(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    text= models.CharField(max_length=255)
    mean= models.CharField(max_length=255)
    spell= models.CharField(max_length=255)
    wordType= models.CharField(max_length=255)
    topic= models.ForeignKey(topic, on_delete=models.CASCADE,null=True)
    url=models.CharField(max_length=255)

class myWords(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    word= models.ForeignKey(words, on_delete=models.CASCADE)
    users= models.ForeignKey(users, on_delete=models.CASCADE)
    saveF=models.BooleanField(default=0)
    delete= models.BooleanField(default=0)
    url=models.CharField(max_length=255)

class historyTranslate(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    users= models.ForeignKey(users,on_delete=models.CASCADE)
    text= models.TextField()
    mean= models.TextField()
    delete= models.BooleanField(default=0)

class historyResult(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    users= models.ForeignKey(users,on_delete=models.CASCADE)
    numberQT= models.IntegerField(default=0)
    numberQF= models.IntegerField(default=0)
    topic= models.ForeignKey(topic,on_delete=models.CASCADE, null=True)
class historySearch(models.Model):
    id= models.AutoField(auto_created=True, primary_key=True)
    users= models.ForeignKey(users,on_delete=models.CASCADE)
    idSearch=models.IntegerField(default=0)
    delete= models.BooleanField(default=0)   




