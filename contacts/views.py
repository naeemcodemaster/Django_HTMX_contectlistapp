from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    contacts = request.user.contacts.all().order_by('-created_at')
    print("Fetched Contacts:", contacts)  # Debugging statement
    context = {
        'contacts': contacts,
    }
    return render(request, 'contacts.html', context)