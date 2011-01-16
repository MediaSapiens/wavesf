# Copyright 2010 Daniel Gray
# danamantium@gmail.com
# This file is part of django-gigyauth.
#
# django-gigyauth is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django-gigyauth is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with django-gigyauth.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *

from views import *

urlpatterns = patterns('',
    url(r'^login/return/$',gigya_login_return,name="gigya_login_return"),
    url(r'^login/$',gigya_login,name='gigya_login')
)

