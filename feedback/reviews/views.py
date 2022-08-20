from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm 
from .models import Review

# Create your views here.

def review (request):
    if request.method == "POST":
    #     users_input = request.POST["username"]
    #     print(users_input , "***")
        form = ReviewForm(request.POST)
        if form.is_valid():
            # print(form.clean() ,"###")
            # rw=form.cleaned_data
            # review = Review(username=rw["username"],email=rw["email"], review=rw["review"], rating= rw["rating"])
            # review.save()
            # print('done', rw)
            form.save()
            return HttpResponseRedirect("/thank-you")

    else :
        form = ReviewForm()

    return render(request ,'reviews/review.html',
                {"form": form} ,
                )

def thank_you (request ):    
    return render(request , "reviews/thank_you.html" )