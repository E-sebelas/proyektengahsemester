from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Report(models.Model):
    BOOK_ISSUE_CHOICES = [
        ('Buku Rusak', 'Damaged'),
        ('Informasi Hilang', 'Missing Information'),
        # Add more choices here
        ('Masalah Lainnya', 'Others'),
    ]
    book_title = models.CharField(max_length=200)
    issue_type = models.CharField(max_length=200, choices=BOOK_ISSUE_CHOICES)
    other_issue = models.CharField(max_length=200, blank= True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Under Review')
    date_added = models.DateField(auto_now_add=True)

class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    response_text = models.TextField()
    BOOK_STATUS_CHOICES = [
        ('Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ]
    status = models.CharField(max_length=200, choices=BOOK_STATUS_CHOICES)
    date_added = models.DateTimeField(auto_now_add=True)
