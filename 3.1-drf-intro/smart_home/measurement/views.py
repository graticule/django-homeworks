# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import BriefSensorSerializer, DetailedSensorSerializer, DetailedMeasurementSerializer


#@api_view(['GET', 'POST'])
class ListSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = BriefSensorSerializer


#@api_view(['GET', 'PATCH'])
class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = DetailedSensorSerializer


#@api_view(['POST'])
class MeasurementView(CreateAPIView):
    serializer_class = DetailedMeasurementSerializer
