from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import ProfileModel
from contact.models import bloodrequest
from django.contrib.auth.models import User
from django.db.models import Q, Count
from home.models import reportdoner,bloodbank,event,sliderimg


def home(request):
    user=request.user
    br = bloodrequest.objects.all().order_by('-id')
    slid = sliderimg.objects.all().order_by('-id')



    if user.is_authenticated:
        pr=menu_profile(request)

        return render(request, 'home.html',{'pf':pr ,'queryset':br,'slimg':slid})
    else:
        return render(request, 'home.html',{'queryset':br,'slimg':slid})

def menu_profile(request):

    profile = ProfileModel.objects.get(user=request.user)
    return profile

def filter(request):
    bloodd=request.POST['blood']
    state =request.POST['state']
    district =request.POST['district']
    city =request.POST['city']
    qs = ProfileModel.objects.all().order_by('-id')

    if bloodd:
        qs = qs.filter(bloodgroup=bloodd)

        if state:
            qs = qs.filter(state=state)

            if district:
                qs = qs.filter(district=district)

                if city:
                    qs= qs.filter(Q(city__icontains=city))

                    return qs

                else:
                    return qs

            else:
                return qs

        else:
            return qs

def blood(request):
    user=request.user

    if user.is_authenticated:
        pr=menu_profile(request)

        if request.method == "POST":
            qs = filter(request)
            context = {'queryset': qs,'pf': pr}
            return render(request, 'blood.html',context)
        context = {'pf': pr}
        return render(request, 'blood.html',context)

    if request.method == "POST":
        qs= filter(request)
        context = {'queryset': qs}
        return render(request, 'blood.html',context)

    else:
        return render(request, 'blood.html')

def report(request, ProfileModel_id):
    usenet1 = get_object_or_404(ProfileModel, pk=ProfileModel_id)
    ruse=ProfileModel.objects.get(id=ProfileModel_id)

    user=request.user
    if user.is_authenticated:


        if request.method == "POST":
            reportdoner.objects.create(reason=request.POST['reason'],reportinfo=request.POST['reportinfo'],reportuseracc=ruse,mail=usenet1.user.email,mobile=usenet1.mobile)

            return render(request, 'blood.html', {'userreport':usenet1,'pf':ruse})
        return render(request, 'report.html', {'userreport':usenet1,'pf':ruse})

    if request.method == "POST":
        reportdoner.objects.create(reason=request.POST['reason'],reportinfo=request.POST['reportinfo'],reportuseracc=ruse,mail=usenet1.user.email,mobile=usenet1.mobile)

        return render(request, 'blood.html', {'userreport':usenet1})
    else:

        return render(request, 'report.html', {'userreport':usenet1})


def changeavailable(request):
    profile = ProfileModel.objects.get(user=request.user)
    if request.method == "POST":
        profile.avilable=request.POST['available']
        profile.save()
        return redirect('profile')
    else:

        return render(request, 'home.html')

def searchbank(request):
    state =request.POST['state']
    district =request.POST['district']
    city =request.POST['city']
    bdm = bloodbank.objects.all().order_by('-id')


    if state:
        bdm = bdm.filter(state=state)


        if district:
            bdm = bdm.filter(district=district)


            if city:
                bdm = bdm.filter(city__icontains=city)

                return bdm

            else:
                return bdm

        else:
            return bdm

def bloodbank1(request):
    user=request.user

    if user.is_authenticated:
        pr=menu_profile(request)

        if request.method == "POST":

            bdm= searchbank(request)

            context = {'queryset': bdm,'pf': pr}
            return render(request, 'bloodbank.html',context)
        context = {'pf': pr}
        return render(request, 'bloodbank.html',context)

    if request.method == "POST":
        bdm= searchbank(request)
        context = {'queryset': bdm}
        return render(request, 'bloodbank.html',context)

    else:
        return render(request, 'bloodbank.html')



def eventblog(request):
    user=request.user
    blgdata = event.objects.all().order_by('-id')
    if user.is_authenticated:
        pr=menu_profile(request)


        context = {'pf': pr,'blogs':blgdata}
        return render(request, 'event.html',context)
    return render(request, 'event.html',{'blogs':blgdata})


def about(request):
    user=request.user
    if user.is_authenticated:
        pr=menu_profile(request)
        context = {'pf': pr}
        return render(request, 'about.html',context)
    return render(request, 'about.html')



