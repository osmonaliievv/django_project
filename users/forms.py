from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Введите свою почту")
    phone_number = forms.CharField(required=True, label="Введите свой номер телефона")
    experience = forms.IntegerField(required=True, label='Введите свой опыт работы в годах')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Укажите пол')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'experience',
            'gender',
            'phone_number',
        )

    def save(self, commit=True):
        user = super(CustomUserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.experience = self.cleaned_data['experience']
        user.gender = self.cleaned_data['gender']

        if commit:
            user.save()
        return user

