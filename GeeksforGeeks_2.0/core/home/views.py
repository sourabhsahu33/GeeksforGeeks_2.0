
from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from .models import Subject
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from .forms import SubjectForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# ========= Compiler ====================
import traceback
from io import StringIO
from contextlib import redirect_stdout  # Add this import

# ================== Write Home Page URL ======================
def about(request): return render(request, 'about.html')
def courses(request): return render(request, 'courses.html')
def contact(request): return render(request, 'contact.html')
def index(request): return render(request, "index.html")
def blog(request): return render(request, 'blog.html')
def filter(request): return render(request, 'filter.html')
def alarm(request): return render(request, 'alarm.html')


# ================ Compiler Logic =====================
def execute_code(code):
    try:
        # Capture standard output in a buffer
        output_buffer = StringIO()
        with redirect_stdout(output_buffer):
            exec(code)
        output = output_buffer.getvalue()
    except Exception as e:
        # Provide detailed error information
        output = f"Error: {str(e)}\n{traceback.format_exc()}"
    return output

def compiler(request):
    return render(request, 'compiler.html')

def runcode(request):
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        output = execute_code(codeareadata)
        return render(request, 'compiler.html', {"code": codeareadata, "output": output})
    return HttpResponse("Method not allowed", status=405)

# ============== Login Required Sections======================
@login_required(login_url='/login/')
# ================= Resume Section ====================
def resume_form(request): return render(request, 'resume_form.html') 


@login_required(login_url='/login/')
def resume(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        about = request.POST.get('about', '')
        age = request.POST.get('age', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')

        # Skills
        skill1 = request.POST.get('skill1', '')
        skill2 = request.POST.get('skill2', '')
        skill3 = request.POST.get('skill3', '')
        skill4 = request.POST.get('skill4', '')
        skill5 = request.POST.get('skill5', '')

        # Education
        degree1 = request.POST.get('degree1', '')
        college1 = request.POST.get('college1', '')
        year1 = request.POST.get('year1', '')
        degree2 = request.POST.get('degree2', '')
        college2 = request.POST.get('college2', '')
        year2 = request.POST.get('year2', '')
        degree3 = request.POST.get('degree3', '')
        college3 = request.POST.get('college3', '')
        year3 = request.POST.get('year3', '')

        # Languages
        lang1 = request.POST.get('lang1', '')
        lang2 = request.POST.get('lang2', '')
        lang3 = request.POST.get('lang3', '')

        # Projects
        project1 = request.POST.get('project1', '')
        durat1 = request.POST.get('duration1', '')
        desc1 = request.POST.get('desc1', '')
        project2 = request.POST.get('project2', '')
        durat2 = request.POST.get('duration2', '')
        desc2 = request.POST.get('desc2', '')

        # Work Experience
        company1 = request.POST.get('company1', '')
        post1 = request.POST.get('post1', '')
        duration1 = request.POST.get('duration1', '')
        lin11 = request.POST.get('lin11', '')
        company2 = request.POST.get('company2', '')
        post2 = request.POST.get('post2', '')
        duration2 = request.POST.get('duration2', '')
        lin21 = request.POST.get('lin21', '')

        # Achievements
        ach1 = request.POST.get('ach1', '')
        ach2 = request.POST.get('ach2', '')
        ach3 = request.POST.get('ach3', '')

        return render(request, 'resume.html', {
            'name': name, 'about': about, 'age': age, 'email': email, 'phone': phone,
            'skill1': skill1, 'skill2': skill2, 'skill3': skill3, 'skill4': skill4, 'skill5': skill5,
            'degree1': degree1, 'college1': college1, 'year1': year1,
            'degree2': degree2, 'college2': college2, 'year2': year2,
            'degree3': degree3, 'college3': college3, 'year3': year3,
            'lang1': lang1, 'lang2': lang2, 'lang3': lang3,
            'project1': project1, 'durat1': durat1, 'desc1': desc1,
            'project2': project2, 'durat2': durat2, 'desc2': desc2,
            'company1': company1, 'post1': post1, 'duration1': duration1, 'lin11': lin11,
            'company2': company2, 'post2': post2, 'duration2': duration2, 'lin21': lin21,
            'ach1': ach1, 'ach2': ach2, 'ach3': ach3,
        })

    return render(request, 'resume_form.html')



# =========CGPA Calculator============
#  Mapping of letter grades to numeric values
GRADE_POINTS = {'A': 9, 'S': 10, 'B': 8, 'C': 7, 'D': 6, 'F': 0}
@login_required(login_url='/login/')
def cgpa_calculator(request):
    subjects = Subject.objects.all()
    form = SubjectForm()
 
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')
 
    # Calculate CGPA
    total_credits = 0
    total_grade_points = 0
 
    for subject in subjects:
        total_credits += subject.credit
        total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)
 
    if total_credits != 0:
        cgpa = total_grade_points / total_credits
    else:
        cgpa = 0
 
    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }
 
    return render(request, 'subject.html', context)

 
@login_required(login_url='/login/')
def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
 
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')
    else:
        form = SubjectForm(instance=subject)
 
    context = {
        'form': form,
        'subject_id': subject_id,
    }
 
    return render(request, 'edit_subject.html', context)
 
@login_required(login_url='/login/')
def delete_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    return redirect('cgpa_calculator')
 
 
@login_required(login_url='/login/')
def result(request):
    subjects = Subject.objects.all()
    form = SubjectForm()
 
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cgpa_calculator')
 
    # Calculate CGPA
    total_credits = 0
    total_grade_points = 0
 
    for subject in subjects:
        total_credits += subject.credit
        total_grade_points += subject.credit * GRADE_POINTS.get(subject.grade, 0)
 
    if total_credits != 0:
        cgpa = total_grade_points / total_credits
    else:
        cgpa = 0
 
    context = {
        'subjects': subjects,
        'form': form,
        'cgpa': cgpa,
    }
 
    return render(request, 'pdf.html', context)
 

# =============Login System ==============
# Login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()  # Use .first() to get the first object or None
            if not user_obj:
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_authenticated = authenticate(request, username=username, password=password)
            if user_authenticated:
                login(request, user_authenticated)
                return redirect('home')  # Redirect to the 'home' view after successful login
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Click on GFG logo")
            return redirect('/login/')
    return render(request, "login.html")

# Register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if user_obj:
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "register.html")

# Logout function
def custom_logout(request):
    logout(request)
    return redirect('index')
