from django.shortcuts import render
from . import models

def index(request):
    banners = models.Baner.objects.all()
    services = models.Service.objects.all()
    contact_info = models.Contact.objects.all()
    agents = models.Agent.objects.all()
    homes = models.Home_imgs.objects.all()
    contct_us=models.Contct_us.objects.all()
    context = {
        'banners': banners,
        'services': services,
        'contacts': contact_info,
        'agents': agents,
        'homes': homes,
        'contct' : contct_us
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        models.Contact.objects.create(f_name=name, email=email, text=message)
      
    return render(request, 'index.html', context)
