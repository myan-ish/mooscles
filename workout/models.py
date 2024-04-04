from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    video = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Workout(models.Model):
    exercises = models.ManyToManyField(Exercise, through='WorkoutExercise')

    session = models.CharField(blank=True, null=True, max_length=250)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.session} - {self.created_at}"
    
    
class WorkoutExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.exercise.name} - {self.workout.session}"
    
    class Meta:
        unique_together = ('exercise', 'workout')
