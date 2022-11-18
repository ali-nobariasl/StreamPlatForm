from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination




class WatchListPagination(PageNumberPagination):
    page_size = 10
    #page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 20
    #last_page_strings = 'end'

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit =10
    