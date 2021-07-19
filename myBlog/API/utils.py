

from rest_framework.generics import ListCreateAPIView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page



class ViewListMixin(ListCreateAPIView):
    @method_decorator(cache_page(60 * 1))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)