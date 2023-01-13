from rest_framework import pagination

class ContactPagination(pagination.PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = "size"
    page_size = 10
    max_page_size = 20
    last_page_strings = "end"