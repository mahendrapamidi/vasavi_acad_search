from django.db import models
from django.utils import timezone
import os
from django.conf import settings



def get_file_path(instance,filename):
    return (settings.MEDIA_ROOT+'/'+instance.department_code+'/'+instance.year_code+'/'+filename)
# # class Subject(models.Model):
#     department_code=models.CharField(max_length=2,blank=False)
#     subject_code=models.CharField(max_length=7,blank=False)
#     subject_name=models.CharField(max_length=100,blank=False)

#     def __str__(self):
#         return u'%s | %s' %(self.subject_code,self.subject_name)    
department = (
	('it','IT'),
	('cse','CSE'),
	('eee','EEE'),
	('mech','MECH'),
	('ece','ECE'),
	('civil','CIV'),
)
year = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
)
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file_name=models.CharField(max_length=255, blank=True)
    document= models.FileField(upload_to=get_file_path,blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    department_code=models.CharField(max_length=4 ,choices=department,default='it')
    year_code=models.CharField(max_length=1,choices=year,default='1')
    subject_code=models.CharField(max_length=7,blank=False)
    subject_name=models.CharField(max_length=100,blank=False)
    def get_relative_path(self):
        pat=os.path.relpath(self.files.path, settings.MEDIA_ROOT)
        return (settings.MEDIA_URL+pat)
    relative_path=property(get_relative_path)
    class Meta:
        verbose_name='File'
        verbose_name_plural='Files'

    def __str__(self):
        return (self.file_name)



