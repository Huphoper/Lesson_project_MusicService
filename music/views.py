from django.shortcuts import render
from django.views import View
from music.models import User, Song
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class startmusic(View):
    def get(self, request, id, *args, **kwargs):
        try:
            son = Song.objects.get(id=id)
        except Song.DoesNotExist:
            raise Http404

        context = {'songcount': Song.objects.count(), 'song': son}
        return render(request, 'song.html', context=context)


class listmusic(View):
    def get(self, request, *args, **kwargs):
        context = {'songcount': Song.objects.count(), 'songs': Song.objects.all()}
        return render(request, 'index.html', context=context)

    def post(self, request, *args, **kwargs):
        if request.POST.get("reset"):
            Song.objects.all().delete()
            User.objects.all().delete()

            userk = User.objects.create_user("Duke_is407", "mail@mail.com", "12536")
            newsound = Song.objects.create(title="Never-Gonna-Give-You-Up", artist="Rick-Astley",
                                           path_to_file="Rick-Astley-Never-Gonna-Give-You-Up.mp3")
            newsound.favorite_by.add(userk)
            return HttpResponseRedirect(reverse('main'))


class add_to_favorites(View):
    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        song_id = request.POST.get("song_id")
        try:
            son = Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            raise Http404
        User.objects.all().delete()
        userk = User.objects.create_user("Duke_is407", "mail@mail.com", "12536")
        son.favorite_by.add(userk)
        son.save()
        return HttpResponseRedirect(reverse('song', args=[song_id]))


class addmusic(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'addmusic.html', context=context)

    def post(self, request, *args, **kwargs):
        title = request.POST['title']
        artist = request.POST['artist']
        path_to_file = request.POST['path_to_file']
        if title and artist and path_to_file:
            if Song.objects.filter(title=title, artist=artist).count() != 0:
                context = {'info': 'Такая песня уже есть в библиотеке!'}
                return render(request, 'addmusic.html', context=context)
            else:
                Song.objects.create(title=title, artist=artist, path_to_file=path_to_file)
                return HttpResponseRedirect(reverse('main'))
        else:
            context = {'info': 'Не все поля заполнены!'}
            return render(request, 'addmusic.html', context=context)
