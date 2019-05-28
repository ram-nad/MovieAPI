from django.urls import path

from . import views

urlpatterns = [
	path('',views.MovieList.as_view()),
	path('<int:id>',views.MovieDetail.as_view()),
	path('year/<int:year>',views.MovieListYear.as_view()),
	path('rating/<int:rating>',views.Rating.as_view()),
	path('<int:id>/ratings',views.RatingList.as_view()),
	path('<int:id>/ratings/<slug:username>',views.RatingDetail.as_view()),
]
