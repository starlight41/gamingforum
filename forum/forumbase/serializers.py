from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)                                
from forumbase.models import Question


class QuestionSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Question 
        fields = ('id', 'title', 'tags')