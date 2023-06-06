from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView
from django.contrib import messages

from usuario.forms import CustomUsuarioCreateForm


class CadastroView(CreateView):
    model = get_user_model()
    form_class = CustomUsuarioCreateForm
    template_name = 'registration/cadastro.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })
