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


def update_diet(request, id):
    diet = Diet.objects.get(id=id)
    form = DietForm(request.POST or None, instance=diet)

    if form.is_valid():
        form.save()
        return redirect('list_diets')

    return render(request, 'diets-form.html', {'form': form, 'diet': diet})


def update_result(request, id):
    result = Result.objects.get(id=id)
    form = ResultForm(request.POST or None, instance=result)

    if form.is_valid():
        form.save()
        return redirect('list_diets')

    return render(request, 'result-form.html', {'form': form, 'result': result})


def delete_diet(request, id):
    diet = Diet.objects.get(id=id)
    results = Result.objects.filter(diet_id=id)

    if request.method == 'POST':
        results.delete()
        diet.delete()
        return redirect('list_diets')

    return render(request, 'diet-confirm-delete.html', {'diet': diet})


def delete_result(request, id):
    result = Result.objects.get(id=id)

    if request.method == 'POST':
        result.delete()
        return redirect('list_diets')

    return render(request, 'result-confirm-delete.html', {'result': result})
