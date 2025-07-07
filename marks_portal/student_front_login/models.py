from django.db import models

# Create your models here.
class Student(models.Model):
    student=models.CharField(max_length=20, null=True, blank=True)
    student_name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True, blank=True)
    address=models.CharField(max_length=100,null=True, blank=True)
    std=models.IntegerField(null=True, blank=True)
    father=models.CharField(max_length=20,null=True, blank=True)
    dob=models.DateField(null=True, blank=True)
    img=models.ImageField(upload_to='student_image',null=True, blank=True)

    



class StudentTermSummary(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    # Bengali
    bengali_first_theory = models.IntegerField(null=True, blank=True)
    bengali_first_practical = models.IntegerField(null=True, blank=True)
    bengali_second_theory = models.IntegerField(null=True, blank=True)
    bengali_second_practical = models.IntegerField(null=True, blank=True)
    bengali_third_theory = models.IntegerField(null=True, blank=True)
    bengali_third_practical = models.IntegerField(null=True, blank=True)

    # English
    english_first_theory = models.IntegerField(null=True, blank=True)
    english_first_practical = models.IntegerField(null=True, blank=True)
    english_second_theory = models.IntegerField(null=True, blank=True)
    english_second_practical = models.IntegerField(null=True, blank=True)
    english_third_theory = models.IntegerField(null=True, blank=True)
    english_third_practical = models.IntegerField(null=True, blank=True)

    # Mathematics
    mathematics_first_theory = models.IntegerField(null=True, blank=True)
    mathematics_first_practical = models.IntegerField(null=True, blank=True)
    mathematics_second_theory = models.IntegerField(null=True, blank=True)
    mathematics_second_practical = models.IntegerField(null=True, blank=True)
    mathematics_third_theory = models.IntegerField(null=True, blank=True)
    mathematics_third_practical = models.IntegerField(null=True, blank=True)

    # Physical Science
    physical_science_first_theory = models.IntegerField(null=True, blank=True)
    physical_science_first_practical = models.IntegerField(null=True, blank=True)
    physical_science_second_theory = models.IntegerField(null=True, blank=True)
    physical_science_second_practical = models.IntegerField(null=True, blank=True)
    physical_science_third_theory = models.IntegerField(null=True, blank=True)
    physical_science_third_practical = models.IntegerField(null=True, blank=True)

    # Life Science
    life_science_first_theory = models.IntegerField(null=True, blank=True)
    life_science_first_practical = models.IntegerField(null=True, blank=True)
    life_science_second_theory = models.IntegerField(null=True, blank=True)
    life_science_second_practical = models.IntegerField(null=True, blank=True)
    life_science_third_theory = models.IntegerField(null=True, blank=True)
    life_science_third_practical = models.IntegerField(null=True, blank=True)

    # History
    history_first_theory = models.IntegerField(null=True, blank=True)
    history_first_practical = models.IntegerField(null=True, blank=True)
    history_second_theory = models.IntegerField(null=True, blank=True)
    history_second_practical = models.IntegerField(null=True, blank=True)
    history_third_theory = models.IntegerField(null=True, blank=True)
    history_third_practical = models.IntegerField(null=True, blank=True)

    # Geography
    geography_first_theory = models.IntegerField(null=True, blank=True)
    geography_first_practical = models.IntegerField(null=True, blank=True)
    geography_second_theory = models.IntegerField(null=True, blank=True)
    geography_second_practical = models.IntegerField(null=True, blank=True)
    geography_third_theory = models.IntegerField(null=True, blank=True)
    geography_third_practical = models.IntegerField(null=True, blank=True)

    

