from django.shortcuts import render, redirect
from blog.models import Blog
from blog.forms import BlogAddForm
from django.contrib import messages

# Create your views here.

def home(request):

	blogs = Blog.objects.all()
	return render(request, "home.html", {'blogs': blogs})

def blog_add(request):

	if not request.user.is_authenticated():
		messages.error(request, "You must login to post a blog")
		return redirect("login")

	if not request.method == "POST":
		form = BlogAddForm
		return render(request, "blog_add.html", {'form': form})

	form = BlogAddForm(request.POST)

	if not form.is_valid():
		return render(request, "blog_add.html", {'form': form})

	blog = Blog()
	blog.user = request.user
	blog.title = form.cleaned_data['title']
	blog.body = form.cleaned_data['body']
	blog.save()

	return redirect("home")

def blog_detail(request,**kwargs):

	try:
		blog = Blog.objects.get(id=kwargs['blog_id'])

	except:
		messages.error(request, "Sorry this blog does not exist")
		return redirect("home")

	return render(request, "blog_detail.html", {'blog': blog})


def blog_edit(request, **kwargs):

	if not request.user.is_authenticated():
		messages.error(request, "You must login to post a blog")
		return redirect("login")

	try:
		blog = Blog.objects.get(id=kwargs['blog_id'])

	except:
		messages.error(request, "Sorry this blog does not exist")
		return redirect("home")

	form = BlogAddForm(instance=blog)

	if not request.method == "POST":
		return render(request, "blog_edit.html", {'form': form})

	form = BlogAddForm(request.POST, instance=blog)

	if not form.is_valid():
		return render(request, "blog_edit.html", {'form': form})

	blog.title = form.cleaned_data['title']
	blog.body = form.cleaned_data['body']
	blog.save()

	return redirect("blog_detail", blog.id)


def blog_delete(request, **kwargs):

	if not request.user.is_authenticated():
		messages.error(request, "You must login to delete a blog")
		return redirect("login")

	try:
		blog = Blog.objects.get(id=kwargs['blog_id'])

	except:
		messages.error(request, "Sorry this blog does not exist")
		return redirect("home")

	blog.delete()

	return redirect("home")

