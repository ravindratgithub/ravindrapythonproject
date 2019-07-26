from django.shortcuts import render
from .models import Admin,Employee,Categories,Userlogn
from django.views.generic import CreateView,UpdateView,DeleteView
def openIndex(request):
    qs=Categories.objects.all()
    return render(request,"index.html",{"data":qs})

def adminLogin(request):
     username= request.POST.get("username")
     password=request.POST.get("password")
     # a=Admin(username=username,password=password)
     # a.save()
     qs=Admin.objects.filter(username=username,password=password)
     if qs:
         return render(request,"adminHome.html",)
     else:
         return render(request,"admin.html",{"msg":"Invalid Admin"})

class CreateEmp(CreateView):
    template_name = "createemp.html"
    model = Employee
    fields = ('idno','name','branch','email','contactno','address','city','categoryid','password')
    success_url = "/viewemp/"

class UpdateEmployee(UpdateView):
    template_name = "updateemp.html"
    model = Employee
    fields = ('name','branch','email','contactno','address','city','categoryid','password')
    success_url = '/viewemp/'

class DeleteEmployee(DeleteView):
    model = Employee
    success_url = '/viewemp/'

class AddCategories(CreateView):
    template_name = "addcategories.html"

    model = Categories
    fields = ('categoriesID','categoriesNAME','description')
    success_url = "/viewcategories/"

class UpdateCategories(UpdateView):
    template_name = "updatecategories.html"
    model = Categories
    fields = ('categoriesNAME','description')
    success_url = "/viewcategories/"

class DeleteCategories(DeleteView):
    model = Categories
    success_url = "/viewcategories/"

def changePassword(request):
    idno=request.POST.get("idno")
    qs=Employee.objects.filter(idno=idno)
    return render(request,"changepass.html",{"data":qs})

def change(request):
    old = request.POST.get("oldpass")
    new = request.POST.get("newpass")
    confirm = request.POST.get("confirmpass")
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    branch=request.POST.get("t3")
    email=request.POST.get("t4")
    cno=request.POST.get("t5")
    address=request.POST.get("t6")
    city=request.POST.get("t7")
    cat=request.POST.get("t8")
    pas=request.POST.get("t9")
    if old == pas and new == confirm:
        Employee(idno=idno,name=name,branch=branch,email=email,contactno=cno,address=address,city=city,categoryid=cat,password=new).save()
        return render(request, "changepassword.html", {"msg": "Password Changed Successfully"})
    else:
        return render(request, "changepassword.html", {"error": "Password Does Not Match"})

def employeeLogin(request):
    idno=request.POST.get("idno")
    password=request.POST.get("password")
    qs=Employee.objects.filter(idno=idno,password=password)
    if not qs:
        return render(request,"emplog.html",{"msg":"Invalid User"})
    else:
        return render(request,"empHome.html")

def userLogin(request):
    idno=request.POST.get("idno")
    password=request.POST.get("password")
    qs=Userlogn.objects.filter(userId=idno,password=password)
    print(qs)
    if qs:
        return render(request, "userHome.html",{"data":qs})
    else:
        return render(request, "userlog.html", {"msg": "Invalid User"})