from django.shortcuts import render
from django.http import HttpResponse
from . models import postdb
from django.http import HttpResponseForbidden 
from .forms import postform,userregisterform
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout

# Create your views here.

def myhome(request):
    return render(request,'post1/myhome.html')

@login_required
def post_list(request):
    posts = postdb.objects.all()
    return render(request,'post1/myhome.html',{'posts':posts})

# def post_create(request):
#     if request.method == 'POST':
#       form = postform(request.POST,request.FILES)
#     if form.is_valid():
#           post = form.save(commit= False)
#           post.user = request.user
#           post.save()
#           return redirect('post_list')
    
#     else:
#         form = postform()
#     return render(request,'post_create.html',{'form':form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = postform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('post_list')  # change to your desired redirect
    else:
        form = postform()  # this was missing
    return render(request, 'post1/post_create.html', {'form': form})

@login_required
def post_edit(request,post_id):
    post =  get_object_or_404(postdb, pk = post_id)

    # if post.user != request.user:                 
    #     return HttpResponseForbidden("You are not allowed to edit this post.")  
    
    if request.method == 'POST':
      form = postform(request.POST,request.FILES,instance=post)
      if form.is_valid():
          post = form.save(commit= False)
          post.user = request.user
          post.save()
          return redirect('post_list')
    else:
         form = postform(instance=post)
    return render(request,'post1/post_edit.html',{'form':form})




@login_required
def post_delete(request,post_id):
    post = get_object_or_404(postdb, pk = post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,'post1/post_delete.html',{'post':post})







def register(request):
    if request.method == 'POST':
        form = userregisterform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('post_list')
    else:
        form = userregisterform()
    
    return render(request,'registration/register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # now correctly refers to Django's login
            return redirect('home')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'login.html')



# def logout(request):
#     logout(request)
#     return redirect('login')


