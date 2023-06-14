from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import ListaModels
from .forms import ListaForm


def Chamada(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)
        if form.is_valid():
            aluno = form.data['aluno']
            professor = form.data['professor']          

            form.save()

        return redirect('Listar')

    else:
        form = ListaForm
        return render(request, 'chamada.html', {'form': form})


def Listar(request):
    
    presenca = ListaModels.objects.all()
    
    context = {'ListarPresenca': presenca}

    return render(request, 'listar.html', context)
