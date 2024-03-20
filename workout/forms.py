from django import forms

class AddExerciseForm(forms.Form):
    exercise = forms.IntegerField()
    sets = forms.IntegerField()
    reps = forms.IntegerField()
    weight = forms.DecimalField(max_digits=8, decimal_places=2)

    def clean(self):
        cleaned_data = super().clean()
        exercise = cleaned_data.get("exercise")
        sets = cleaned_data.get("sets")
        reps = cleaned_data.get("reps")
        weight = cleaned_data.get("weight")

        if not exercise:
            self.add_error("exercise", "Exercise is required")
        if not sets:
            self.add_error("sets", "Sets is required")
        if not reps:
            self.add_error("reps", "Reps is required")
        if not weight:
            self.add_error("weight", "Weight is required")
        
        return cleaned_data
