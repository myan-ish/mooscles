from django.urls import include, path

from workout.views import add_exercise, get_exercises, retrieve_exercise, update_exercise

urlpatterns = [
   path("add-exercise/", add_exercise, name="add-exercise"),
   path("get-exercises/", get_exercises, name="get-exercises"),
   path("get-exercises/<int:exercise_id>/", retrieve_exercise, name="retrieve-exercise"),
   path("edit-exercise/<int:exercise_id>/", update_exercise, name="update-exercise"),
]
