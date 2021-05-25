from django.db import models

# Create your models here.

from sqlalchemy.sql.functions import mode


class faculty(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()
    password=models.CharField(max_length=20)

class facultyfeedback(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=30)
    course=models.CharField(max_length=10,null=True)
    adequacy_of_ourse_sylabus=models.CharField(max_length=10)
    Background_for_benefiting_courcr=models.CharField(max_length=10)
    course_difficulty_to_understand=models.CharField(max_length=10)
    syllabus_completeing_range=models.CharField(max_length=10)
    library_material_availability=models.CharField(max_length=10)
    difficulty_to_get_material=models.CharField(max_length=10)
    levelof_preparation_for_class=models.CharField(max_length=10)
    how_teacher_able_to_communicate=models.CharField(max_length=10)
    how_teacher_encourages_student=models.CharField(max_length=10)
    method_of_encouraging=models.CharField(max_length=10)
    how_helps_advicing=models.CharField(max_length=10)
    teachers_approach=models.CharField(max_length=10)
    Internal_assessment=models.CharField(max_length=10)
    effect_of_internal_assesment=models.CharField(max_length=10)
    how_often_gets_feedback_on_performance=models.CharField(max_length=10)
    Were_your_assignments_discussed_with_you=models.CharField(max_length=10)
    Were_you_provided_with_course_contributory_lecture_too_at_the_beginning=models.CharField(max_length=10)