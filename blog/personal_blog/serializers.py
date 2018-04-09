from rest_framework import serializers
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from personal_blog.models import ArticleModel,ColumnModel,LabelModel,CommentModel


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnModel
        fields = '__all__'


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelModel
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = '__all__'


class ArticleSerializer(CacheResponseMixin,serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = '__all__'