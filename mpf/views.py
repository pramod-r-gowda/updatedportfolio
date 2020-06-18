from django.shortcuts import render

# Create your views here.
def homepage(request):
	name='Pramod R'
	context={'n':name}
	return render(request,'mpf/index.html',context)