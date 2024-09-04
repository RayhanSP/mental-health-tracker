from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275903',
        'name': 'Rayhan Syahdira',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)
