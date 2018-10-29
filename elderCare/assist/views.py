from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Section
from .forms import SectionForm

# Create your views here.
def home(request):
	sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'assist/home.html', {'sections': sections})

def doc_list(request):
    sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'assist/doc_list.html', {'sections': sections})

def doc_detail(request, pk):
    sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    section = get_object_or_404(Section, pk=pk)
    return render(request, 'assist/doc_detail.html', {'section': section, 'sections' : sections})

def doc_new(request):
    sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.author = request.user
            section.published_date = timezone.now()
            section.save()
            return redirect('doc_detail', pk=section.pk)
    else:
        form = SectionForm()
    return render(request, 'assist/doc_edit.html', {'form': form, 'sections' : sections})

def doc_edit(request, pk):
    section = get_object_or_404(Section, pk=pk)
    sections = Section.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if request.method == "POST":
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            section = form.save(commit=False)
            section.author = request.user
            section.published_date = timezone.now()
            section.save()
            return redirect('doc_detail', pk=section.pk)
    else:
        form = SectionForm(instance=section)
    return render(request, 'assist/doc_edit.html', {'form': form, 'sections' : sections})