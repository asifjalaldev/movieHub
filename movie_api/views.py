from django.shortcuts import render, HttpResponse

# Create your views here.
def movie_list(request):
    return HttpResponse('testing movie list')
def movie_detail(request, pk):
    return HttpResponse(f'testing movie detail {pk}')