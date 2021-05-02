from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from music.models import Music

def music(request):
    music = Music.objects.all()
    return render(request, 'music/music.html', {'music' : music})

def author(request):
    author = "Jeon-Yongho"
    return render(request, 'music/author.html', {'author' : author})


def list_musics(request):
    members = Music.objects.all()
    return render(request, 'music/list_music.html', {'members' : members})


from music.forms import MusicForm


def create_music(request):
    form = MusicForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_music')

    return render(request, 'music/music_form.html', {'form': form})


def update_music(request, id):
    member = Music.objects.get(id=id)
    form = MusicForm(request.POST or None, instance=member)

    if form.is_valid():
        form.save()
        return redirect('list_members')

    return render(request, 'music/music_form.html', {'form': form, 'member': member})


def delete_music(request, id):
    member = Music.objects.get(id=id)

    if request.method == 'POST':
        member.delete()
        return redirect('list_members')

    return render(request, 'msuc/music_delete_confirm.html', {'member': member})





