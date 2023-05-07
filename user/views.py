from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from user.forms import LoginForm, RegistrationForm
from django.views.generic import ListView
from django.contrib.auth.models import User
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('/login/')


class LogRegView(ListView):

    def get_context_data(self, **kwargs):
        context = {
            'user': kwargs['user'],
            'log_form': kwargs['log_form'],
            'reg_form': kwargs['reg_form'],
        }

        return context

    def get(self, request):
        log_form = LoginForm
        reg_form = RegistrationForm
        return render(request, 'user/log_reg.html', context=self.get_context_data(
            user=None if request.user.is_anonymous else request.user,
            log_form=log_form,
            reg_form=reg_form
        ))

    def post(self, request):
        log_form = LoginForm(data=request.POST)
        reg_form = RegistrationForm(data=request.POST)
        if log_form.is_valid():

            user = authenticate(
                username=log_form.cleaned_data.get('username'),
                password=log_form.cleaned_data.get('password')
            )

            if user:
                login(request, user=user)
                return redirect('/')
            else:
                log_form.add_error(
                    'username', 'username or password is not correct')

        if reg_form.is_valid():
            if reg_form.cleaned_data.get('password') == reg_form.cleaned_data.get('confirm__password'):

                user = User.objects.create_user(
                    username=reg_form.cleaned_data.get('username'),
                    password=reg_form.cleaned_data.get('confirm__password')
                )
                return redirect('/')

            else:
                reg_form.add_error('confirm__password',
                                   'passwords are different')

        return render(request, 'user/log_reg.html', context=self.get_context_data(
            user=None,
            log_form=log_form,
            reg_form=reg_form
        ))


def login_view(request):

    if request.method == 'GET':
        log_form = LoginForm
        return render(request, 'user/log_reg.html', context={
            'log_form': log_form,
            'user': None if request.user.is_anonymous else request.user
        })

    if request.method == 'POST':
        log_form = LoginForm(data=request.POST)
        if log_form.is_valid():

            user = authenticate(
                username=log_form.cleaned_data.get('username'),
                password=log_form.cleaned_data.get('password')
            )

            if user:
                login(request, user=user)
                return redirect('/')
            else:
                log_form.add_error(
                    'username', 'username or password is not correct')

        return render(request, 'user/log_reg.html', context={
            'log_form': log_form,
            'user': None if request.user.is_anonymous else request.user
        })


def profile_view(request, id):
    return render(request, 'user/profile.html', context={
        'user': User.objects.get(id=id)
    })
