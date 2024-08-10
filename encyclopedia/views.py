from django.shortcuts import render
from django.http import HttpResponse
from markdown import Markdown
from django.urls import reverse
from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    d=title
    mark=Markdown()
    c=util.list_entries()
    if d in c:
        return render(request,"encyclopedia/title.html",{
        "title":d,
        "content":mark.convert(util.get_entry(d))
    })
    else:
        return render(request, "encyclopedia/error.html",{
            "entries":c
        })
    
def search(request):
    if request.method=="POST":
        look=request.POST['q']
        mark=Markdown()
        c=util.list_entries()
        if look in c:
            return render(request,"encyclopedia/title.html",{
            "title":look,
            "content":mark.convert(util.get_entry(look))
    })
        else:
            entries=util.list_entries()
            recomend=[]
            for entry in entries:
                if look.lower() in entry.lower():
                    recomend.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recomend":recomend
            })

def newpage(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content'] 
        c=util.list_entries()
        util.save_entry(title,content)
    return render(request,"encyclopedia/newpage.html")

def edit(request):
    if request.method=="POST":
        title= request.POST["entry_title"]
        content=util.get_entry(title)
        return render(request,"encyclopedia/edit.html",{
            "title":title,
            "content":content
        })
    
def save_edit(request):
    if request.method=="POST":
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        mark=Markdown()
        return render(request,"encyclopedia/title.html",{
            "title":title,
            "content":mark.convert(util.get_entry(title))
    })
    
def rand(request):
    Entry=util.list_entries()
    rand_entry= random.choice(Entry)
    mark=Markdown()
    return render(request,"encyclopedia/title.html",{
            "title":title,
            "content":mark.convert(util.get_entry(rand_entry))
    })
