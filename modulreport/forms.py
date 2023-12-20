from django import forms
from .models import Report
from .models import Response


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['book_title', 'issue_type', 'other_issue', 'description', 'username', 'admin_response']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['response_text', 'status']
