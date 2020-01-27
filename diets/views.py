from django.shortcuts import render, redirect
from .models import Diet, Result
from .forms import DietForm, ResultForm


def list_diets(request):
    diets = Diet.objects.all()
    results = Result.objects.all()

    return render(request, 'diets.html', {'diets': diets, 'results': results})


def create_diet(request):
    form = DietForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_diets')

    return render(request, 'diets-form.html', {'form': form})


def create_result(request, id):
    form = ResultForm(request.POST or None)
    form.fields['diet_id'].initial = id

    if form.is_valid():
        form.save()
        return redirect('list_diets')

    return render(request, 'result-form.html', {'form': form})
