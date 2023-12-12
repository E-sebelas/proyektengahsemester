from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    BOOK_ISSUE_CHOICES = [
        ('Buku Rusak', 'Damaged'),
        ('Informasi Hilang', 'Missing Information'),
        ('Masalah Lainnya', 'Others'),
    ]
    book_title = models.CharField(max_length=200)
    issue_type = models.CharField(max_length=200, choices=BOOK_ISSUE_CHOICES)
    other_issue = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, default='Under Review')
    date_added = models.DateField(auto_now_add=True)

    def to_dict(self):
        report_dict = {
            'model': 'Report',
            'id': self.user.pk,
            'fields': {
                'book_title': self.book_title,
                'issue_type': self.issue_type,
                'other_issue': self.other_issue,
                'description': self.description,
                'user': self.user.pk if self.user else 0,
                'status': self.status,
                'date_added': self.date_added.strftime("%Y-%m-%d")  # Adjust the date format if needed
            }
        }
        return report_dict



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
