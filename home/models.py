from django.db import models
from ckeditor.fields import RichTextField

class Slider(models.Model):
    subtitle = models.CharField(max_length=255, verbose_name='Sub Title',blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Title',null=True)
    description = models.TextField(verbose_name='Description',blank=True, null=True)
    image = models.ImageField(upload_to='slider/', verbose_name='Image', help_text='Image size should be 1520x570 px')
    link = models.CharField(max_length=255, verbose_name='Link', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name='Is Active', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(upload_to='about/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'History'
        
class MessageFromDirector(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='about/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Message From Director'
        
class KeyAchievement(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = RichTextField()
    image = models.ImageField(upload_to='about/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Key and Achievement'
        
class Mission(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = RichTextField()
    image = models.ImageField(upload_to='about/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Vision, Mission & Strategy'
        
class Outcome(models.Model):
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
    
class Course(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    image = models.ImageField(upload_to='course/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class ThreeZero(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    image = models.ImageField(upload_to='popular_course/', verbose_name='Image')
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Three Zeros'
    
class Facility(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='facility/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
PROGRAM_STATUS = (
    ('completed', 'Completed'),
    ('ongoing', 'On Going'),
)
    
class Program(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    summary = models.TextField(verbose_name='Summary')
    description = RichTextField(null=True)
    image = models.ImageField(upload_to='program/', verbose_name='Image')
    status = models.CharField(max_length=50, choices = PROGRAM_STATUS, verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/', verbose_name='Image')
    location = models.CharField(max_length=255, verbose_name='Location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "News"
        
class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/', verbose_name='Image')
    location = models.CharField(max_length=255, verbose_name='Location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Article"
    
class Events(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to='title/', verbose_name='Image')
    location = models.CharField(max_length=255, verbose_name='Location')
    event_date = models.CharField(max_length=255,null=True, verbose_name='Event Date')
    event_time = models.CharField(max_length=255,null=True, verbose_name='Event Time')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Events'
    
class Testomonials(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='Full Name')
    designation = models.CharField(max_length=255, verbose_name='Designation')
    image = models.ImageField(upload_to='testomonials/', verbose_name='Image')
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = 'Testomonials'
        
class ImageCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title', unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='image_category/', verbose_name='Image', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ImageGallery(models.Model):
    category = models.ForeignKey(ImageCategory, on_delete=models.CASCADE, verbose_name='Image Category')
    image = models.ImageField(upload_to='image_gallery/', verbose_name='Image')
    
    def __str__(self):
        return self.category.title
    
class Video(models.Model):
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.link
    
class Archive(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    files = models.FileField(upload_to='archive/', verbose_name='Files')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class OurPartnerDatas(models.Model):
    title = models.CharField(max_length=255, verbose_name='Name')
    tagline = models.CharField(max_length=255, verbose_name='Tag Line')
    description = RichTextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Our Partner Description'
    
class OurPartner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    image = models.ImageField(upload_to='our_partner/', verbose_name='Image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
    def __str__(self):
        return self.name
    
class AnnualReport(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to='annualreport_images/', max_length=100, null=True,blank=True)
    files = models.FileField(upload_to='annualreport/', max_length=200)
    
    def __str__(self):
        return self.title
    
POSITION = (
    ('team', 'Team Member'),
    ('board', 'Board Member'),
    ('both', 'Both'),
)
    
class Team(models.Model):
    fullname = models.CharField(max_length=225, verbose_name='Full Name')
    image = models.FileField(upload_to='teams/', max_length=100)
    designation = models.CharField(max_length=225)
    position = models.CharField(max_length=225, null=True)
    facebook = models.CharField(max_length=225, null=True, blank=True)
    linkedin = models.CharField(max_length=225, null=True, blank=True)
    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")

    def __str__(self):
        return self.fullname

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.name
    
class SocialAccount(models.Model):
    linkedin = models.CharField(max_length=245, blank=True, null=True)
    facebook = models.CharField(max_length=245, blank=True, null=True)
    twitter = models.CharField(max_length=245, blank=True, null=True)
    instagram = models.CharField(max_length=245, blank=True, null=True)

