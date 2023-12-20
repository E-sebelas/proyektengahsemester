# urls.py (modul "report")
from django.urls import path
from . import views  # Impor tampilan yang sesuai
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('reportbook/', views.report_book, name='report_book'),
    path('simpanlaporan/', views.simpan_laporan, name='simpan_laporan'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'), 
    path('hapuslaporan/<int:id>/', views.hapus_laporan, name='hapus_laporan'),
    path('adminreport/', views.admin_report, name='admin_report'),
    path('reportresponse/<int:report_id>/', views.response_view, name='reportresponse'),
    path('json/<int:user_id>/', views.show_json_by_user, name='show_json_by_user'),
    path('simpanlaporanflutter/', views.simpan_laporan_flutter, name='simpan_laporan_flutter'),
    path('responselaporanflutter/<int:report_id>/', views.response_laporan_flutter, name='response_laporan_flutter'),
]

