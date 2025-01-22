from django import forms
from . import models, paser_librusec


class BookForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('librusec', 'librusec'),
        ('mybook', 'mybook'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        model = models.LibrusecParser
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'librusec':
            file_librusec = paser_librusec.parsing()
            for i in file_librusec:
                models.LibrusecParser.objects.create(**i)
