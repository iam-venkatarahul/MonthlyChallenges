from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
import django.http
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges_dict = {
    "january": "Go to new movies",
    "february" : "Sleep 8hrs a day",
    "march" :"Read a Book daily",
    "april" :"Stop watching Tv",
    "may":"Start Running",
    "june" :"Increase Protien intake",
    "july" :"Start Coding",
    "august": "Go to gym",
    "september": "Start Learning Full stack",
    "october" :"Eat Only Veg",
    "november" :"Start Running",
    "december" :"Start Vlogging",
}
#first view
def monthly_challenge(request , month):
    try:
        challenge_msg = monthly_challenges_dict[month]
        return render(request , "Challenges/challenges.html" , {
            "text": challenge_msg,
            "month_name": month.capitalize()
        })
    except:
        return HttpResponseNotFound("<h1>This month is invalid.....</h1>")
    
def monthly_challenge_number(request , month):
    months = list(monthly_challenges_dict.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is invalid.....</h1>")
    redirect_month = months[month- 1]
    redirect_path = reverse("month-chall", args=[redirect_month])  #challenge/1
    return HttpResponseRedirect(redirect_path)
    
def index_of_months(request):
    list_months = ""
    months = list(monthly_challenges_dict.keys())
    
    for month in months:
        c_month = month.capitalize()
        month_path = reverse("month-chall" , args=[month])
        list_months += f"<li><a href = \"{month_path}\">{c_month}</a></li>"
        
    response_data = f"<ui>{list_months}</ui>"
    return HttpResponse(response_data)
    