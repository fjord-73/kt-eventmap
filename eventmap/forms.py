from django import forms
from.models import Visit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=54,
        help_text='※有効なメールアドレスを入力してください。',
        label='Eメールアドレス'
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',)