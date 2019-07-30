from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CsrfMixins(object):
        @method_decorator(csrf_exempt)
        def dispatch(self, request, *args, **kwargs):
            return super(CsrfMixins, self).dispatch(request, *args, **kwargs)

