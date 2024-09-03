from django.shortcuts import render, redirect
from django.contrib.auth import login
from . forms import SignUpForm

# Create your views here.

def frontpage(request):
    return render (request, 'core/base.html')


def Signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            user=form.save()

            login(request, user)

            return redirect('base.html')
    else:
        form=SignUpForm()

    return render(request, 'core/signup.html', {'form': form})