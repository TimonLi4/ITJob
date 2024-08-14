from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate ,login,logout
from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import LoginUserForm, ProfileUserForm,RegisterUserForm, UserPasswordChangeForm
from django.views.generic.edit import CreateView,UpdateView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView



class RegisterUser(CreateView):
    form_class=RegisterUserForm
    template_name='users/register.html'
    success_url=reverse_lazy('users:login')
    extra_content={
        'title': 'Регистрация',
    }

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}


"""def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request,'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request,'users/register.html',{'form':form})
"""

class ProfileUser(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    form_class=ProfileUserForm
    template_name='users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile',args=[self.request.user.pk])
    
    def get_object(self,queryset = None):
        return self.request.user



class LoginUser(LoginView):
    form_class=AuthenticationForm
    template_name='users/login.html'
    extra_context={'title':'Авторизация'}



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))