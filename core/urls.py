from django.urls import path
from .views import current_user, UserList,getbooks,
addBook,updateBookById,deleteBookbyId

urlpatterns = [
    path('current_user/', current_user),
    path('getAllBooks', getbooks),
    path('addBook', addBook),
    path('updateBookById/<int:pk>', updateBookById),
    path('deleteBookbyId/<int:pk>', deleteBookbyId),
    path('users/', UserList.as_view())
]
