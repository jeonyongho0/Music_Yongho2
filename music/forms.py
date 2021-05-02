from django import forms
from music.models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = '__all__'
        #field = ['music_name', 'music_brand', 'music_price', 'music_buy', 'music_producer', 'music_quantity']
