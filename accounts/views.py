from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import ProfileModel
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid Input'})
    else:

        return render(request, 'login.html')

@login_required(login_url="/accounts/login")
def logout(request):
    if 1 == 1:
        auth.logout(request)
        return redirect('home')



def signup(request):


    if request.method == "POST":
        if request.POST['pswd1'] == request.POST['pswd2']:

            if request.POST['birth']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'signup.html', {'error': 'Username Not Available'})
                except User.DoesNotExist:

                    user = User.objects.create_user(username=request.POST['username'],
                                                    first_name=request.POST['first_name'],
                                                    last_name=request.POST['last_name'], password=request.POST['pswd1'],
                                                    email=request.POST['username'])

                    ProfileModel.objects.create(user=user, avilable=request.POST['avilable'],
                                                district=request.POST['district1'],
                                                zipcode=request.POST['zipcode'], state=request.POST['state'],
                                                city=request.POST['city'], other_mobile=request.POST['mobile_other'],
                                                mobile=request.POST['mobile'], bloodgroup=request.POST['blood'],
                                                address=request.POST['address'], birthdate=request.POST['birth'],
                                                pic=request.FILES['propic'])
                    auth.login(request, user)
                    return redirect('profile')
            else:
                return render(request, 'signup.html', {'error': 'Don\'t Eligible for Donate Blood 17age '})

        else:
            return render(request, 'signup.html', {'error': 'Password Don\'t Matched Enter Correct Password'})
    else:
        return render(request, 'signup.html')


@login_required(login_url="/accounts/login")
def profileupdate(request):

    profile1 = ProfileModel.objects.get(user=request.user)
    context = {'pf': profile1}
    user = request.user
    if user.is_authenticated:

        if request.method == "POST":
            if request.POST['pswd1'] == request.POST['pswd2']:
                firstname = request.POST['first_name']
                lasttname = request.POST['last_name']
                email = request.POST['email']
                mobile = request.POST['mobile']
                mobileo = request.POST['mobile_other']
                dob = request.POST['birth']
                address = request.POST['address']
                city = request.POST['city']
                district = request.POST['district1']
                state = request.POST['state']
                zip = request.POST['zipcode']
                password1 = request.POST['pswd1']
                available = request.POST['avilable']
                pic1=request.FILES['propic']
                profile1.pic = pic1
                profile1.save()

                profile2 = ProfileModel.objects.filter( user = request.user).update(birthdate=dob,address=address,city=city,district=district,state=state,zipcode=zip,avilable=available,mobile=mobile,other_mobile=mobileo)
                user.first_name = firstname
                user.last_name = lasttname
                user.email = email
                user.username = email
                user.set_password(password1)

                user.save()

                user = auth.authenticate(username=email, password=password1)
                auth.login(request, user)
                return redirect('profile')


            else:

                return render(request, 'profileupdate.html',{'error': 'Password Don\'t Matched Enter Correct Password','pf':profile1}, context)
        else:

            return render(request, 'profileupdate.html', context)

    return render(request, 'profileupdate.html', context)

@login_required(login_url="/accounts/login")
def profile(request):
    profile = ProfileModel.objects.get(user=request.user)
    return render(request, 'profile.html', {'pf': profile})


        




