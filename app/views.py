from django.shortcuts import render, get_object_or_404
from .models import Vaga
from django.shortcuts import redirect
from .forms import VagaForm

# Página Inicial (Home) com destaque
def home(request):
    vagas_em_alta = Vaga.objects.filter(ativa=True)[:3]
    return render(request, 'app/home.html', {'vagas_em_alta': vagas_em_alta})

# Lista de Vagas com Pesquisa e Filtros
def lista_vagas(request):
    vagas = Vaga.objects.filter(ativa=True)
    
        
    # Filtro por modalidade
    modalidade = request.GET.get('modalidade')
    if modalidade:
        vagas = vagas.filter(modalidade=modalidade)

    return render(request, 'app/lista_vagas.html', {'vagas': vagas})

# Detalhes de uma Vaga
def detalhe_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    return render(request, 'app/detalhe_vaga.html', {'vaga': vaga})



# Painel de Gestão de Vagas
def painel_gestao(request):
    vagas = Vaga.objects.all()
    return render(request, 'app/painel_gestao.html', {'vagas': vagas})

# Criar Vaga
def criar_vaga(request):
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('painel_gestao')
    else:
        form = VagaForm()
    return render(request, 'app/form_vaga.html', {'form': form, 'titulo_pagina': 'Registar Nova Vaga'})

# Editar Vaga
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

# Eliminar Vaga (Apenas POST por segurança)
def eliminar_vaga(request, pk):
    vaga = get_object_or_404(Vaga, pk=pk)
    if request.method == 'POST':
        vaga.delete()
        return redirect('painel_gestao')
    return render(request, 'app/confirmar_eliminar.html', {'vaga': vaga})