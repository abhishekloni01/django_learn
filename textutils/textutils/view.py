#Created by Abhishek

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse(''' <h1>Hello Abhishek</h1>
#                             <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">
#                             Code with harry django </a>''')
# def about(request):
#     return HttpResponse("""about abhishek  <br>
#                         <a href="/">Back</a>""")

def home(request):
    return render(request, 'indexnew.html')

# def capfirst(request):
#     print(request.GET.get('text'))
#     return HttpResponse('cap first')
#
# def charcount(request):
#     return HttpResponse("this is char count")
#
# def indexnew(request):
#     return render(request, 'indexnew.html')


def analysed(request):
    inp_text=request.GET.get('text', 'default')
    inp_check=request.GET.get('rmpunc', 'off')
    #inp_cap = request.GET.get('capitalize', 'off')
    #inp_rmexsp = request.GET.get('rmexspace', 'off')

    punctuation = ''' !@#$%^&*()-[]{}_;'.:"<>/~'''
    analyse = ""
    if inp_check=="on":
        for char in inp_text:
            if char not in punctuation:
                analyse += char

    # if inp_cap=='on':
    #     analyse= analyse.upper()

    # if inp_rmexsp == 'on':
    #     for index, ch in enumerate(analyse):
    #         if not(analyse[index] == ' ' and analyse[index+1] == ' '):
    #             analyse = ch



    else:
        analyse="cant remove punctuation: {}".format(inp_text)

    params={ 'purpose': 'removed punctuation', 'analysed_text': analyse}
    return render(request, 'analysed.html', params)



