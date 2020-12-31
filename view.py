
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    remove = request.POST.get('removepunc', 'off')
    upper = request.POST.get('upper', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
   
    if remove == 'on':
        punctuations='''!@#$%^&*()_-=+[]{}:;"'<>?/'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params = {'purpose' : 'Removed Punctuation', 'analyzed_text': analyzed}
        # Analyze the text "About Website <a href='/' >back</a>"
        djtext=analyzed
        #return render(request,'analyze.html', params)
    if(upper=='on'):
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if( spaceremover=='on'):
        analyzed=""
        for i,char in enumerate(djtext):
            if not (djtext[i] == " " and djtext[i+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if(remove!='on' and upper!='on' and newlineremover !='on' and spaceremover!='on' ):
        return HttpResponse('Please select any operation')

    return render(request, 'analyze.html', params)
def exl(request):
    s = '''<h2>Navigation bar</h2><br>
        <a href='https://www.google.co.in/'>Google</a><br>
        <a href='https://www.facebook.com/'>Facebook</a>'''
    return HttpResponse(s)