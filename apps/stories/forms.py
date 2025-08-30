from django import forms
from .models import Story

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ["name", "email", "title", "story", "wishlist_url", "allow_comments", "share_publicly"]
        widgets = { "story": forms.Textarea(attrs={"rows": 6}) }
