from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg


class MovieSerializer(serializers.ModelSerializer):

    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def get_rate(self, obj):
        # reviews = obj.reviews.all()
        # if reviews:
        #     soma_reviews = 0
        #     for review in reviews:
        #         soma_reviews += review.stars
        #     return round(soma_reviews / reviews.count(), 1)
        # return None
        rate = obj.reviews.aggregate(Avg("stars"))["stars__avg"]
        if rate:
            return rate

    def validate_release_date(self, value):
        if value.year < 1888:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1888"
            )
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError(
                "O resumo não pode ter mais do que 200 caracteres"
            )
        return value


# class MovieSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
#     relase_date = serializers.DateField()
#     actors = serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)
#     resume = serializers.CharField()
