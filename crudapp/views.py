from django.shortcuts import render, redirect
from django.conf import settings
from crudapp.models import Member, User, MyTestModel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from crudapp.forms import MyTestModelForm_01, MyTestModelForm_02

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

######### TESTING THE FORM CLASS - WITH THE FORM CLASS CREATED FROM SCRATCH ##################
def test_model_form_01(request):
    if request.method == 'POST':
        form = MyTestModelForm_01(request.POST)
        if form.is_valid():
            mytestmodel = MyTestModel(
                my_char = form.cleaned_data['my_char'],
                my_date = form.cleaned_data['my_date'],
                my_datetime = form.cleaned_data['my_datetime'],
                my_integer = form.cleaned_data['my_integer'],
                my_boolean = form.cleaned_data['my_boolean'],
                my_email = form.cleaned_data['my_email'],
                my_text = form.cleaned_data['my_text'],
                my_time = form.cleaned_data['my_time'],
                )
            mytestmodel.save()
            return redirect('index')
    else:
        form = MyTestModelForm_01()
    
    return render (request, 'crudapp/mytestmodelform.html', {'form_01': form})

#########           END           #################
    
######### TESTING THE FORM CLASS - BUILDING THE FORM FROM THE MODEL ##################
def test_model_form_02(request):
    if request.method == 'POST':
        form = MyTestModelForm_02(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MyTestModelForm_02()
    
    return render (request, 'crudapp/mytestmodelform.html', {'form_02': form})






##########           END           #################
