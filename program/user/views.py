from django.contrib.auth import views, login
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect

from . import models, forms

# Create your views here.
class CreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserCreationForm
    template_name = 'user/create.html'
    success_url = reverse_lazy('user:update')

    def form_valid(self, form):
        ret = super().form_valid(form)
        login(self.request, self.object)
        return ret

class LoginView(views.LoginView):
    template_name = 'user/login.html'
    form_class = auth_forms.AuthenticationForm

class UpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = models.User
    form_class = forms.UserChangeForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('user:update')

    def get_object(self, queryset=None):
        return self.request.user

class PasswordChangeView(views.PasswordChangeView):
    form_class = auth_forms.PasswordChangeForm
    success_url = reverse_lazy('user:update')
    template_name = 'user/password.html'

class DeleteView(generic.DeleteView):
    model = models.User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user:sign-up')

    def get_object(self, queryset=None):
        return self.request.user

class CreaterApplicationView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.CreateView):
    model = models.Creater
    form_class = forms.CreaterForm
    template_name = 'user/creater_application.html'
    success_url = reverse_lazy('user:creater-update')

    def test_func(self) -> bool | None:
        if self.request.user.creater:
            return False
        return True

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        return redirect(reverse_lazy('user:creater-update'))

    def form_valid(self, form):
        form.instance.user_object = self.request.user
        return super().form_valid(form)
    
class CreaterUpdateView(mixins.LoginRequiredMixin, mixins.UserPassesTestMixin, generic.UpdateView):
    model = models.Creater
    form_class = forms.CreaterForm
    template_name = 'user/creater_update.html'
    success_url = reverse_lazy('user:creater-update')

    def get_object(self, queryset=None):
        return self.request.user.creater

    def test_func(self) -> bool | None:
        if self.request.user.creater:
            return True
        return False

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return super().handle_no_permission()
        return redirect('user:creater-application')
