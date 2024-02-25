from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
tax_rate = 0.15

def default_view(request):
    return HttpResponse("<h1>This is a site to calculate tax.</h1>")

def calculate_tax(request, price):
    price = float(price)
    total = price + (price * tax_rate)
    return HttpResponse(f"<h1>Total price with tax: ${total:.2f}</h1>")

def tax_rate_view(request):
    return render(request, 'tax/tax_rate.html', {'tax_rate': tax_rate})