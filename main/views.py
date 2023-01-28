from django.shortcuts import render,redirect

from .models import Category, Education, Job,Location,Salary
from .forms import Job_form


# Create your views here.
def main(request):
    category= Category.objects.all()
    job=Job.objects.all()
    location = Location.objects.all()
    context={
       
        'jobs':job,
        'categories': category,
        'locations': location
    }
    return render(
        request=request,
        template_name='main/main.html',
        context=context
    )

def createJob(request):
    category1=Category.objects.all()
    education1=Education.objects.all()
    location1= Location.objects.all()
    salary1 = Salary.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "POST":
        company_name =request.POST.get('company')
        title =request.POST.get('title')
        category =request.POST.get('category')
        location =request.POST.get('location')
        descript =request.POST.get('descript')
        education =request.POST.get('education')
        owner=request.user
        salary =request.POST.get('salary')
        contact =request.POST.get('contact')
        newJob= Job.objects.create(
           company_name=company_name,
           title=title,
           category=Category.objects.get(name=category),
           location=Location.objects.get(name=location),
           owner=owner,
           salary=salary,
           descript=descript,
           contact=contact,
           education=Education.objects.get(name=education)
        )
        print(newJob)
        newJob.save()
        return redirect('myprofile')
        


    context={
        'categories':category1,
        'education': education1,
        'locations': location1,
        'salaries': salary1

    }
    return render(request=request, template_name='main/form_create.html', context=context)



def category(request, id):
    category= Category.objects.all()
    job=Job.objects.all()
    location = Location.objects.all()

    category_name = Category.objects.get(id=id)
    sorts = Job.objects.filter(category =category_name)
   

    context ={
        'jobs':job,
        'categories': category,
        'locations':location,
        'sorts':sorts,
        'title':f'{category_name} soha bo\'yicha {len(sorts)} ta ish e\'lon qilingan!'
    }


    return render(
        request=request,
        template_name='main/sort.html',
        context=context

    )



def location(request, id):
    category= Category.objects.all()
    job=Job.objects.all()
    location = Location.objects.all()

    
    city_name=Location.objects.get(id=id)
    cities= Job.objects.filter(location=city_name)


    context ={
        'jobs':job,
        'categories': category,
        'locations':location,
        'sorts':cities,
        'title': f'{city_name}da {len(cities)} ta ish e\'lon qilingan!'

    }


    return render(
        request=request,
        template_name='main/sort.html',
        context=context

    )


def search(request):
    category= Category.objects.all()
    job=Job.objects.all()
    location = Location.objects.all()

    
    q=request.GET.get('q')
    found =Job.objects.filter(title__icontains=q)



    context ={
        'jobs':job,
        'categories': category,
        'locations':location,
        'sorts':found,
        'title': f' "{q}" so\'rov bo\'yicha {len(found)} ta ish topildi'
    }


    return render(
        request=request,
        template_name='main/qidiruv.html',
        context=context

    )


def details(request, id):
    job = Job.objects.get(id=id)
    category= Category.objects.all()
    location = Location.objects.all()
    

    

    context ={
        'job':job,
        'categories': category,
        'locations':location,
    }

    return render(
        request=request,
        template_name='main/details.html',
        context=context

    )

def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    job = Job.objects.get(id=id)
    if job.owner == request.user:
        job.delete()
        return redirect('my_page')

def update(request, id):
    
    form = Job.objects.get(id=id)
    if form.owner != request.user:
        return redirect('logout')
    Form=Job_form(instance=form)
    if request.method == 'POST':
        forma =Job_form(request.POST, instance=form)
        if forma.is_valid():
            forma.save()
            return redirect('my_page')
    context ={
        'form':Form
    }
    return render(request=request, template_name='main/update.html', context=context)




