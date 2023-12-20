from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import DiaryEntryForm  

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful. You can now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'diary/dashboard.html', {'entries': entries})

@login_required
def add_entry(request):
    if request.method == "POST":
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Diary entry added successfully.')
            return redirect('dashboard')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/create_entry.html', {'form': form})

@login_required
def view_entries(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'diary/view_entries.html', {'entries': entries})

@login_required
def view_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    return render(request, 'diary/view_entry.html', {'entry': entry})

@login_required
def edit_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    if request.method == "POST":
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            messages.success(request, 'Diary entry updated successfully.')
            return redirect('dashboard')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/edit_entry.html', {'form': form})

@login_required
def delete_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id, user=request.user)
    if request.method == "POST":
        entry.delete()
        messages.success(request, 'Diary entry deleted successfully.')
        return redirect('dashboard')
    return render(request, 'diary/delete_entry.html')
