from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=='POST':
        number1=int(request.POST.get('txt_num1'))
        number2=int(request.POST.get('txt_num2'))
        sum=number1+number2
        return render(request,'Basics/Sum.html',{'res':sum})
    else:
        return render(request,'Basics/Sum.html')
    
def Largest(request):
    if request.method=='POST':
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        if (a > b):
            Largest = a 
            return render(request,'Basics/Largest.html',{'res':Largest})
        else:
             Largest = b 
             return render(request,'Basics/Largest.html',{'res':Largest})
    else:
        return render(request,'Basics/Largest.html')

def Calclator(request):
    if request.method=='POST':
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        op=request.POST.get('btn')
        if op=='+':
            result=a+b
        elif op=='-':
            result=a-b
        elif op=='*':
            result=a*b
        elif op=='/':
            result=a/b
        return render(request,'Basics/Calculator.html',{'res':result})
    else:
        return render(request,'Basics/Calculator.html')