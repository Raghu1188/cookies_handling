from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):
 reponse = render(request, 'Student/setcookie.html')
 reponse.set_signed_cookie('name', 'Raghuveer', salt='nm', expires=datetime.utcnow()+timedelta(days=2))
 return reponse

def getcookie(request):
 name = request.get_signed_cookie('name', default="Guest", salt='nm')
 return render(request, 'Student/getcookie.html', {'name':name})

def delcookie(request):
 reponse = render(request, 'Student/delcookie.html')
 reponse.delete_cookie('name')
 return reponse