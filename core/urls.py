from django.urls import path
from .views import current_user, UserList,getbooks1,AddBook,UpdateBook,DeleteBook

urlpatterns = [
    path('current_user/', current_user),
    path('getbooks1', getbooks1),
    path('AddBook', AddBook),
    path('updateBookById/<int:pk>', UpdateBook),
    path('DeleteBook/<int:pk>', DeleteBook),
    

    #path('editBookByIdAPI', views.editBookByIdAPI.as_view()),
    path('users/', UserList.as_view())

]
