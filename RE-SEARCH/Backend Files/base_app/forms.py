from django import forms
from .models import Cluster, Url

class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ('cluster','cluster_url', 'depth', 'output_type')
        
    def __init__(self, cluster_id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if cluster_id:
            self.fields['cluster'].initial = cluster_id
            self.fields['cluster'].widget = forms.HiddenInput()
        
     
