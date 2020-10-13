from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = ['post_notice', 'post_title', 'post_content']

        widgets = {

            'post_notice': forms.CheckboxInput(

            ),

            'post_title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),

            'post_content': forms.CharField(widget=CKEditorUploadingWidget()),
        }


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=CKEditorUploadingWidget(), required=True)