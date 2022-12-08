# from turtle import st
# from django.shortcuts import render
# from bookApi.models import Book
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from bookApi.serializers import BookSerializers

# # Create your views here.
# @api_view(["GET"])
# def book_list(request):
#     books = Book.objects.all() #returns complex data
#     serializer = BookSerializers(books, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializers(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, id):
#     try:
#         book = Book.objects.get(id=id)
#     except:
#         return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = BookSerializers(book)
#         return Response(serializer.data)

#     if request.method == 'PUT':
#         serializer = BookSerializers(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         book.delete()
#         return Response({'Record Deleted.'}, status=status.HTTP_204_NO_CONTENT)
from rest_framework.views import APIView
from bookApi.models import Book
from bookApi.serializers import BookSerializers
from rest_framework.response import Response
from rest_framework import status

class BookList(APIView):
    
    def get(self, request):
        books = Book.objects.all() #returns complex data
        serializer = BookSerializers(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreate(APIView):

    def post(self, request):
        serializer = BookSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):

    def get_book_by_id(self, id):
        try:
            book = Book.objects.get(id=id)
            return book
        except:
            return Response({'Error': "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        book = self.get_book_by_id(id)
        serializer = BookSerializers(book)
        return Response(serializer.data)

    def put(self, request, id):
        book = self.get_book_by_id(id)
        serializer = BookSerializers(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = self.get_book_by_id(id)
        book.delete()
        return Response({'Record Deleted.'}, status=status.HTTP_204_NO_CONTENT)