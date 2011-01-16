from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.hashcompat import sha_constructor

import random

attrs_dict = {'class': 'required'}


class SignupFormTos(SignupForm):
    """ Add a Terms of Service button to the ``SignupForm``. """
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                             label=_(u'I have read and agree to the Terms of Service'),
                             error_messages={'required': _('You must agree to the terms to register.')})

def identification_field_factory(label, error_required):
    """
    A simple identification field factory which enable you to set the label.

    :param label:
        String containing the label for this field.

    :param error_required:
        String containing the error message if the field is left empty.

    """
    return forms.CharField(label=_("%(label)s") % {'label': label},
                           widget=forms.TextInput(attrs=attrs_dict),
                           max_length=75,
                           error_messages={'required': _("%(error)s") % {'error': error_required}})

class AuthenticationForm(forms.Form):
    """
    A custom form where the identification can be a e-mail address or username.

    """
    identification = identification_field_factory("Email or username",
                                                  "Either supply us with your email or username.")
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput(attrs=attrs_dict, render_value=False))
    remember_me = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                                     required=False,
                                     label=_(u'Remember me for %(days)s') % {'days': userena_settings.USERENA_REMEMBER_ME_DAYS[0]})

    def __init__(self, *args, **kwargs):
        """ A custom init because we need to change the label if no usernames is used """
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        if userena_settings.USERENA_WITHOUT_USERNAMES:
            self.fields['identification'] = identification_field_factory("Email",
                                                                         "Please supply your email.")

    def clean(self):
        """
        Checks for the identification and password.

        If the combination can't be found will raise an invalid sign in error.

        """
        identification = self.cleaned_data.get('identification')
        password = self.cleaned_data.get('password')

        if identification and password:
            user = authenticate(identification=identification, password=password)
            if user is None:
                raise forms.ValidationError(_("Please enter a correct username or email and password. Note that both fields are case-sensitive."))
        return self.cleaned_data
	