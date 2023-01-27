import this

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from users.models import User
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from captcha.fields import CaptchaField

from .models import *


class AddPostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input'}))
    photo = forms.ImageField(label='Фото', widget=forms.FileInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Article
        fields = ['title', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()


class PersonalAreaForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Фамилия'}))
    patronymic = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Отчество'}))
    birth = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'single-input', 'placeholder': 'Дата рождения'}))
    school = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Школа'}))
    school_class = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Класс'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Имя пользователя',
                                                             'readonly': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'single-input', 'placeholder': 'Email адрес',
                                                            'readonly': True}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Домашний адрес'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'single-input', 'placeholder': 'Телефон'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'single-input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic', 'birth', 'school', 'school_class', 'username', 'email', 'address', 'phone_number', 'image')


