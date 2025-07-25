from django.shortcuts import render,redirect

from .models import Visitor


# Create your views here.
def visitor_from_view(request):
    if request.method == "post":
        names = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        purpose = request.POST.get('purpose')
        Visitor.objects.create(name=names,email=email,phone=phone,purpose=purpose)
        return redirect('visitor-list')
    else:
        return render(request, 'visitor_form.html')