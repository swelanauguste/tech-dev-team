from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q

from .models import Document

# class SearchListView(ListView):
#     model = Document
#     template_name = "core/search_result_list.html"
#     queryset = Document.objects.all()

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         if query:
#             return Document.objects.filter(
#                 Q(name__icontains=query)
#                 | Q(description=query)
#             )
#         else:
#             return Document.objects.all()

class DocumentListView(ListView):
    model = Document
    # paginate_by = 10
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Document.objects.filter(
                Q(name__icontains=query)
                | Q(description=query)
            )
        else:
            return Document.objects.all()
