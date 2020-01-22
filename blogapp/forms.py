from django import forms
from blogapp.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'autor',
            'title',
            'text',
            'created_date'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'author',
            'text',
        )
