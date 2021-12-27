from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CsvForm
from .models import Csv
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage
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
            # myfile = form.cleaned_data['myfile']
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


###########################################################################################
#####https://stackoverflow.com/questions/62912039/uploading-csv-file-django-using-a-form#####################################################################################

import csv
def save_new_students_from_csv(file_path):
    # do try catch accordingly
    # open csv file, read lines
    with open(file_path, 'r') as fp:
        students = csv.reader(fp, delimiter=',')
        row = 0
        for student in students:
            if row==0:
                headers = student
                row = row + 1
            else:
                # create a dictionary of student details
                new_student_details = {}
                for i in range(len(headers)):
                    new_student_details[headers[i]] = student[i]

                # for the foreign key field current_class in Student you should get the object first and reassign the value to the key
                new_student_details['current_class'] = StudentClass.objects.get() # get the record according to value which is stored in db and csv file

                # create an instance of Student model
                new_student = Student()
                new_student.__dict__.update(new_student_details)
                new_student.save()
                row = row + 1
        fp.close()
##--------------------------------------------------
def uploadcsv(request):
    if request.method == 'GET':
        form = StudentBulkUploadForm()
        return render(request, 'students/students_upload.html', {'form':form})

    # If not GET method then proceed
    try:
        form = StudentBulkUploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'File is not CSV type')
                return redirect('students:student-upload')
            # If file is too large
            if csv_file.multiple_chunks():
                messages.error(request, 'Uploaded file is too big (%.2f MB)' %(csv_file.size(1000*1000),))
                return redirect('students:student-upload')

            # save and upload file
            form.save()

            # get the path of the file saved in the server
            file_path = os.path.join(BASE_DIR, form.csv_file.url)

            # a function to read the file contents and save the student details
            save_new_students_from_csv(file_path)
            # do try catch if necessary

    except Exception as e:
        logging.getLogger('error_logger').error('Unable to upload file. ' + repr(e))
        messages.error(request, 'Unable to upload file. ' + repr(e))
    return redirect('students:student-upload')

###################################################################################################################