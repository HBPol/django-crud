from django.shortcuts import render, redirect
from crudapp.models import Member
from requests.api import request

def index(request):
    members = Member.object.all()
    context = {'members': members}
    return render(request, 'crudapp/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crudapp/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lasttname = request.POST['lastname']
    member.save()
    return redirect('/crudapp/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crudapp/')
    
