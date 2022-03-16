from django import forms


class CrawlForm(forms.Form):
    root_url = forms.URLField(label='Website to crawl', required=True)
