from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
from .forms import PostModelForm

def post_model_list_view(request):
    qs = PostModel.objects.all()
    template = "blog/list-view.html"
	context = {
		"object_list": qs,
	}
    
	return render(request, template, context)

def post_model_create_view(request):
    template = "blog/create-view.html"
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {
            "form": PostModelForm()
        }
    return render(request, template, context)

# Create your views here.
