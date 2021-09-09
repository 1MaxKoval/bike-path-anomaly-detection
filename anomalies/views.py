from django.core.exceptions import ObjectDoesNotExist
from anomalies.models import AccelerationLocation, AccelerationThreshold
from anomalies.api.serializers import AccelerationLocationSerializer, AccelerationThresholdSerializer
from rest_framework.views import Response, APIView
from rest_framework.decorators import api_view
from rest_framework import status


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
        print(request.data)
        ser.is_valid()
        breakpoint()
        if ser.errors:
            print(ser.errors)
            breakpoint()
            return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)
        ser.save()
        response = Response(data=ser.data)
        print(response.data)
        return Response(data=ser.data)

    def delete(self, request):
        vals = AccelerationLocation.objects.all()
        vals.delete()
        return Response(data={'success': 'deleted'})



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
