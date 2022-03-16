from django.views.generic import FormView

from .forms import CrawlForm
from .crawler import crawl


class CrawlFormView(FormView):
    template_name = 'base.html'
    form_class = CrawlForm
    success_url = '/'

    def form_valid(self, form: CrawlForm):
        result = crawl(start_url=form.cleaned_data['root_url'])
        return self.render_to_response(
            {
                'crawling_result': result
            }
        )
