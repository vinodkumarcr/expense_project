from django.shortcuts import render,get_object_or_404,HttpResponseRedirect

from .models import Expense,Total
from .forms import FormView
from django.views.generic import TemplateView

def index(request):
    return render(request,'index.html')


def main(request):
    Tabs=Expense.objects.select_for_update(request)
    some=Total.objects
    return render(request,'main.html',{'Tabs':Tabs,'totals':some})

def add(request):
    form=FormView()
    if request.method=='POST':
            form=FormView(request.POST)
            if form.is_valid():
                form.save()
                amount=str(form.cleaned_data['Money'])
                return HttpResponseRedirect("/main/")

    return render(request,'add.html',{'form':form})
