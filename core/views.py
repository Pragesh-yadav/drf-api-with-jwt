from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken,bookSerializer
from django.http import JsonResponse

from .models import BookDetails
@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@api_view(['GET'])
def getbooks(request):
    queryset = BookDetails.objects.all()
    print("query set is")
    print(queryset)
    serializer_class = bookSerializer(queryset, many=True)
    print('s data is ')
    print(serializer_class.data)
    return Response(serializer_class.data)

@api_view(['PUT'])
def updateBookById(request, pk):
    print(pk)

    serializer = BookDetails.objects.get(id=pk)
    print('daddad daad')
    print(serializer)
    serializer_class = bookSerializer(serializer, data=request.data)

    if serializer_class.is_valid():
        serializer.save()
        return Response(serializer_class.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteBookbyId(request, pk):
    print('delete called and id is')
    print(pk)

    serializer = BookDetails.objects.get(id=pk)
    serializer.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def addBook(request):
    print("entered in add")
    serializer = bookSerializer(data=request.data)
    print("ser")
    print (serializer)
    print("data is 1")
    print (request.data)
    if serializer.is_valid(raise_exception=True):
        print("data came is valid")
        print(serializer)
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
