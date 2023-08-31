from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 32},
        {"name": "Charlie", "age": 28},
        {"name": "David", "age": 22},
        {"name": "Eve", "age": 30},
        {"name": "Frank", "age": 42},
        {"name": "Grace", "age": 19},
        {"name": "Hannah", "age": 36},
    ]
    text = """ 
    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nemo magni iste iure fugiat doloremque minus ex. Omnis perferendis dicta porro ipsum quos, quaerat ipsa pariatur reprehenderit facilis! Cupiditate, incidunt quae?"""

    vegetables = ["Pumpkin", "Tomato"]

    return render(
        request,
        "index.html",
        context={
            "page": "Home123",
            "people": people,
            "text": text,
            "vegetable": vegetables,
        },
    )


def aboutus(request):
    context = {"page": "About Us"}
    return render(request, "aboutus.html", context)


def contact(request):
    context = {"page": "Contact"}
    return render(request, "contact.html", context)
