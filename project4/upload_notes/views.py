from django.shortcuts import render, redirect
from .forms import NoteForm
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'upload_notes/notes_list.html', {'notes': notes})

@login_required
def note_upload(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'upload_notes/note_form.html', {'form': form})
