from django.urls import path

from .views import (
    TutorialListView,
    # TutorialUpdateView,
    TutorialDetailView,
    # TutorialDeleteView,
    # TutorialCreateView  # new
)

urlpatterns = [
    path('<int:id>/',TutorialDetailView, name='tutorial_detail'),
    path('', TutorialListView, name='tutorial_list'),
]
