from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    comments = Comment.objects.all()[:4] 

    context = {'comments': comments}
    return render(request, 'home.html', context)

def loginPage(request):
    page = 'login' 

    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'GET':

        context = {'page': page}
        return render(request, 'login.html', context)
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.add_message(request, constants.ERROR, 'Usuário não foi encontrado.')    

        user = authenticate(request, username=username, password=password)    

        if user:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou senha estão incorretos.')

def registro(request):
    form = UserCreationForm()

    if request.method == 'GET':

        context = {'form':form}
        return render(request, 'login.html', context)
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, request.user)
            return redirect('home')
        else:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou senha inválidos.')
            return redirect('registro')
        
def logoutPage(request):
    logout(request)

    return redirect('home')            

login_required()
def newComment(request):
    if request.method == 'POST':
        comment = request.POST.get('body')
        comment = Comment.objects.create(
            user = request.user,
            body = comment
        )

        messages.add_message(request, constants.SUCCESS, 'Comentário criado!')
        return redirect('/')

def deleteComment(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'GET':
        
        context = {'comment': comment}
        return render(request, 'delete.html', context)
    
    elif request.method == 'POST':
        comment.delete()

        messages.add_message(request, constants.INFO, 'Comentário Apagado!')
        return redirect('/')
    
def updateComment(request, id):
    comment = Comment.objects.get(id=id)    
    if request.method == 'GET':

        context = {'comment':comment}
        return render(request, 'update.html', context)
    
    elif request.method == 'POST':     
        comment = request.POST.get('body')
        Comment.objects.filter(id=id).update(body=comment)

        messages.add_message(request, constants.SUCCESS, 'Comentário atualizado!')
        return redirect('/')

def detailComment(request, id):
    message = Comment.objects.get(id=id)      

    context = {'message':message}
    return render(request, 'detail_message.html', context)  

