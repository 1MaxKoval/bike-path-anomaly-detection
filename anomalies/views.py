from django.core.exceptions import ObjectDoesNotExist
from anomalies.models import AccelerationLocation, AccelerationThreshold
from anomalies.api.serializers import AccelerationLocationSerializer, AccelerationThresholdSerializer
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view


class AccelerationLocationView(APIView):

    def get(self, request):
        try:
            threshold = AccelerationThreshold.objects.get(name='default_threshold')
        except ObjectDoesNotExist:
            return Response({'error': 'Please first set the default_threshold.'})
        models = AccelerationLocation.objects.filter(acceleration__gt=threshold.threshold)
        ser = AccelerationLocationSerializer(models, many=True)
        return Response(ser.data)


    def post(self, request):
        ser = AccelerationLocationSerializer(data=request.data, many=True)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data)


@api_view(['PATCH', 'POST'])
def set_threshold(request):
    try:
        threshold = AccelerationThreshold.objects.get(name='default_threshold')
    except ObjectDoesNotExist:
        data = request.data
        data['name'] = 'default_threshold'
        ser = AccelerationThresholdSerializer(data=data, context={'request': request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data=ser.data)
    request.data['name'] = 'default_threshold'
    ser = AccelerationThresholdSerializer(threshold, data=request.data, context={'request': request})
    ser.is_valid(raise_exception=True)
    ser.save()
    return Response(data=ser.data)


