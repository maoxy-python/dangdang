from django.shortcuts import render

# Create your views here.

def show_index(reqeust):
    return render(reqeust,'index.html')