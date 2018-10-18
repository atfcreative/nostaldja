from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Decade, Fad
from .forms import DecadeForm, FadForm

# Create your views here.

########DECADE ###############################
# Show decades
def decade_list(request):
    decades = Decade.objects.all()
    return render(request, 'nostaldja/decade_list.html', {'decades': decades})

# Post Decades
def decade_detail(request, id):
    decade = Decade.objects.get(id = id)
    return render(request, 'nostaldja/decade_detail.html', {'decade': decade})

# Create decades
def decade_create(request):
    if request.method == 'POST':
        form = DecadeForm(request.POST)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', id = decade.id)
    else:
      form = DecadeForm()
    return render(request, 'nostaldja/decade_form.html', {'form': form})

# Edit Decades
def decade_edit(request, id):
    decade = Decade.objects.get(id = id)
    if request.method == "POST":
        form = DecadeForm(request.POST, instance = decade)
        if form.is_valid():
            decade = form.save()
            return redirect('decade_detail', id = decade.id)
    else:
        form = DecadeForm(instance = decade)
    return render(request, 'nostaldja/decade_form.html', {'form': form})

# delete Decades
def decade_delete(request, id):
  if request.method == 'POST':
    Decade.objects.get(id = id).delete()
  return redirect('decade_list')

##########FADS ###############################

def fad_list(request):
  fads = Fad.objects.all()
  return render(request, 'nostaldja/fad_list.html', {'fads': fads})

def fad_detail(request, id):
  fad = Fad.objects.get(id = id)
  return render(request, 'nostaldja/fad_detail.html', {'fad': fad})

def fad_create(request):
  if request.method == 'POST':
    form = FadForm(request.POST)
    if form.is_valid():
      fad = form.save()
      return redirect('fad_detail', id = fad.id)
  else:
    form = FadForm()
  return render(request, 'nostaldja/fad_form.html', {'form': form})

def fad_edit(request, id):
  fad = Fad.objects.get(id = id)
  if request.method == 'POST':
    form = FadForm(request.POST, instance = fad)
    if form.is_valid():
      fad = form.save()
      return redirect('fad_detail', id = fad.id)
  else:
    form = FadForm(instance = fad)
  return render(request, 'nostaldja/fad_form.html', {'form': form})

def fad_delete(request, id):
  if request.method == 'POST':
    Fad.objects.get(id = id).delete()
  return redirect('fad_list')
