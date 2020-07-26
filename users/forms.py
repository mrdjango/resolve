from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


def clean(self, *args, **kwargs):
    email = self.clean_data.get('email')
    email_qs = User.objects.filter(email=email)
    if email_qs.exists():
        raise forms.ValidationError(
            "Email you entered is already exists!"
        )
    return super(UserRegisterForm, self).clean(*args, **kwargs)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

        def clean(self, *args, **kwargs):
            email = self.clean_data.get('email')
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError(
                    "Email you entered is already exists!"
                )
            return super(UserRegisterForm, self).clean(*args, **kwargs)


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
