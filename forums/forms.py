from django.forms import ModelForm

from forums.models import Post




class CreatePostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ["title","content", "book_name", "rating", "author"]