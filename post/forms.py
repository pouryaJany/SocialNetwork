from django import forms
from .models import Post, Image

from django.utils.safestring import mark_safe
from django import forms


# class ImagePreviewWidget(forms.widgets.FileInput):
#     def render(self, name, value, attrs=None, **kwargs):
#         input_html = super().render(name, value, attrs=None, **kwargs)
#         img_html = mark_safe(f'Currently:<img style="width:250px; height:250px;" src="{value.url}"/>')
#         clear_html = mark_safe(f'<input type="checkbox">')
#         return f'{img_html} Change Image:{input_html}{clear_html}clear'


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'caption')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'caption': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostImageUpdateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image1', 'image2', 'image3', 'image4', 'image5')


class PostCreationForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageSelectionForPostCreationForm(forms.Form):
    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
