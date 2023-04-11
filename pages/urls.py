from django.urls import path
from pages.views import AboutPageView, AnnualReportPageView, ArchivesPageView, ArticleDetailView, ArticlesPageView, ContactView, DonationView, EventDetailView, GalleyView, LoginView, NewsDetailView, NewsPageView, BoardPageView, CompletedProgramPageView, EventsPageView, KeyPageView, MessageFromDirectorPageView, MissionPageView, OngoingProgramPageView, OutcomePageView, PartnerPageView, ProgramDetailView, TeamPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('message-from-director/', MessageFromDirectorPageView.as_view(), name='msg'),
    path('outcomes/', OutcomePageView.as_view(), name='outcome'),
    path('annual-reports/', AnnualReportPageView.as_view(), name='reports'),
    path('archives/', ArchivesPageView.as_view(), name='archives'),
    path('mission/', MissionPageView.as_view(), name='mission'),
    path('key/', KeyPageView.as_view(), name='key'),
    path('our-partner/', PartnerPageView.as_view(), name='partner'),
    path('ongoing-program/', OngoingProgramPageView.as_view(), name='ongoingprogram'),
    path('completed-program/', CompletedProgramPageView.as_view(), name='completedprogram'),
    path('events/', EventsPageView.as_view(), name='events'),
    path('news/', NewsPageView.as_view(), name='news'),
    path('articles/', ArticlesPageView.as_view(), name='articles'),
    path('teams/', TeamPageView.as_view(), name='teams'),
    path('gallery/', GalleyView.as_view(), name='gallery'),
    path('board-members/', BoardPageView.as_view(), name='boards'),
    path('contact-us/', ContactView.as_view(), name='contact'),
    # details-page
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='articledetail'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='newsdetail'),
    path('programs/<slug:slug>/', ProgramDetailView.as_view(), name='programdetail'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='eventdetail'),
    # donation
    path('donation/', DonationView.as_view(), name='donation'),
    # loginview
    path('login/', LoginView.as_view(), name='login'),
]