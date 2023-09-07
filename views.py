from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    param={'name':'kashish','place':'India'}
    return render(request,'Index2.html',param)
# def about(request):
    # return HttpResponse("This is the about page of coffee website\n<a href='http://127.0.0.1:8000/'><b>HOME</b></a>")
def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get("fullcaps","off")
    newlineremover=request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("extraspaceremover","off")
    charactercounter=request.POST.get("charactercounter","off")
    # print(removepunc)
    # print(djtext)
    # analyzed=""
    # punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removing Punctuations','analyzed_text':analyzed}
        return render(request,"Analyze.html",params)
        # djtext=analyzed
    elif fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        return render(request,'Analyze.html',params)
        # djtext = analyzed
    elif newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!='\r':
                analyzed+=char
            else:
                print("No")
        params={'purpose':'New Lines Removed','analyzed_text':analyzed}
        return render(request,'Analyze.html',params)
        # djtext = analyzed
    elif extraspaceremover=="on":
        analyzed=""
        # for char in djtext:
        #     if char!=' ':
        #         analyzed+=char
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params={'purpose':'Extra Spaces Removed','analyzed_text':analyzed}
        return render(request,'Analyze.html',params)
        # djtext = analyzed
    elif charactercounter=="on":
        analyzed=0
        for char in djtext:
            if char!=" ":
                analyzed+=1
        params={'purpose':'Character Counter','analyzed_text':analyzed}
        return render(request,'Analyze.html',params)
        # djtext = analyzed


    elif (removepunc!="on" and newlineremover!="on" and extraspaceremover!="on"
    and charactercounter!="on" and fullcaps!="on"):
        return HttpResponse("Please Select an operation")
    # return render(request,'Analyze.html',params)


