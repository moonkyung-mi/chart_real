from django.shortcuts import render
import json
from main.models import Fruit
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def db_save() :
    temp = Fruit(f_name='grape',value=170000)
    temp.save()

def db_load() :
    fin = []
    fin.append(list(Fruit.objects.values('f_name')))
    fin.append(list(Fruit.objects.values('value')))
    # print(list(fin))
    res_n = []
    res_v = []
    for f in fin :
        for temp in f :
            print(list(temp.keys())) 
            if list(temp.keys())[0] == 'f_name' :
                res_n.append(temp['f_name']) 
            else : 
                res_v.append(temp['value'])
    # print(res_n)
    # print(res_v)
    return res_n,res_v

def index(request):
    # db_save()
    line_lbl, line_val = db_load()
    contx_dic = {
        'main_line_lbl': line_lbl, #['apple','melon','orange','banana'],
        'main_line_val': line_val #[100000,60000,120000,18000],
                }
    result = json.dumps(contx_dic,ensure_ascii=False)
    print(result)
    context = {"result" : result }

    return render(request, 'main/index.html', context)

@csrf_exempt
def chart(request) :
    line_lbl, line_val = db_load()
    contx_dic = {
        'main_line_lbl': line_lbl, #['apple','melon','orange','banana'],
        'main_line_val': line_val #[100000,60000,120000,18000],
                }
    result = json.dumps(contx_dic,ensure_ascii=False)
    return HttpResponse(result,content_type="application/json")