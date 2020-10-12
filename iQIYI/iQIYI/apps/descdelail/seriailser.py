from rest_framework.serializers import ModelSerializer

from descdelail.models import PerformerDetailModel


class DescSerialiser(ModelSerializer):
    class Meta:
        model = PerformerDetailModel
        fields = '__all__'

