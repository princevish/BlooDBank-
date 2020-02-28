from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import ProfileModel
from django.contrib.auth.models import User
from django.db.models import Q, Count
from contact.models import contact,bloodrequest
# Create your views here.



def contactuser(request):
    user=request.user

    if user.is_authenticated:
        profile = ProfileModel.objects.get(user=request.user)


        if request.method == "POST":
            contact.objects.create(name=request.POST['name'], email=request.POST['email'], massage=request.POST['massage'])

            context = {'pf':profile,'massage':'Save Successfull.... '}
            return render(request, 'contact.html', context)
        return render(request, 'contact.html', {'pf':profile})
    
    if request.method == "POST":
        contact.objects.create(name=request.POST['name'], email=request.POST['email'], massage=request.POST['massage'])
        context = {'massage':'Form is Save '}
           
        return render(request, 'contact.html', context)
    else:
		
        return render(request, 'contact.html', )


def bloodrequest1(request):
    user = request.user
    bloodrequest2 = bloodrequest.objects.all().order_by('-id')

    if user.is_authenticated:
        profile = ProfileModel.objects.get(user=request.user)

        if request.method == "POST":
            bloodrequest.objects.create(name=request.POST['name'],
                                        email=request.POST['email'],
                                        bloodgroup=request.POST['blood'],
                                        mobile=request.POST['mobile'],
                                        address=request.POST['address'],
                                        city=request.POST['city'],
                                        district=request.POST['district'],
                                        state=request.POST['state'])



            context = {'pf': profile,'queryset':bloodrequest2, 'massage': 'Save Successfull... '}
            return render(request, 'bloodrequest.html', context)
        return render(request, 'bloodrequest.html', {'pf': profile,'queryset':bloodrequest2})

    if request.method == "POST":
        bloodrequest.objects.create(name=request.POST['name'],
                                    email=request.POST['email'],
                                    bloodgroup=request.POST['blood'],
                                    mobile=request.POST['mobile'],
                                    address=request.POST['address'],
                                    city=request.POST['city'],
                                    district=request.POST['district'],
                                    state=request.POST['state'])
        context = {'queryset':bloodrequest2,'massage': 'Form is Save '}

        return render(request, 'bloodrequest.html', context)
    else:

        return render(request, 'bloodrequest.html',{'queryset':bloodrequest2} )
