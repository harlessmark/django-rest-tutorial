from rest_framework import serializers
from news.models import Journalist, Article

from datetime import datetime
from django.utils.timesince import timesince

class ArticleSerializer(serializers.ModelSerializer):
    time_since_publication = serializers.SerializerMethodField()

    # displays author string name instead of id
    author = serializers.StringRelatedField()

    class Meta:
        model = Article

        # serialize all of the model fields
        fields = "__all__"

        # choose what fields to serialize and send to user
        # fields = ("title", "body")

        # choose which fields to exclude when sending to user
        # exclude = ("id",)

    def get_time_since_publication(seld, object):
        """ gets the time since publication """
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)

        return time_delta

    # object-level custom validation
    def validate(self, data):
        """ checks that description and title are different """

        if data["title"] == data["descriptions"]:
            raise serializers.ValidationError("Title and description must be different")
        
        return data

    # field-level custom validation
    def validate_title(self, value):
        """ checks that title is greater than 10 characters """
        if len(value) < 10:
            raise serializers.ValidationError("Title must be at least 10 characters long")

        return value

class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Journalist 
        fields = "__all__"

# regular serialization
# class ArticleSerializer(serializers.Serializer): 
#     id = serializers.IntegerField(read_only=True)
#     author = serializers.CharField()
#     title = serializers.CharField()
#     descriptions = serializers.CharField()

#     # notice: we use CharField here even though the model is TextField
#     body = serializers.CharField()

#     location = serializers.CharField()
#     publication_date = serializers.DateField()
#     active = serializers.BooleanField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)

#     # creates an Article instance
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         # if 'author' is not provided, just use the old author by using `instance.author`
#         instance.author = validated_data.get('author', instance.author)
#         instance.title = validated_data.get('title', instance.title)
#         instance.descriptions = validated_data.get('descriptions', instance.descriptions)
#         instance.body = validated_data.get('body', instance.body)
#         instance.location = validated_data.get('location', instance.location)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.active = validated_data.get('active', instance.active)

#         instance.save()
#         return instance