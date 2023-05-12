from django.db import models

# Create your models here.
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils.text import slugify

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.blog_name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()
    featured_image = models.ImageField(upload_to='uploads/')
    tags = TaggableManager(blank=True)
    featured = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    mod_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, related_name='post' ,on_delete=models.CASCADE, null=True)

    meta_title = models.CharField(max_length=200, null=True, blank=True)
    meta_description = models.CharField(max_length=300, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title
    
