from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login
from mainapp.forms import NovoUsuarioForm


class HomeView(TemplateView):
    template_name = 'mainapp/index.html'

def register(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        messages.error(request, "Falha no cadastro do usuário.")
    form = NovoUsuarioForm()
    context = {'form': form}
    return render(request, template_name='mainapp/register.html', context=context)