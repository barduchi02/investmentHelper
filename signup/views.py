from django.shortcuts import render
from .forms import UserForm


# Create your views here.


def index(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()
            return render(request, 'signup/index.html', {'form': user_form, 'message': 'Usuário criado com sucesso!'})
        else:
            return render(request, 'signup/index.html', {'form': user_form})
    else:
        user_form = UserForm()
        return render(request, 'signup/index.html', {'form': user_form})