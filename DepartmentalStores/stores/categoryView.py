# generic
from rest_framework import generics, mixins
from stores.models import Category
from .serilizers import CategorySerializer

class CategoryPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"
    serializer_class = CategorySerializer
    # queryset = Category.object.all

    def get_queryset(self):
        did = self.kwargs.get(self.lookup_url_kwarg)
        return Category.objects.filter(department=did)

    def perform_create(self, serializer):
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    lookup_field = 'pk' # id # url(r'^P<pk>\d+')
    serializer_class = CategorySerializer
    # queryset = Location.objects.all()

    def get_queryset(self):
        return Category.objects.all()