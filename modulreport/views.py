# Dalam file views.py di modul "report"
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Report  # Import model Report
from django.contrib.auth.decorators import login_required  # Untuk mengharuskan pengguna masuk sebelum mengakses view
from django.template.defaultfilters import date  # Import filter date
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from .forms import ResponseForm
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
import json
from .models import Response  # Import the Response model from your app's models



def report_book(request):
    # Logika untuk halaman "Report Product" di sini
    laporan_list = Report.objects.filter(user=request.user)
    return render(request, 'mainreport.html', {'laporan_list': laporan_list})


@csrf_exempt
@login_required  # Menambahkan dekorator untuk memastikan pengguna masuk sebelum mengakses view
def simpan_laporan(request):
    if request.method == 'POST':
        # Mendapatkan data dari permintaan POST
        book_title = request.POST.get('book_title')
        issue_type = request.POST.get('issue_type')
        other_issue = request.POST.get('other_issue', '')
        description = request.POST.get('description')


        # Lakukan validasi data di sini jika diperlukan

        # Buat objek Report dan simpan ke database
        report = Report(
            book_title=book_title,
            issue_type=issue_type,
            other_issue=other_issue,
            description=description,
            user=request.user,  # Menghubungkan laporan dengan pengguna yang masuk
        )

        report.save()
        formatted_date = date(report.date_added, "M. d, Y")

        return JsonResponse({'success': True, 'report': {
            'id': report.id,  # Tambahkan ID laporan baru
            'status': report.status,
            'book_title': report.book_title,
            'issue_type': report.issue_type,
            'other_issue': report.other_issue,  # tambahkan other_issue jika ada
            'description': report.description,
            'date_added': formatted_date,  # tambahkan date_added
        }})

    return JsonResponse({'success': False})

def show_xml(request):
    data = Report.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Report.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def hapus_laporan(request, id):
    if request.method == 'POST':
        try:
            laporan = get_object_or_404(Report, pk=id)  # Gantilah "Laporan" dengan model Anda yang sesuai
            laporan.delete()  # Menghapus laporan dari database
            return JsonResponse({"message": "Laporan berhasil dihapus."})
        except Exception as e:
            return JsonResponse({"message": f"Gagal menghapus laporan: {str(e)}"}, status=500)
    return JsonResponse({"message": "Permintaan tidak valid."})

def admin_report(request):
    # Logika untuk halaman "Report Product" di sini
    laporan_list = Report.objects.all()
    return render(request, 'adminreport.html', {'laporan_list': laporan_list})

@csrf_exempt
@login_required
@require_POST
def response_view(request, report_id):
    try:
        data = json.loads(request.body)
        response_text = data.get('responseText')
        status = data.get('status')

        report = Report.objects.get(pk=report_id)
        response = Response(response_text=response_text, user=request.user, report=report)
        response.save()

        report.status = status
        report.description = response_text
        report.save()
        formatted_date = date(report.date_added, "M. d, Y")

        # Update laporan_list
        laporan_list = Report.objects.all()

        # Return the updated data as JSON response
        return JsonResponse({'success': True, 'report': {
            'id': report.id,
            'status': status,
            'book_title': report.book_title,
            'issue_type': report.issue_type,
            'other_issue': report.other_issue,
            'description': response_text,
            'date_added': formatted_date,
        }})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

