from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.SpellDetail.as_view(), name='spell_detail'),
    path('like/<slug:slug>/', views.SpellLike.as_view(), name='spell_like'),
    path('categories/<category>', views.ListCategories.as_view(),
         name='categories'),
    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(),
         name='delete_comment'),
#     path('create_profile/<int:pk>', views.CreateProfileView.as_view(),
#          name='create_profile'),
    path('profile_view/<int:pk>', views.ProfileView.as_view(), name='profile'),

]
