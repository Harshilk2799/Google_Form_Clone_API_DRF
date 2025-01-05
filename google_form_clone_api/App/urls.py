from django.urls import path
from App import views

urlpatterns = [
    path("questions/", views.QuestionAPI.as_view()),
    path("form/<pk>/", views.FormAPI.as_view()),
    path("store_response/", views.StoreResponsesAPI.as_view()),
    path("form/response/<pk>/", views.FormResponsesAPI.as_view())
]
