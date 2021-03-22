from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    # email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')
    #
    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = User.objects.get(email=email)
    #
    #     except User.DoesNotExist:
    #         # Unable to find a user, this is fine
    #         return email
    #
    #     # A user was found with this as a username, raise an error.
    #     raise forms.ValidationError('This email address is already in use. Please try Different one!')



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']