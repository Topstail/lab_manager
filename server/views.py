from django.shortcuts import render

# Create your views here.

def show_all_host(request):
    host = []
    return render(request, 'host_list.html', locals())

def show_dashboard(request):
    labs = []
    print(request.path)
    return render(request, 'dashboard.html', locals())
