from django.shortcuts import render, redirect


def main_view(request, **kwargs):

	return render(request, "main.html", {})

def contact(request, **kwargs):

	return render(request, "contact.html", {})


def about_us(request, **kwargs):
	return render(request, "about.html", {})
