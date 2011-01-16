import django.db.models as models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

class Profile(models.Model):
    """
    parameters we can get from gigya:
    
    birthMonth,isLoggedIn,city,UID,zip,birthYear,state,provider,email,
    UIDSig,photoURL,timestamp,loginProviderUID,signature,isSiteUID,proxiedEmail
    ,thumbnailURL,nickname,firstName,loginProvider,gender,lastName,profileURL
    birthDay,country,isSiteUser

    One unique user can have several UID's 
    """
    user 			= models.ForeignKey(User, unique=True, null=True)
    uid             = models.CharField(max_length=255)
    login_provider  = models.CharField(max_length=150)
    timestamp       = models.DateTimeField(null=True,blank=True)
    isLoggedIn      = models.BooleanField(default=False)    
    birthday        = models.DateField(null=True,blank=True)
    
    city            = models.CharField(max_length=150, null=True,blank=True)
    state           = models.CharField(max_length=150, null=True,blank=True)
    zip             = models.CharField(max_length=30, null=True,blank=True)
    country         = models.CharField(max_length=30, null=True,blank=True)
    photourl        = models.CharField(max_length=255, null=True,blank=True)
    
    first_name      = models.CharField(max_length=80, null=True,blank=True)
    last_name       = models.CharField(max_length=80, null=True,blank=True)
    gender          = models.CharField(max_length=2, null=True,blank=True)
    profileUrl      = models.CharField(max_length=2, null=True, blank=True)
    
def create_profile(sender, instance=None, **kwargs):
    if instance is None:
        return
    profile, created = Profile.objects.get_or_create(user=instance)

post_save.connect(create_profile, sender=User)