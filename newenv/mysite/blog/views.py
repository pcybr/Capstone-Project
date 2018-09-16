from django.shortcuts import render
from django.http import HttpResponse
from .models import PostModel
from django.shortcuts import get_object_or_404


def post_model_list_view(request):
    qs = PostModel.objects.all()
    template = "blog/list-view.html"
    context = {
<<<<<<< HEAD
       	"object_list": qs,
    }
    return render(request, template, context)

def post_model_detail_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    context = {
        "object": obj,
    }
    template = "blog/detail-view.html"
    return render(request, template, context)

# Create your views here.
