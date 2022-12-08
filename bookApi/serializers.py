from rest_framework import serializers
from bookApi.models import Book
from django.forms import ValidationError

# class BookSerializers(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_dates = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)

#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.title)
#         instance.publish_dates = data.get('publish_dates', instance.title)
#         instance.quantity = data.get('quantity', instance.title)

#         instance.save()
#         return instance

class BookSerializers(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No DIet COke Plaease!")
        return value

    def validate(self, data):
        if data["number_of_pages"] > 200 and data["quantity"]>200:
            raise ValidationError("Too Heavy for Inventory")
        return data