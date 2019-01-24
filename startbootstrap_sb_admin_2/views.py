from django.shortcuts import render, HttpResponse


def home_page_detail(request):
    return render(request, "home_page.html")

def blank_page(request):
    return render(request, "pages/blank.html")

def buttons_page(request):
    return render(request, "pages/buttons.html")

def forms_page(request):
    return render(request, "pages/forms.html")

def flot_page(request):
    return render(request, "pages/flot.html")

def grid_page(request):
    return render(request, "pages/grid.html")

def icons_page(request):
    return render(request, "pages/icons.html")

def login_page(request):
    return render(request, "pages/login.html")

def morris_page(request):
    return render(request, "pages/morris.html")

def notifications_page(request):
    return render(request, "pages/notifications.html")

def panel_page(request):
    return render(request, "pages/panels-wells.html")

def tables_page(request):
    return render(request, "pages/tables.html")

def typography_page(request):
    return render(request, "pages/typography.html")