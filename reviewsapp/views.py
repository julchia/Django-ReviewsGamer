import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from reviewsapp.models import Reviews
from reviewsapp.forms import ReviewForm, RegisterForm

# Create your views here.

def index(request):
    if request.GET.get('search'):
        query = request.GET.get('search')
        query_result = Reviews.objects.filter(game_name__icontains=query).values_list
        return render(request, 'reviewsapp/search.html', {'query_result': query_result, 'query': query})
    else:
        return render(request, 'reviewsapp/index.html')

def reviews(request):
    reviews = Reviews.objects.all()
    return render(request, 'reviewsapp/reviews.html', {'reviews': reviews})

def aboutus(request):
    return render(request, 'reviewsapp/aboutus.html')

def upload_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            game_name = form.cleaned_data['game_name']
            plataform = form.cleaned_data['plataform']
            genre = form.cleaned_data['genre']
            release_year = form.cleaned_data['release_year']
            review = form.cleaned_data['review']
            score = form.cleaned_data['score']
            cover = form.cleaned_data['cover']

            newrev = Reviews(game_name=game_name, plataform=plataform, genre=genre, 
                            release_year=release_year, review=review, score=score, cover=cover)
            newrev.save()
            return redirect('reviews')
    else:
        form = ReviewForm()
    return render(request, 'reviewsapp/upload.html', {'form': form})         

class UserRegister(CreateView):
    model = User
    template_name = 'reviewsapp/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index') 

class SearchReview(View):
    def get(self, request):
        if request.is_ajax:
            query = request.GET.get('term', '')
            query_result = Reviews.objects.filter(game_name__icontains=query)
            games = []
            for game in query_result:
                data = {}
                data['label'] = game.game_name
                games.append(data)
            data_json = json.dumps(games)
        else:
            data_json = "fallo"
        mimetype = "application/json"
        return HttpResponse(data_json, mimetype)                                        