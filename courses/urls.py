from django.urls import path

from .views import (
    TutorialListView,
    # TutorialUpdateView,
    TutorialDetailView,
    # TutorialDeleteView,
    # TutorialCreateView  # new
)

urlpatterns = [
#     path('<int:pk>/edit/',
         # TutorialUpdateView.as_view(), name='tutorial_edit'),
    path('<int:id>/',TutorialDetailView, name='tutorial_detail'),
#     path('<int:pk>/delete/',
         # TutorialDeleteView.as_view(), name='tutorial_delete'),
    # path('new/', TutorialCreateView.as_view(), name='tutorial_new'),
    path('', TutorialListView, name='tutorial_list'),
]
