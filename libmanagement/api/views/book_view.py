from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import logging
from api.models import Book
from api.serializers import BookSerializer

logger = logging.getLogger('django')
from rest_framework import response,status
from rest_framework.response import Response





class AdminBookView(APIView):
    permission_classes = [IsAdminUser, IsAuthenticated]
    authentication_class = [JSONWebTokenAuthentication]
    def post(self,request):
        try:
            serializer=BookSerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def patch(self,request):
        try:
            book_obj=None
            try:
                book_obj=Book.objects.get(id=request.data.get('id'))
            except Exception as e:
                logger.exception(e)
                return Response(data={'message':"Invalid book id"})
            serializer = BookSerializer(book_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self,request,id=None):
        try:
            if id==None:
                return Response(data={"message":"Book Id not specified"},status=status.HTTP_400_BAD_REQUEST)
            try:
                Book.objects.get(id=id).delete()
            except Book.DoesNotExist as e:
                logger.exception(e)
                return Response(data={'message':"Book does not exist"},status=status.HTTP_404_NOT_FOUND)

            return Response(data={'message':"Book deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetBookView(APIView):
    permission_classes = [IsAdminUser,IsAuthenticated]
    authentication_class = [JSONWebTokenAuthentication]

    def get(self,request):
        try:

            book_data=Book.objects.all()
            serializer = BookSerializer(book_data,many=True)
            return response.Response(data={'data':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            logger.exception(e)
            return Response({'message': 'Something went wrong'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

