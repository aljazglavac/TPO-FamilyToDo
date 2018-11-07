from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .enums import Importance

''' Family model '''
class Family(models.Model):
    family_name = models.CharField('Family name', max_length=30)
    password = models.CharField('Password', max_length=30)
    ''' easy password is 4 digit number for kids to remember faster '''
    easy_password = models.IntegerField('Easy Password', validators=[MinValueValidator(0000),MaxValueValidator(9999)])

    ''' overwrite of default __str__ method, returns name of family '''
    def __str__(self):
        return self.family_name

''' Parent model '''
class Parent(models.Model):
    parent_name = models.CharField('Parent name', max_length=30)
    ''' Family can have two parents but parent can have only one family, many-to-one '''
    parent_family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Parent family')

    ''' overwrite of default __str__ method, returns name of parent '''
    def __str__(self):
        return self.parent_name

''' Child model '''
class Child(models.Model):
    child_name = models.CharField('Children name', max_length=30)
    ''' Family can have many children but child can have only one family, many-to-one '''
    child_family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Family of child')
    
    ''' overwrite of default __str__ method, returns name of child '''
    def __str__(self):
        return self.child_name

''' Task model '''
class Task(models.Model):
    ''' task name/description '''
    task_name = models.CharField('Task', max_length=30)
    ''' taks importance, enum field(high, medium, low) '''
    task_importance = models.CharField('Importance', max_length=3, choices=[(tag, tag.value) for tag in Importance])
    ''' task reward, parent addes reward when completed, can be null/blak '''
    task_reward = models.CharField('Reward', max_length=30, null=True, blank=True)
    ''' days to finish taks, 0 means no limit, only pozitive integers '''
    task_due = models.IntegerField('Due days', default=0, validators=[MinValueValidator(0)])
    ''' taks belongs to one family and to one child '''
    task_family = models.OneToOneField(Family, on_delete=models.CASCADE, verbose_name="Task belongs to family", null=True)
    task_child = models.OneToOneField(Child, on_delete=models.CASCADE, verbose_name="Task belongs to child", null=True)

    ''' overwrite of default __str__ method, returns name of task '''
    def __str__(self):
        return self.task_name