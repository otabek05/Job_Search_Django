from django.forms import ModelForm


from . import models

class Job_form(ModelForm):
    class Meta:
        model = models.Job
        fields = ['company_name','title','category','location','salary', 'descript','contact','education']

       
    def __init__(self, *args, **kwargs):
        super(Job_form, self).__init__(*args, **kwargs)
        
        # Forma sohasiga bitta bitta murojaat etish
        # self.fields['title'].widget.attrs.update({'class': 'form-control'})
        # self.fields['description'].widget.attrs.update({'class': 'form-control'})
        
        # formaning har bir sohasiga 'form-control' class ini for tsikli yordamida qo'shib chiqish
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        



