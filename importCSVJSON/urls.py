from django.contrib import admin
from django.urls import path
from importCSVJSON import views
# from importCSVJSON import views as uploader_views
urlpatterns = [
    path('importCSV/',views.importCSV,name='importCSV'),
    path('dataanalysis/',views.data_analysis,name='dataanalysis'),
    path('fileupload/', views.UploadView, name='fileupload'),
    # path('fileupload/', UploadView.as_view(), name='fileupload'),


]