from django.shortcuts import render

#about view
def about_us(request):
    return render(request, 'about.html')

#join view
def join_us(request):
    return render(request, 'join.html')

#help center view
def help_center(request):
    return render(request, 'help_center.html')

#terms view
def terms(request):
    return render(request, 'terms.html')

#privacy view
def privacy(request):
    return render(request, 'privacy.html')