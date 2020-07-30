from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import Markdown
from . import util
from random import choice

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request,entry):
    try:
        content = util.get_entry(entry)  
        markdowner = Markdown()
        content = markdowner.convert(content)
        return render(request, "encyclopedia/page.html", {
            "title": entry,
            "content": content
        })
    except:
        return render(request, "encyclopedia/error.html",{
            "message": "Page Does Not Exist!!Lalaaaaa"
        })

def edit(request,title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        "title": title,
        "content": content
    })

def save(request,title):
    if title != request.POST["title"]:
        util.del_entry(title)
    content = request.POST["new_content"]
    title = request.POST["title"]
    util.save_entry( title , content )
    return HttpResponseRedirect(reverse(("page"),args=(title,)))

def random_page(request):
    entries = util.list_entries()
    entry = choice(entries)
    return HttpResponseRedirect(reverse(("page"),args=(entry,)))

def create(request):
    return render(request, "encyclopedia/create.html",{
        "title": "Title",
        "content":"Write your Content here"
    })

def delete(request,title):
    util.del_entry(title)
    return HttpResponseRedirect(reverse(("index")))

def search(request):
    string_ = request.POST["string_"]
    titles = util.list_entries()
    entries = []
    for i in titles: 
        if i.lower().find(string_.lower()) == -1: 
            pass 
        else: 
            entries.append(i)
    return render(request,"encyclopedia/search.html",{
        "string_": string_,
        "entries": entries
    })        





