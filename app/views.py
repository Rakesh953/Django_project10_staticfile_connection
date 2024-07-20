from django.shortcuts import render

# Create your views here.
def static_file_connection(request):
    return render(request,'static_file_connection.html')

