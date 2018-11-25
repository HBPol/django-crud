from django.shortcuts import render, redirect
from django.conf import settings
from crudapp.models import Member, User
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crudapp/index.html', context)

def create(request):
    if request.method == "POST":
        member = Member(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            friendname_id=request.POST['friendname'],
            # Adding the get method ensures that if variable is empty, an empty value is assigned to 'file'
            file = request.FILES.get('file', ''),
            )
        member.save()
        return redirect('index')
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
    # Adding the get method ensures that if variable is empty, an empty value is assigned to 'file'
    member.file = request.FILES.get('file', '')
    member.save()
    return redirect('index')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('index')
    
