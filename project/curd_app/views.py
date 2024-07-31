from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


def create_view(request):
    template_name = "curd_app/create.html"
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Movie.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    template_name = "curd_app/create.html"
    object = Movie.objects.get(id=pk)
    form = MovieForm(request.POST)
    if request.method == "POST":
        form = MovieForm(request.POST, instacne=object)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Movie.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
    return render(request, template_name)



