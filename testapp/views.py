from django.shortcuts import render
from testapp.form import studentform
# Create your views here.

# def std_form_view(request):
#     form=studentform()
#     return render(request,'form.html',{'form':form})

def student_info(request):
    submitted=False
    sname=''
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            print("Form validation success and print data")
            print('Name:',form.cleaned_data['name'])
            print('RollNo:',form.cleaned_data['rollno'])
            print('Marks:',form.cleaned_data['marks'])
            sname=form.cleaned_data['name']
            submitted=True
    form=studentform()
    return render(request,'form.html',{'form':form,'submitted':submitted,
	'sname':sname})
