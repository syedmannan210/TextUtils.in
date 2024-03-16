#I've created this file myself
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # params={'name':'Syed','place':'Japan'}
    return render(request,"index.html")#,params)
#     return HttpResponse('''<ul>
#   <li><a href="https://www.youtube.com/">Youtube</a></li>
#   <li><a href="https://anitaku.to/home.html">Anime</a></li>
#   <li><a href="https://cineb.rs/">Movies</a></li>
# </ul>''')
def about(request):
    file=open("template/about.html","r")
    return HttpResponse(file.read())
def analyzetext(request):
    #Get the text
    txt=request.POST.get('text','default')
    #Get checkbox values
    capitalize = request.POST.get('capitalize', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    rempunc=request.POST.get('rempunc', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(capitalize)
    print(txt)
    #Analyze the text by checking which check box is on
    if capitalize=="on":
        analyzed=txt.title()
        params={'purpose':'Capitalize','analyzedtext':analyzed}
        # return render(request,'analyze.html',params)
        txt=analyzed
    if fullcaps=="on":
        analyzed=txt.upper()
        params = {'purpose': 'UPPERCASE', 'analyzedtext': analyzed}
        # return render(request, 'analyze.html', params)
        txt=analyzed
    if rempunc=="on":
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for char in txt:
            if char not in punc:
                analyzed=analyzed+char

        params = {'purpose': 'Punctuation Removed', 'analyzedtext': analyzed}
        # return render(request, 'analyze.html', params)
        txt=analyzed
    if charcount=="on":
        analyzed=len(txt)-1
        params = {'purpose': 'Number of characters are:', 'analyzedtext': analyzed}
        # return render(request, 'analyze.html', params)
        # txt=analyzed
    if (charcount=="off" and rempunc=="off" and fullcaps=="off" and capitalize=="off"):
        return HttpResponse("Error! Please select checkbox")
    return render(request, 'analyze.html', params)