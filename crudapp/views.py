from django.shortcuts import render, redirect
from django.conf import settings
from crudapp.models import Member, User
from django.core.files.storage import FileSystemStorage

def index(request):
    members = Member.objects.all()
    
    context = {'members': members}
    return render(request, 'crudapp/index.html', context)

def create(request):
    if request.method == "POST" and request.FILES['file']:
        member = Member(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            friendname_id=request.POST['friendname'],
            file = request.FILES['file'],
            )
        member.save()
        return redirect('/')
    else:
        # Send user to the empty form along with the list of users to populate the drop-down control
        friendslist = User.objects.all()
        context = {'friendslist': friendslist}
        return render(request, 'crudapp/create.html', context)

def edit(request, id):
    members = Member.objects.get(id=id)
    friendslist = User.objects.all()
    context = {'members': members, 'friendslist': friendslist}
    return render(request, 'crudapp/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.friendname_id = request.POST['friendname']
    member.save()
    return redirect('/crudapp/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crudapp/')
    
