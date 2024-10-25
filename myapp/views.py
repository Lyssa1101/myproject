from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MyModel
from .forms import MyModelForm  # Assume we'll create a form for model data

# Home View (GET)
def home(request):
    return render(request, 'home.html')

# Form View (GET for form display, POST for form submission)
def form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data_list')
    else:
        form = MyModelForm()
    return render(request, 'form.html', {'form': form})

# Data List View (GET)
def data_list(request):
    data = MyModel.objects.all()
    return render(request, 'data_list.html', {'data': data})

# Detail View (GET)
def detail_view(request, pk):
    item = get_object_or_404(MyModel, pk=pk)
    return render(request, 'detail.html', {'item': item})