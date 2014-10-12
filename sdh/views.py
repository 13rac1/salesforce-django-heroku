from django.shortcuts import render, get_object_or_404

from models import Contact

def index(request):
    # Get ten Contacts
    contacts = Contact.objects.all()[:10] 
    context = {
        'contacts': contacts,
    }
    
    return render(request, 'sdh/index.html', context)
