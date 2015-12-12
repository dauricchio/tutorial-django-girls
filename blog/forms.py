from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post#diciamo a Django quale model utilizzare per creare questo form 
        fields = ('title', 'text',)