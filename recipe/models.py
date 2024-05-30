from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length = 50)
    ingredients = models.TextField()
    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to="recipe/images/")
    instructions = models.TextField()
    created_on = models.DateField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} of Mr. {self.user.first_name} {self.user.last_name}"


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"User : {self.reviewer.user.first_name} ; Recipe: {self.recipe.user.first_name}"