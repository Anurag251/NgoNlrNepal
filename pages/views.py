from venv import create
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from home.models import About, AnnualReport, Archive, Article, Contact, ImageCategory, ImageGallery, KeyAchievement, Mission, News, Events, MessageFromDirector, OurPartner, OurPartnerDatas, Outcome, Program, Team, Video
from django.shortcuts import get_object_or_404
import sweetify
# email
from django.core.mail import EmailMessage
from django.conf import settings
from django.template import loader

from pages.models import Donation
from django.contrib import auth

class AboutPageView(View):
    def get(self, request, *args, **kwargs):
        about = About.objects.all().order_by('-id')
        context = {
            'about': about
        }
        return render(request, 'frontend/pages/about.html', context)
    
class MessageFromDirectorPageView(View):
    def get(self, request, *args, **kwargs):
        message_from_director = MessageFromDirector.objects.all().order_by('-id')
        context = {
            'msg_from_dir': message_from_director
        }
        return render(request, 'frontend/pages/message_from_director.html', context)
    
class MissionPageView(View):
    def get(self, request, *args, **kwargs):
        mission = Mission.objects.all().order_by('-id')
        context = {
            'mission':mission,
        }
        return render(request, 'frontend/pages/mission.html', context)
    
class KeyPageView(View):
    def get(self, request, *args, **kwargs):
        keyachievent = KeyAchievement.objects.all().order_by('-id')
        context = {
            'keys':keyachievent,
        }
        return render(request, 'frontend/pages/key.html', context)
    
class OutcomePageView(View):
    def get(self, request, *args, **kwargs):
        outcomes = Outcome.objects.all().order_by('-id')
        context = {
            'outcomes':outcomes,
        }
        return render(request, 'frontend/pages/outcome.html', context)
    
class AnnualReportPageView(View):
    def get(self, request, *args, **kwargs):
        reports = AnnualReport.objects.all().order_by('-id')
        context = {
            'reports':reports,
        }
        return render(request, 'frontend/pages/annual-reports.html', context)    
    
class ArchivesPageView(View):
    def get(self, request, *args, **kwargs):
        reports = Archive.objects.all().order_by('-id')
        context = {
            'reports':reports,
        }
        return render(request, 'frontend/pages/archives.html', context)  

class PartnerPageView(View):
    def get(self, request, *args, **kwargs):
        partners = OurPartner.objects.all().order_by('-id')
        ourpartners = OurPartnerDatas.objects.all().order_by('-id')
        context = {
            'partners': partners,
            'datas': ourpartners,
        }
        return render(request, 'frontend/pages/partners.html', context)
    
    def post(self, request, *args, **kwargs):
        return render(request, 'frontend/pages/partners.html')
    
class OngoingProgramPageView(View):
    def get(self, request, *args, **kwargs):
        programs = Program.objects.filter(status='ongoing').order_by('-id')
        context = {
            'programs': programs
        }
        return render(request, 'frontend/pages/ongoing-programs.html', context)

class CompletedProgramPageView(View):
    def get(self, request, *args, **kwargs):
        programs = Program.objects.filter(status='completed').order_by('-id')
        context = {
            'programs': programs
        }
        return render(request, 'frontend/pages/completed-programs.html', context)

class EventsPageView(View):
    def get(self, request, *args, **kwargs):
        events = Events.objects.all().order_by('-id')
        context = {
            'events': events
        }
        return render(request, 'frontend/pages/events.html', context)
    
class NewsPageView(View):
    def get(self, request, *args, **kwargs):
        news = News.objects.all().order_by('-id')
        context = {
            'news': news,
        }
        return render(request, 'frontend/pages/news.html', context)
    
class ArticlesPageView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by('-id')
        context = {
            'articles': articles,
        }
        return render(request, 'frontend/pages/articles.html', context)
    
class TeamPageView(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.all().order_by('-id')
        context = {
            'teams':team,
        }
        return render(request, 'frontend/pages/teams.html', context)
    
class BoardPageView(View):
    def get(self, request, *args, **kwargs):
        team = Team.objects.filter(position='board').order_by('-id')
        context = {
            'teams':team,
        }
        return render(request, 'frontend/pages/board-member.html', context)
    
class GalleyView(View):
    def get(self, request, *args, **kwargs):
        gallery = ImageCategory.objects.all().order_by('-id')
        galleryimages = ImageGallery.objects.all().order_by('-id')
        videos = Video.objects.all().order_by('-id')
        print(videos)
        context = {
            'imagecategory':gallery,
            'gallerys':galleryimages,
            'videos':videos
        }
        return render(request, 'frontend/pages/gallery.html', context)
    
class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'frontend/pages/contact.html')
    
    def post(self, request, *args, **kwargs):
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            mail_subject = request.POST.get('subject')
            user_message = request.POST.get('email')
            to_email = settings.EMAIL_TO_USER
            message = loader.render_to_string('frontend/email_message.html', {
                'name':name,
                'subject':mail_subject,
                'email':email,
                'message':user_message,
            })
            send_email = EmailMessage(mail_subject, message, to=[to_email], from_email=settings.EMAIL_HOST_USER)
            send_email.content_subtype = "html" 
            send_email.send()         
            sweetify.success(request, 'Your message has been sent successfully, we will reply soon') 
            Contact.objects.create(
                name = name,
                email = email,
                subject = mail_subject,
                message = user_message,
            )
            return redirect('contact')
        except Exception as e:
            print(e)
            sweetify.error(request, 'Something went wrong') 
            return redirect('contact')
    
    
# details page
class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        get_article = get_object_or_404(Article, slug = kwargs['slug'])
        recent_articles = Article.objects.exclude(slug=get_article).order_by('-id')
        context = {
            'article':get_article,
            'recent_articles':recent_articles,
        }
        return render(request, 'frontend/pages/article-details.html',context)
    
class NewsDetailView(View):
    def get(self, request, *args, **kwargs):
        get_news = get_object_or_404(News, slug = kwargs['slug'])
        recent_news = News.objects.exclude(slug=get_news).order_by('-id')
        context = {
            'news':get_news,
            'recent_news':recent_news,
        }
        return render(request, 'frontend/pages/news-details.html', context)

class ProgramDetailView(View):
    def get(self, request, *args, **kwargs):
        get_program = get_object_or_404(Program, slug = kwargs['slug'])
        recent_program = Program.objects.exclude(slug=get_program).order_by('-id')
        context = {
            'program':get_program,
            'recent_program':recent_program,
        }
        return render(request, 'frontend/pages/program-details.html', context)
    
class EventDetailView(View):
    def get(self, request, *args, **kwargs):
        get_event = get_object_or_404(Events, slug = kwargs['slug'])
        recent_event = Events.objects.exclude(slug=get_event).order_by('-id')
        context = {
            'program':get_event,
            'recent_program':recent_event,
        }
        return render(request, 'frontend/pages/event-details.html', context)
    
class DonationView(View):
    def post(self, request, *args, **kwargs):
        fullname = request.POST.get('fullname')
        number = request.POST.get('number')
        email = request.POST.get('email')
        receipt = request.POST.get('receipt')
        if fullname and number and email and receipt:
            Donation.objects.create(
                fullname = fullname,
                number = number,
                email = email,
                receipt = receipt
            )
            sweetify.success(request, 'Your message has been sent successfully, we will reply soon')
        else:
            return redirect('index')
        return HttpResponseRedirect('/')
    
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/admin")
        return render(request, 'frontend/auth/login.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                auth.login(request, user)
                return HttpResponseRedirect('/admin')
            else:
                sweetify.error(request, 'Credentials do not match')
        return render(request, 'frontend/auth/login.html')