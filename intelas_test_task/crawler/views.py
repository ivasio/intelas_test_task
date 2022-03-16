from django.views.generic import FormView

from .forms import CrawlForm


class CrawlFormView(FormView):
    template_name = 'base.html'
    form_class = CrawlForm
    success_url = '/'

    def form_valid(self, form: CrawlForm):
        return self.render_to_response(
            {
                'crawling_result': form.cleaned_data['root_url']
            }
        )
