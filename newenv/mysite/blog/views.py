from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import PostModel
from django.shortcuts import get_object_or_404
from .forms import PostModelForm, PostDeleteForm
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages

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

def post_model_update_view(request, id=None):
    template = "blog/update-view.html"
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj.title = form.cleaned_data['title']
        obj.content = form.cleaned_data['content']
        obj.save()
        context = {
            "form": PostModelForm()
        }
    return render(request, template, context)
    
def post_model_delete_view(request, id=None):
    template = "blog/delete-view.html"
    obj = get_object_or_404(PostModel, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/blog/")
    context = {
        "id": obj.id,
        "title": obj.title
    }

    # form = PostDeleteForm(request.POST or None)
    # if form.is_valid():
    #     obj = form.save(commit=False)
    #     obj.save()
    #     context = {
    #         "form": PostDeleteForm()
    #     }

    return render(request, template, context)



def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)

# Create your views here.
