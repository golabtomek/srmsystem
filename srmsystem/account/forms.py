from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .models import Profile

class LoginForm(auth_views.AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({ 'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({ 'placeholder':'Password'})

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(help_text=False)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    field_order = [
            'username', 
            'password',
            'password2',
            'email',
            'first_name',
            'last_name'
            ]

    def __init__(self, *args, **kw):
        super(forms.ModelForm, self).__init__(*args, **kw)

        self.fields['username'].widget.attrs.update({ 'placeholder':'Username'})
        self.fields['password'].widget.attrs.update({ 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({ 'placeholder':'Repeat password'})
        self.fields['email'].widget.attrs.update({ 'placeholder':'E-mail address'})
        self.fields['first_name'].widget.attrs.update({ 'placeholder':'First Name'})
        self.fields['last_name'].widget.attrs.update({ 'placeholder':'Last Name'})
    
    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check to see if any users already exist with this email as a username.
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')