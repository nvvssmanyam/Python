# generic
from rest_framework import generics, mixins
from stores.models import Location
from .serilizers import LocationSerializer

class LocationPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LocationSerializer
    # queryset = Location.object.all

    def get_queryset(self):
        return Location.objects.all()

    def perform_create(self, serializer):
        #serializer.save(self.request.location)
        serializer.save()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LocationRudView(generics.RetrieveUpdateDestroyAPIView): #DetailView
    pass
    lookup_field = 'pk' # id # url(r'^P<pk>\d+')
    serializer_class = LocationSerializer
    # queryset = Location.objects.all()

    def get_queryset(self):
        return Location.objects.all()

    