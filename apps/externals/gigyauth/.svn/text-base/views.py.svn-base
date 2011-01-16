import logging
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from django.shortcuts import render_to_response
from django.contrib.auth import login, authenticate

from models import Profile
from django.conf import settings

"""
-- Returned gigya parameters
birthMonth,isLoggedIn,city,UID,zip,birthYear,state,provider,email,
UIDSig,photoURL,timestamp,loginProviderUID,signature,isSiteUID,proxiedEmail
,thumbnailURL,nickname,firstName,loginProvider,gender,lastName,profileURL
birthDay,country,isSiteUser
"""
GIGYAUTH_API_KEY = getattr(settings,'GIGYAUTH_API_KEYS','2_YxjIbtIvfNHLWQr8rTcbVPD29y1iouWkhdShHIG2Hh7QUAbd_odcbN2DBXD8J9wv')
LOGIN_FAILURE_PAGE= getattr(settings,'GIGYAUTH_LOGIN_FAILURE_PAGE','/') #upate this to point to your error page for login failures

def gigya_login(request):
    """
    This just renders up the gigya javascript necessary to process logins.
    This also will integrate into django's core auth system and allow users to register
    using the normal / non oauth method
    """
    return render_to_response('gigyauth/login.html',{'api_key':GIGYAUTH_API_KEY},context_instance=RequestContext(request))
     
def gigya_login_return(request):
    """
    Process login responses.  There should be some settings for this
    to either do a quick account creation, prompt users for more information
    etc...
    
    For now,it simply creates a new user account with bare bones info, and then the user can populate their
    profile info from the various auth services after the fact. 
    """
    uid = request.GET.get('UID','-1')
    
    #1. Create a new Gigya user profile object
    profile                   = Profile()
    profile.uid               = uid
    profile.first_name        = request.GET.get('firstName','')
    profile.login_provider    = request.GET.get('login_provider','')
    profile.city              = request.GET.get('city','')
    profile.state             = request.GET.get('state','')
    profile.zip               = request.GET.get('zip','')
    profile.country           = request.GET.get('country','')
    profile.save()
    
    auth_user=False
    
    userInfo = { 'nickname':request.GET.get('nickname','0'),'first_name':request.GET.get('first_name','0') }
    #2. Authenticate and create a new user based on profile.uid
    try:
        if not request.user or not request.user.is_authenticated():
            auth_user = authenticate(access_token=uid,infodict=userInfo) #the uid from gigya is our unique key.
            #logging.debug("auth and create new user gigya uid:"+uid)
            print "Auth and create new user gigya id:"+uid
            #we need to add a little security here, but for now 
            #this should work.  i.e: signing is required at this stage.
        else:
            import backends.gigyaoauth
            backends.gigyaoauth.updateProfile(uid, request.user,userInfo)
            if request.session.has_key('redirect_url'):
                return HttpResponseRedirect("request.session['redirect_url']")
            return HttpResponseRedirect("/")
    except Exception,e:
        print "Generic Gigya Return Error:", e
        raise
        return HttpResponseRedirect(LOGIN_FAILURE_PAGE)
    
    #3. Log the newly created user in:
    if auth_user:
        login(request, auth_user)
    else:
        print "You are not logged in. Tsk. Tsk."
    
    #return
    return HttpResponseRedirect("/")
    
