from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect  


def homePage(request):
    return render(request, 'home.html')

def submitform(request):
     
        return HttpResponse(request)
    
    
def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "about.html", {'output': output})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def course(request):
    return HttpResponse("<h1>Course List</h1>")

def courseDetails(request, courseid):
    return HttpResponse(f"<h1>Details of Course ID: {courseid}</h1>")  

# def submit_contact(request):
#     num1 = request.GET.get('num1', 0)  # Default to 0 if num1 is not provided
#     num2 = request.GET.get('num2', 0)  # Default to 0 if num2 is not provided

#     try:
#         # Perform your desired operation (e.g., addition)
#         result = int(num1) + int(num2)
#     except ValueError:
#         result = "Invalid input"

#     return render(request, 'userform.html', {'output': result})

def userform(request):
    finalans = 0
    data={}
    try:
        if request.method== "POST":
        # n1= request.GET['num1']
        # n2 = request.GET['num2']
         n1= (request.POST.get('num1'))
        n2 = (request.POST.get('num2') ) 
        finalans = int(n1) + int(n2)
        data={
            'n1': n1,
            'n2': n2,
            'output' :finalans
        }
        url="/about/?output={}".format(finalans)
        
        return HttpResponseRedirect(url)
    
    except:
        pass
        
    return render(request, "userform.html", data)