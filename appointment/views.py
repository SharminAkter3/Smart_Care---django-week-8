from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()  # filter na korly sob golo show korby
    serializer_class = serializers.AppointmentSerializer

    # custom query -> specific karo jnn filter korbo
    def get_queryset(self):
        queryset = super().get_queryset()  # agy r query ta ky override korby
        patient_id = self.request.query_params.get(
            "patient_id"
        )  # url e kono kicu pass korly
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
            return queryset
