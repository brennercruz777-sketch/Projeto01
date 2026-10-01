from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vaga
from .forms import VagaForm

# --- VIEWS PÚBLICAS ---

def home(request):
    vagas_em_alta = Vaga.objects.filter(ativa=True)[:3]
    return render(request, 'app/home.html', {'vagas_em_alta': vagas_em_alta})

def lista_vagas(request):
    vagas = Vaga.objects.filter(ativa=True)
    modalidade = request.GET.get('modalidade')
    if modalidade:
        vagas = vagas.filter(modalidade=modalidade)
    return render(request, 'app/lista_vagas.html', {'vagas': vagas})


# --- VIEWS PROTEGIDAS (REQUEREM LOGIN) ---

@login_required
def painel_gestao(request):
    vagas = Vaga.objects.all()
    return render(request, 'app/painel_gestao.html', {'vagas': vagas})

@login_required
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel_gestao')
    else:
        form = VagaForm()
    return render(request, 'app/form_vaga.html', {'form': form, 'titulo_pagina': 'Registar Nova Vaga'})

@login_required
def editar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('painel_gestao')
    else:
        form = VagaForm(instance=vaga)
    return render(request, 'app/form_vaga.html', {'form': form, 'titulo_pagina': 'Editar Vaga'})

@login_required
def eliminar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        vaga.delete()
        return redirect('painel_gestao')
    return render(request, 'app/confirmar_eliminar.html', {'vaga': vaga})

@login_required
def perfil(request):
    return render(request, 'app/perfil.html')

def detalhe_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    return render(request, 'app/detalhe_vaga.html', {'vaga': vaga})