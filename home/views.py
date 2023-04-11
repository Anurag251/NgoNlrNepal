from django.shortcuts import render
from django.views import View
from home.models import About, News, Course, Events, Facility, ImageCategory, ImageGallery, MessageFromDirector, OurPartner, Program, ThreeZero, Slider, Testomonials

class HomeView(View):
    def get(self, request, *args, **kwargs):
        sliders = Slider.objects.filter(is_active=True)
        abouts = About.objects.all().order_by('-id')
        courses = Course.objects.all().order_by('-id')
        popular_courses = ThreeZero.objects.all().order_by('-id')
        facilities = Facility.objects.all().order_by('-id')
        programs = Program.objects.filter(status='ongoing').order_by('-id')
        allnews = News.objects.all().order_by('-id')
        allevents = Events.objects.all().order_by('-id')
        alltesto = Testomonials.objects.all().order_by('-id')
        imagecategory = ImageCategory.objects.all().order_by('-id')
        gallerys = ImageGallery.objects.all().order_by('-id')
        partners = OurPartner.objects.all().order_by('-id')
        context = {
            'sliders': sliders,
            'abouts': abouts,
            'courses': courses,
            'popular_courses': popular_courses,
            'facilities': facilities,
            'allnews': allnews,
            'allevents': allevents,
            'alltesto': alltesto,
            'gallerys': gallerys,
            'imagecategory': imagecategory,
            'partners': partners,
            'programs': programs,
        }
        return render(request, 'frontend/index.html', context)