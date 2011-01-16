from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME


'''
TODO: 
- HttpResponseRedirect('/login/?next=%s' % request.path)
'''

def login(request):
  if request.method == 'POST':
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
      if user.is_active:
        login(request, user)
        # success
        return HttpResponseRedirect('/')
      else:
        # disabled account
        return direct_to_template(request, 'inactive_account.html')
    else:
      # invalid login
      return direct_to_template(request, 'invalid_login.html')
      
def logout(request):
  logout(request)