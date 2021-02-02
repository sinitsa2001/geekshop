from django.conf import settings
from django.contrib import auth, messages
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm, UserProfileEditForm
from authapp.models import User
from basketapp.models import Basket


def send_verify_email(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])

    subject = f'подтверждение учетной записи {user.username}'

    message = f'Для подтверждения перейдите по ссылке: {settings.DOMAIN}{verify_link}'

    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently =False)


def verify(request, email, activation_key):
    # user = User.objects.get_object_or_404(email =email)
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = None
            user.save()
            auth.login(request, user)
        return render(request, 'authapp/verification.html')
    except Exception as ex:
        return HttpResponseRedirect(reverse('main'))


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
    context = {'form':form}
    return render(request, 'authapp/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user =form.save()
            if send_verify_email(user):
                print('success')
            else:
                print('failed')
            messages.success(request,'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('authapp:login'))
    else:
        form = UserRegisterForm()
        # messages.error(request,print(form.errors))

    context = {'form':form}
    return render(request, 'authapp/register.html', context,print(form.errors))

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('authapp:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)
    baskets = Basket.objects.filter(user=request.user)

    # total_quantity = 0
    # for basket in Basket.objects.filter(user=request.user):
    #     total_quantity += basket.quantity
    #
    # total_sum =0
    # for basket in Basket.objects.filter(user=request.user):
    #     total_sum += basket.sum()



    context = {
            'form':form,
            'baskets': baskets,
            'profile_form': profile_form,
            # 'total_quantity':sum(basket.quantity for basket in baskets),
            # 'total_sum': sum(basket.sum() for basket in baskets),
                   }
    return render(request,'authapp/profile.html',context)



def logout (request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))


