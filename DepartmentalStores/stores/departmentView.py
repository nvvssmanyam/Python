# generic
from rest_framework import generics, mixins
from stores.models import Department
from .serilizers import DepartmentSerializer

class DepartmentPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    lookup_url_kwarg = "pk"
    serializer_class = DepartmentSerializer
    # queryset = Department.object.all

    def get_queryset(self):
        lid = self.kwargs.get(self.lookup_url_kwarg)
        return Department.objects.filter(location=lid)

    def perform_create(self, serializer):
        #serializer.save(self.request.location)
        serializer.save()
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DepartmentRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    pass
    lookup_field = 'pk' # id # url(r'^P<pk>\d+')
    serializer_class = DepartmentSerializer
    # queryset = Location.objects.all()

    def get_queryset(self):
        return Department.objects.all()