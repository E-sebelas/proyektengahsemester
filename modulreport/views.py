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
from django.contrib.auth.models import User

@login_required
def report_book(request):
    # Logika untuk halaman "Report Product" di sini
    laporan_list = Report.objects.filter(user=request.user)
    return render(request, 'mainreport.html', {'laporan_list': laporan_list})



@csrf_exempt
@login_required(login_url='/login/')  # Requires authentication with '/login/'
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

        # Include the 'username' in the response
        user_info = {
            'username': report.user.username
        }

        # Return the updated data as JSON response
        return JsonResponse({'success': True, 'report': {
            'id': report.id,
            'status': status,
            'book_title': report.book_title,
            'issue_type': report.issue_type,
            'other_issue': report.other_issue,
            'description': response_text,
            'date_added': formatted_date,
            'user': user_info  # Include user information
        }})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@csrf_exempt
def show_json_flutter(request):
    print(request.body)

    data = json.loads(request.body)
    print(data)
    user_id = data['user_id']
    # flutter = {
    #  'user_id' : input user id    # }
    user = User.objects.get(pk=user_id)
    products = Report.objects.filter(user=user)
    print(user)
    print(products)
    product_list = []
    for product in products:
        product_list.append(product.to_dict())
    print(product_list)
    return JsonResponse({'products':product_list})

def show_json_by_user(request, user_id):
    data = Report.objects.filter(user__id=user_id)  # Filter by user_id

    serialized_data = serializers.serialize("json", data)
    return HttpResponse(serialized_data, content_type="application/json")


@csrf_exempt
def simpan_laporan_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Extracting data from the request
        book_title = data.get('book_title')
        issue_type = data.get('issue_type')
        other_issue = data.get('other_issue')
        description = data.get('description')

        # Creating a new Product object using the extracted data
        new_product = Report.objects.create(
            book_title=book_title,
            issue_type=issue_type,
            other_issue=other_issue,
            description=description,
            user=request.user  # Make sure to handle user authentication properly
        )

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
