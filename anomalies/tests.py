from rest_framework.test import APIRequestFactory, APITestCase
from anomalies.views import set_threshold, AccelerationLocationView
from anomalies.api.serializers import AccelerationLocationSerializer
from anomalies.models import AccelerationThreshold, AccelerationLocation


class TestAccelerationViews(APITestCase):

    def setUp(self):
        self.rf = APIRequestFactory()

    def test_get_accelerations(self):
        model = AccelerationThreshold.objects.create(name='default_threshold', threshold=7)
        model.save()
        for i in range(5, 11):
            model = AccelerationLocation.objects.create(latitude=i, longitude=i, acceleration=i)
            model.save()
        request = self.rf.get('/anomalies', data=dict(), format='json')
        response = AccelerationLocationView.as_view()(request)
        self.assertTrue(len(list(response.data)), 3)

    def test_post_acceleration_duplicate_coordinates(self):
        data = [
            {'latitude': 12.44, 'longitude': -123.0, 'acceleration': 0.54},
            {'latitude': 12.44, 'longitude': -123.0, 'acceleration': 0.54},
        ]
        request = self.rf.post('/anomalies', data=data, format='json')
        response = AccelerationLocationView.as_view()(request)
        self.assertTrue(True)


    def test_post_set_threshold(self):
        data = {'threshold': 20.0}
        request = self.rf.post('/threshold', data=data, format='json')
        response = set_threshold(request)
        self.assertTrue('20.0' in response.data['threshold'])

    def test_patch_set_threshold(self):
        model = AccelerationThreshold.objects.create(name='default_threshold', threshold=10.4)
        model.save()
        data = {'threshold': 20.0}
        request = self.rf.patch('/threshold', data=data, format='json')
        response = set_threshold(request)
        self.assertTrue('20.0' in response.data['threshold'])


