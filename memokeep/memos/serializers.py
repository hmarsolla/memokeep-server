from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memo
        fields = ('url', 'title', 'text', 'tags')