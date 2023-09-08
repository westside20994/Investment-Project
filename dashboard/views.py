from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def user_dashboard(request):
    # Add context data here if needed
    return render(request, 'dashboard/index.html')
