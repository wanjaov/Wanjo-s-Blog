from django.db import models
from django.contrib.auth.models import User

"""
TABLE COLUMN DATATYPES
1. VARCHAR(char) - It stores a specific number of characters, therefore we must give it a limit.
2. NUMBER(INT, FLOAT)
3. TEXT(string)
4. BLOB - For storing image and file paths
5. DATE
6. BOOLEAN

ORM FIELD DATATYPES: They are a obtained from table column datatypes. We access them using the module 'module'.
1. models.Charfield(max_length=X) - Translated from VARCHAR
2. models.Integerfield()
3. models.FloatField()
4. models.TextField()
5. models.Imagefield()
6. models.Filefield()
7. models.BooleanField(default=True) or models.BooleanField(default= False)
8. models.EmailField()
9. models.ForeignKey()

TODO: Look at other field datatypes in django in django orm
"""

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photo/', null=True, blank=True)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.CharField(max_length=300)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

"""

"""