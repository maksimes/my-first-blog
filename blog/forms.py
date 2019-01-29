from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)


class SearchForm(forms.Form):

    search_field = forms.CharField(label='Найти',
                                   widget=forms.TextInput(attrs={
                                       'placeholder':'Поиск по постам, их заг'
                                                     'оловкам и комментариям',
                                       'size':'60'}))
    sort_field = forms.BooleanField(label="Сначала старые", required=False)
