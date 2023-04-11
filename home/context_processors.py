from home.models import SocialAccount

def social_accounts(request):
    socials = SocialAccount.objects.all()
    return dict(socials=socials)