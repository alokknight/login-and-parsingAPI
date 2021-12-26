from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CsvForm
from .models import Csv
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
# Create your views here.

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class UploadView(CreateView):
    model = Csv
    fields = ['file_name', ]
    success_url = reverse_lazy('fileupload')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Csv.objects.all()
        print(context)
        return context


# def importCSV(request):
#     form = CsvForm()
#     # if request.method=='POST':
#     #     form = CsvForm(request.POST or None, request.FILES or None)
#     #     # print(type(form))
#     #     if form.is_valid():
#     #         form.save()
#     #         print('form saved')
#     #     else:
#     #         print('invalid form')


#     # # if request.method == 'POST' and request.FILES["myfile"]:
#     # #     myfile = request.FILES["myfile"]
#     # #     print('\nWhat is `myfile`?')
#     # #     print(type(myfile))
#     #         # print(form)


#     #     # df=pd.read_csv('',sep=';')
#     #     # print(df)
#     #     # row_iter = df.iterrows()

#     #     # obj = csv.objects.get(activated = False)
#     #     # with open(obj.file_name.path , 'r') as f:
#     #     #     reader = Csv.reader(f)

#     #     #     for i in enumrate(reader):
#     #     #         if i==0:
#     #     #             pass
#     #     #         else:
#     #     #             row = "".join(row)
#     #     #             row = row.replace(";"," ")
#     #     #             row = row[1].upper()
#     #     #             obj.activated = True
#     #     #             obj.save()
#     #     context={'form': form }
#     #     print(context)
#     #     print("success")
#     #     # return redirect('/importCSVJSON/importCSV/')

#     return render(request, "importCSVJSON/importCSV.html",{'form':form})


def importCSV(request):
    form = CsvForm()
    if request.method == 'POST':
        form = Form_fieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('importCSVJSON/importCSV')
    context = {'form':form}
    return render(request,"importCSVJSON/importCSV.html",context)

def readcsv(request):
    df=pd.read_csv('form',sep=';')
    print(df)
    row_iter = df.iterrows()
    return JsonResponse({})

def data_analysis(request):
    print('Data analysis')
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        print('\nWhat is `myfile`?')
        print(type(myfile))

        print('\nDirectly accessing `myfile` gives nothing :(')
        print(type(str(myfile.read())))
        print(str(myfile.read()))

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print('\nHowever, when using FileSystemStorage...')
        print('\nReading filename: %s' % filename)
        print(type(fs.open(filename)))
        print(fs.open(filename))

        print('\nOpen and preview using pandas:')
        df = pd.read_csv(fs.open(filename))
        print(df)

        print('\nOr with CSV module:')
        with fs.open(filename, 'rt') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)

        print('Data analysis')
        r_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='r')))
        p_table = df.apply(lambda x: df.apply(lambda y: r_xor_p(x, y,
                                                                r_xor_p='p')))

        return render(request, 'importCSVJSON/data_analysis.html',
                      {'result_present': True,
                       'results': {'r_table': r_table.to_html(),
                                   'p_table': p_table.to_html()},
                       'df': df.to_html()})

    return render(request, 'importCSVJSON/data_analysis.html')
