from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumber(pagination.PageNumberPagination):

    def get_paginated_response(self, data):

        return Response(OrderedDict([
            ('current_page', self.page.number),
            ('next_page', self.page.next_page_number() if self.page.has_next() else None),
            ('previous_page', self.page.previous_page_number() if self.page.has_previous() else None),
            ('last_page', self.page.paginator.num_pages),
            ('total_results', self.page.paginator.count),
            ('results', data)
        ]))
