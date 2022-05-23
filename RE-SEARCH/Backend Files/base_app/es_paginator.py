'''from django.core.paginator import Paginator, Page

class DSEPaginator(Paginator):
    """
    Overrides the Django Paginator class to count number of items.
    Elasticsearch provides the total as a part of the query results.
    """
    def __init__(self, *args, **kwargs):
        super(DSEPaginator, self).__init__(*args, **kwargs)
        self._count = self.object_list.hits.total

    def page(self, number):
        # this is overridden to prevent any slicing of the object_list
        number = self.validate_number(number)
        return Page(self.object_list, number, self)'''

from django.utils.functional import LazyObject

class SearchResults(LazyObject):
    def __init__(self, search_object):
        self._wrapped = search_object

    def __len__(self):
        return self._wrapped.count()

    def __getitem__(self, index):
        search_results = self._wrapped[index]
        if isinstance(index, slice):
            search_results = list(search_results)
        return search_results