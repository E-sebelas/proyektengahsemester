from django.forms import ModelForm

from bookrequest.models import Reqbook


class ReqForm(ModelForm):
    class Meta:
        model = Reqbook
        fields = ["title", "author", "published"]