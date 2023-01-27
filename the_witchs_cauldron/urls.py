from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.SpellDetail.as_view(), name='spell_detail'),
    path('like/<slug:slug>/', views.SpellLike.as_view(), name='spell_like'),
    path('categories/<category>', views.Categories.as_view(), name='categories'),
]
