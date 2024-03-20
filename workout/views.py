import re
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from workout.forms import AddExerciseForm
from workout.models import Exercise, Workout, WorkoutExercise

User = get_user_model()

def get_exercise(request):
    user = request.user if request.user.id else User.objects.get(username="admin")
    workout, created = Workout.objects.get_or_create(user=user)
    return WorkoutExercise.objects.filter(workout=workout)

def index_page(request):
    return render(request, 'website/index.html', {"exercises": get_exercise(request)})

@csrf_exempt
def add_exercise(request):
    exercises = get_exercise(request)
    if request.method == "POST":
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.id else User.objects.get(username="admin")
            
            workout, created = Workout.objects.get_or_create(user=user)
            
            try:
                WorkoutExercise.objects.create(
                    exercise_id=form.cleaned_data["exercise"],
                    sets=form.cleaned_data["sets"],
                    reps=form.cleaned_data["reps"],
                    weight=form.cleaned_data["weight"],
                    workout=workout
                )
            except IntegrityError as e:
                if 'unique constraint' in str(e).lower() :
                    return render(request, 'website/index.html', {"errors": {"exercise": "Exercise already added", "exercises": exercises}})
                elif 'foreign key constraint' in str(e).lower():
                    return render(request, 'website/index.html', {"errors": {"exercise": "Exercise does not exist", "exercises": exercises}})
                else:
                    return render(request, 'website/index.html', {"errors": {"exercise": "An error occurred", "exercises": exercises}})
            except Exception as e:
                raise e
        else:
            return render(request, 'website/index.html', {"errors": form.errors, "exercises":
                                                          exercises})

    return render(request, 'website/index.html', {"exercises": exercises, "form": AddExerciseForm()})

def get_exercises(request):
    exercises = Exercise.objects.all()
    return render(request, 'website/all_exercises_dropdown.html', {"exercises": exercises})