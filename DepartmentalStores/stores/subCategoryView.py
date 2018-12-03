# generic
from rest_framework import generics, mixins
from stores.models import SubCategory
from .serilizers import SubCategorySerializer

class SubCategoryPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"
    serializer_class = SubCategorySerializer
    # queryset = SubCategory.object.all

    def get_queryset(self):
        cid = self.kwargs.get(self.lookup_url_kwarg)
        return SubCategory.objects.filter(category=cid)

    def perform_create(self, serializer):
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SubCategoryRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    lookup_field = 'pk' # id # url(r'^P<pk>\d+')
    serializer_class = SubCategorySerializer
    # queryset = Location.objects.all()

    def get_queryset(self):
        return SubCategory.objects.all()