from django.conf import settings
from django.contrib.auth.models import User
import cPickle
from django.db import connection, transaction
import random
from gigyauth.models import Profile

def updateName( user, login, name, sid, postfix=0 ):
    """
        Create a unique login name on the system based on the user's 
        gigya credentials.  If a user of the given name already exists,
        Add an intrementally increasing number to their name
        until that username can be created
    """
    try:
        print "Trying to update name with login_name=", login
        user.first_name = name
        newlogin = login
        #strip the username of any special characters, including spaces
    
        if postfix:
            newlogin="%s%03d" % ( login, postfix )
        user.username = newlogin
        user.save()
    except Exception, e:
        print "Couldn't update name, rolling back", e
        transaction.savepoint_rollback(sid)
        updateName( user, login, name, sid, postfix+1 )


validName="abcdefghijklmnopqrstuvwxyzABCD"
sysrand = random.SystemRandom()

@transaction.commit_manually
def updateProfile( token, user=False, userinfo={'nickname':'newUser','first_name':'newUser'}):
    """
    Update the profile of the currently logged in user.
    If the user doesn't exist, make me one!
    
    @todo: replace print statements with logging statements
    """
  
    if not user:
        l= list(validName)
        sysrand.shuffle(l)
        l= "".join(l)
        print "Attempting to create a user with the name "+l
        user=User.objects.create_user(l,'')
        user.save()
        sid = transaction.savepoint()
        updateName( user, str(userinfo['nickname']).replace(' ',''), userinfo['first_name'], sid )
        transaction.savepoint_commit(sid)

    try: 
        userprofile = user.get_profile()
        userprofile.uid = cPickle.dumps(token) #ensures the token parameter is retreivable and unique
        userprofile.user_id = user.id
        userprofile.save()
        transaction.commit()
    except:
        transaction.rollback()
    return user


class GigyaBackend:
    """GigyaBackend for authentication

        > http://wiki.gigya.com/001_Authentication_Quick_start
        
    """
    def authenticate(self, uid,infodict):
        '''
            Authenticates the token by requesting user information from gigya
            Current behavior is that of the 1-step login process documented on their site.
            This could have a number of authentication backends if one wanted to implement
            multiple workflows for logging a user in.
        '''
        print "attempting authentication...."
        global validName
        userProfile=False
        cursor = connection.cursor()
        try:
            profile = Profile.object.get(uid=uid)
            #cursor.execute("select * from profiles_profile where uid=%s", [cPickle.dumps(uid)])
            #row = cursor.fetchone()
            #userProfile = dict(zip( ( i[0] for i in cursor.description), row ))
            return User.objects.get(id=profile.user.id)
        except Exception, e:
            print "Trying to create new user, probably okay, error was:", e
            userProfile=False
        finally:
            cursor.close()
      
        user = False
        try: 
            user = updateProfile( uid, False, infodict)
        except Exception, e:
            print "Error updating profile:", e
        if not user:
            print "Failed to create user" 
            return False
        print "Created User"
        return user
          
    def get_user(self, id):
        try:
          return User.objects.get(pk=id)
        except:
          return None