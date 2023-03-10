from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    path('add_spell/', views.AddSpell.as_view(), name='add_spell'),

    path('edit_spell/<int:pk>', views.EditSpell.as_view(), name='edit_spell'),

    path('delete_spell/<int:pk>', views.DeleteSpell.as_view(),
         name='delete_spell'),

    path('<slug:slug>/', views.SpellDetail.as_view(), name='spell_detail'),

    path('like/<slug:slug>/', views.SpellLike.as_view(), name='spell_like'),

    path('categories/<category>', views.ListCategories.as_view(),
         name='categories'),

    path('edit_comment/<int:pk>', views.EditComment.as_view(),
         name='edit_comment'),

    path('delete_comment/<int:pk>', views.DeleteComment.as_view(),
         name='delete_comment'),
]
