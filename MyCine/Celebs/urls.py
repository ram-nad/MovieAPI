from django.urls import path

from . import views

urlpatterns = [
	path('',views.CelebAdd.as_view()),
	path('<int:id>',views.CelebDetail.as_view()),
	path('director/<int:id>',views.DirectorDetail.as_view()),
	path('actor/<int:id>',views.ActorDetail.as_view()),
]
