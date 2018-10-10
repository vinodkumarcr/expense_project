from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.http import HttpResponse
from .models import Expense,Total,Totals,Share
from .forms import FormView,ShareView
from django.views.generic import TemplateView
from django.db.models import Sum
from django.db.models import F

def index(request):
    return render(request,'index.html')


def main(request):
    Tabs=Expense.objects.all()
    num=[ ]
    su=[ ]
    tota=0
    for yes in Tabs:
        total=yes.Money
        totals=int(total)
        num.append(totals)
    for nums in num:
        tota+=nums
        su.append(tota)
    #print(su)

    some=Total.objects.only('Total_money')
    somes=list(some)
    totals=somes.pop()
    sharu=Share.objects.all()
    ok1=0
    oh=Share.objects.all()
    #print(len(oh))
    dictionary={'Tabs':Tabs,'totals':totals,'tota':tota,'share':sharu}
    if len(oh)!=0:
        hello=friend_share()
        #print(hello)
        #print(tota)
        tota+=hello[0]
        #print(ok1)
    else:
        hello=(0,0)

    di={'my_share':hello[0],'friends_share':hello[1],'tota':tota}
    dictionary.update(di)




    return render(request,'main.html',dictionary)
def add(request):
    rupees=0
    form=FormView()
    if request.method=='POST':
            form=FormView(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/main/")
    return render(request,'add.html',{'form':form})


def reset(request):
    tab=Expense.objects.all()
    tab.delete()
    tabs=Share.objects.all()
    tabs.delete()
    return HttpResponseRedirect("/main/")


def sharing(request):
    rupees=0
    form=ShareView()
    if request.method=='POST':
            form=ShareView(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/main/")
    return render(request,'sharing.html',{'form':form})

def friend_share():
    addm=0
    adds=0
    take=Share.objects.all()
    #print(take)
    for takes in take:
        if takes.Money!=None:
            x=takes.Money/takes.Count
            y_share = float("{0:.2f}".format(x))
            y=float(takes.Money)-y_share
            friends_share = float("{0:.2f}".format(y))
            #print(friends_share)
            #print(y_share)
        else:
            y_share=0
            friends_share=0
            return (0,0)


        addm+=y_share
        adds+=friends_share

    return (addm,adds)
