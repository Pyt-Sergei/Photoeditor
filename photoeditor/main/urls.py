from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.List.as_view()),

    path('resize/', views.Resize.as_view()),
    path('scale/', views.Scale.as_view()),
    path('scale/<str:scaling>', views.ScaleDynamic.as_view()),
    path('crop/', views.Crop.as_view()),
    path('reverse/', views.Reverse.as_view()),
    path('rotate/<int:angle>', views.Rotate.as_view()),

    path('filters/', views.Filter.as_view()),
]
