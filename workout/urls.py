from django.urls import include, path

from workout.views import add_exercise, get_exercises

urlpatterns = [
   path("add-exercise/", add_exercise, name="add-exercise"),
   path("get-exercises/", get_exercises, name="get-exercises"), 
]
