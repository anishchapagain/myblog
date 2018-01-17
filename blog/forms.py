from django import forms
from blog.models import Blog

class BlogAddForm(forms.ModelForm):

	class Meta:
		model = Blog
		fields = ('title', 'body')