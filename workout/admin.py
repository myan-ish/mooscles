from django.contrib import admin

from workout.models import Exercise, Workout, WorkoutExercise

admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(WorkoutExercise)
