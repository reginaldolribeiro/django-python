from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import *


class CarroForm(ModelForm):
    class Meta:
        model = Carro
        fields = ['modelo', 'marca', 'ano', 'valor', 'data_cadastro']

def cadastrar_carro(request):
    template_name='carro_form.html'
    form = CarroForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('carro_list')    
    return render(request, template_name, context)

def listar_carro(request):
    query = request.GET.get("busca")
    if query:
        carro = Carro.objects.filter(modelo__iexact=query)
    else:        
        carro = Carro.objects.all()
    template_name='carro_list.html'
    context = {
        'lista': carro
    }
    return render(request, template_name, context)
    
def editar_carro(request,pk):
    carro = get_object_or_404(Carro, pk=pk)
    template_name='carro_form.html'    
    if request.method == 'POST':
        form = CarroForm(request.POST, instance=carro)
        if form.is_valid():
            form.save()
            return redirect('carro_list')
    else:
        form = CarroForm(instance=carro)        
    context = {
        'form': form
    }
    return render(request, template_name, context)

def deletar_carro(request, pk):
    template_name = 'carro_delete.html'
    #carro = get_object_or_404(Carro, pk=pk)
    carro = Carro.objects.get(pk=pk)
    if request.method == 'POST':
        carro.delete()
        return redirect('carro_list')
    context = {
        'carro': carro
    }
    return render(request, template_name, context)