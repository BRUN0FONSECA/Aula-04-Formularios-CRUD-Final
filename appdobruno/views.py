from django.shortcuts import render, redirect
from .models import Surfistas, Places, FSurfistas
# Create your views here.
def home(request):
  surf= Surfistas.objects.all()
  lugares= Places.objects.all()
  surff= FSurfistas.objects.all()
  print(surf)
  print(lugares)
  print(surff)
  return render(request,"home.html",context={"surfistas":surf,"Fsurf":surff,"lugares":lugares})

def create_surfista(request):
  if request.method=="POST":
    Surfistas.objects.create(
      title=request.POST["title"],
      nacionality=request.POST["nacionality"],
      WorldTitles=request.POST["WorldTitles"],
      stance=request.POST["stance"]
    )
    return redirect("home")
  return render(request,"formssurf.html",context={"action":"Adicionar"})

def create_f(request):
  if request.method=="POST":
    FSurfistas.objects.create(
      title=request.POST["title"],
      nacionality=request.POST["nacionality"],
      WorldTitles=request.POST["WorldTitles"],
      stance=request.POST["stance"]
    )
    return redirect("home")
  return render(request,"formsfsurf.html",context={"action":"Adicionar"})

def create_lugar(request):
  if request.method=="POST":
    Places.objects.create(
      title=request.POST["title"],
      country=request.POST["country"],
      InitialDate=request.POST["InitialDate"],
      FinalDate=request.POST["FinalDate"])
    return redirect("home")
  return render(request,"formsplaces.html",context={"action":"Adicionar"})

def update_surfista(request,id):
  surfista=Surfistas.objects.get(id = id)
  if request.method=="POST":
    surfista.title=request.POST["title"]
    surfista.nacionality=request.POST["nacionality"]
    surfista.WorldTitles=request.POST["WorldTitles"]
    surfista.stance=request.POST["stance"]
    surfista.save()
    return redirect("home")
  return render(request,"formssurf.html",context={"action":"Atualizar","surfista":surfista})


def update_fsurfista(request,id):
  fsurfista=FSurfistas.objects.get(id = id)
  if request.method=="POST":
    fsurfista.title=request.POST["title"]
    fsurfista.nacionality=request.POST["nacionality"]
    fsurfista.WorldTitles=request.POST["WorldTitles"]
    fsurfista.stance=request.POST["stance"]
    fsurfista.save()
    return redirect("home")
  return render(request,"formsfsurf.html",context={"action":"Atualizar","fsurfista":fsurfista})

def update_lugar(request,id):
  lugar=Places.objects.get(id = id)
  if request.method=="POST":
    lugar.title=request.POST["title"]
    lugar.country=request.POST["country"]
    lugar.InitialDate=request.POST["InitialDate"]
    lugar.FinalDate=request.POST["FinalDate"]
    lugar.save()
    return redirect("home")
  return render(request,"formsplaces.html",context={"action":"Atualizar","lugar":lugar})

def delete_surfista(request,id):
  surfista=Surfistas.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      surfista.delete()
    
    return redirect("home")
  return render(request,"are_you_sure_surfista.html",context={"surfista":surfista})

def delete_fsurfista(request,id):
  fsurfista=FSurfistas.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      fsurfista.delete()
    
    return redirect("home")
  return render(request,"are_you_sure_fsurfista.html",context={"fsurfista":fsurfista})

def delete_lugar(request,id):
  lugar=Places.objects.get(id = id)
  if request.method=="POST":
    if "confirm" in request.POST:
      lugar.delete()
    return redirect("home")
  return render(request,"are_you_sure_places.html",context={"lugar":lugar})