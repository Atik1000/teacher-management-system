import logging
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from customauth.forms import LoginForm

logger = logging.getLogger(__name__)


class LoginView(LoginView):
    """ Custom login view """
    template_name = 'customauth/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')
        form = self.form_class
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard:dashboard')
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                messages.error(request, 'Invalid email or password')
        else:
            print(form.errors)
            logger.error(f'Invalid form data: {form.errors}')
            messages.error(
                request, 'Invalid email or password. Please enter correctly.'
            )
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)
