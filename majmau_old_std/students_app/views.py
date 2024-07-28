from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import OldStudents
from django.contrib import messages
from openpyxl import Workbook
from django.utils import timezone
from .forms import SignInForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        try:
            # Retrieve form data
            name = request.POST.get('name')
            place = request.POST.get('place')
            address = request.POST.get('address')
            post = request.POST.get('post')
            pin = request.POST.get('pin')
            phone = request.POST.get('phone')
            district = request.POST.get('district')
            state = request.POST.get('state')
            date_of_birth = request.POST.get('db')
            whatsapp = request.POST.get('whatsapp')
            email = request.POST.get('email')
            date_admission = request.POST.get('da')
            date_left = request.POST.get('dl')
            qualification = request.POST.get('qualification')
            is_qualification = request.POST.get('qualificationis') == 'on'
            member_id = request.POST.get('membership_id')
            unit = request.POST.get('unit')
            sector = request.POST.get('sector')
            division = request.POST.get('division')
            place_holding = request.POST.get('holding')

            # Check if email already exists
            if OldStudents.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists. Please use a different email.')
            else:
                # Create a new record in the OldStudents model
                OldStudents.objects.create(
                    name=name,
                    place=place,
                    address=address,
                    post=post,
                    pin=pin,
                    phone=phone,
                    district=district,
                    state=state,
                    date_of_birth=date_of_birth,
                    whatsapp=whatsapp,
                    email=email,
                    date_admission=date_admission,
                    date_left=date_left,
                    qualification=qualification,
                    is_qualification=is_qualification,
                    member_id=member_id,
                    unit=unit,
                    sector=sector,
                    division=division,
                    place_holding=place_holding,
                    date_created=timezone.now()
                )

                # Add a success message
                messages.success(request, f'Registration successful for {name}, thank you!')

        except Exception as e:
            # Handle exceptions and add an error message
            messages.error(request, 'Attempt failed, please try again.')

    # Render the registration template with messages
    return render(request, 'registration.html')


# login for admin
from django.contrib.auth.models import User  # Import the User model


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)

                students = OldStudents.objects.all()
                context = {
                    'students': students
                }
                return render(request, 'list.html', context)  # Redirect to a home page or dashboard
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            messages.error(request, 'Please correct the errors below.')

    elif request.user.is_authenticated:
        students = OldStudents.objects.all()
        context = {
            'students': students
        }
        return render(request, 'list.html', context)
    else:
        form = SignInForm()

    return render(request, 'admin.html', {'form': form})


def log_out(request):
    logout(request)
    return render(request, 'admin.html')


# Export file
def export_students_to_excel(request):
    # Create an in-memory workbook
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = 'Registered Students'

    # Define column headers
    headers = [
        "Name", "Place", "Address", "Post", "Pin", "Phone", "District",
        "State", "Date of Birth", "WhatsApp", "Email", "Date of Admission",
        "Date Left", "Qualification", "Islamic Qualified", "Member ID", "Unit",
        "Sector", "Division", "Place Holding", "Date Created"
    ]

    # Add headers to the worksheet
    worksheet.append(headers)

    # Fetch data from the database
    students = OldStudents.objects.all()

    # Add student data to the worksheet
    for student in students:
        row = [
            student.name, student.place, student.address, student.post,
            student.pin, student.phone, student.district, student.state,
            student.date_of_birth, student.whatsapp, student.email,
            student.date_admission, student.date_left, student.qualification,
            student.is_qualification, student.member_id, student.unit,
            student.sector, student.division, student.place_holding,
            student.date_created
        ]
        worksheet.append(row)

    # Create an HTTP response with the correct Excel content type
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=students.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response
