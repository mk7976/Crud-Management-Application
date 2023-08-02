from django.shortcuts import render, redirect
from .models import Information


# Create your views here.
def Insertpage(request):
    return render(request, 'insert.html')


def Insertdata(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    passion = request.POST.get('passion')
    if len(name) > 0 and len(email) > 0:
        user = Information.objects.create(Name=name, Email=email, Contact=contact, Passion=passion)
        return redirect('Showdata')

    else:
        return render(request,'insert.html',{'a':"Bad Credentials"})


def Showdata(request):
    all_data = Information.objects.all()
    return render(request, 'show.html', {'key1': all_data})


def Editpage(request, pk):
    data = Information.objects.get(id=pk)
    return render(request, 'edit.html', {'key2': data})


def Updatedata(request, pk):
    u = Information.objects.get(id=pk)
    u.Name = request.POST.get('name')
    u.Email = request.POST.get('email')
    u.Contact = request.POST.get('contact')
    u.Passion = request.POST.get('passion')
    u.save()
    return redirect('Showdata')


def Deletedata(request, pk):
    data1 = Information.objects.get(id=pk)
    data1.delete()
    return redirect('Showdata')
