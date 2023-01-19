from django.shortcuts import render
from gameblog.models import Users,Articles,Games

# Create your views here.

def index(request):
    return render(request,'index.html');

def home(request,username):
    user=Users.objects.filter(username=username).first()
    if not user:
        return render(request,'not_found.html')
    return render(request,'personal.html',{'user':user})

def article(request,articleid):
    article=Articles.objects.filter(article_id=articleid).first()
    if not article:
        return render(request,'not_found.html')
    return render(request,'detail.html',{'article':article})

def game(request,gameid):
    game=Games.objects.filter(game_id=gameid).first()
    if not game:
        return render(request,'not_found.html')
    return render(request,'game.html',{'game':game})

def search(request):
    pass

def edit(request):
    pass

def catalog(request):
    pass