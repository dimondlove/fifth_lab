from django.shortcuts import render


def form(request):
    return render(request, "form_html.html")


def post_student(request):
    lastname = request.POST.get("lastname", "Undefined")
    firstname = request.POST.get("firstname", "Undefined")
    patronymic = request.POST.get("patronymic", "Undefined")
    age = request.POST.get("age", 1)
    address = request.POST.get("student-address", "Undefined")
    student_group = request.POST.get("student_group", "Undefined")
    subjects = request.POST.getlist("subjects", ["Undefined"])
    data = {"lastname": lastname, "firstname": firstname, "patronymic": patronymic, "age": age, "address": address,
            "student_group": student_group, "subjects": subjects}

    return render(request, "student.html", context=data)
