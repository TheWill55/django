from django.shortcuts import render, redirect
from .forms import EscolhaNumeroForm

def pagina_inicial(request):
    return render(request, 'sorteio/pagina_inicial.html')

def escolher_numero(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = EscolhaNumeroForm(request.POST)
            if form.is_valid():
                numero = form.save(commit=False)
                numero.usuario = request.user
                numero.save()
                return redirect('página_de_sucesso')
        else:
            return redirect('login')  # Redirecionar para a página de login se o usuário não estiver autenticado
    else:
        form = EscolhaNumeroForm()
    
    return render(request, 'sorteio/escolher_numero.html', {'form': form})