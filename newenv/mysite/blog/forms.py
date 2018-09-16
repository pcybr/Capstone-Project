from django import forms


from .models import PostModel


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = [
            'title',
            'content'
        ]

class PostDeleteForm(forms.ModelForm):
	class Meta:
		model = PostModel
		fields = []
		

