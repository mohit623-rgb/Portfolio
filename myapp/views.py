from django.shortcuts import render, redirect
from .models import Student   # ✅ correct import
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def Home(request):
    return render(request, "app/index.html")


def submit_form(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message"),

            website=bool(request.POST.get("website")),
            branding=bool(request.POST.get("branding")),
            ecommerce=bool(request.POST.get("ecommerce")),
            seo=bool(request.POST.get("seo")),
        )
        return redirect("home")  # ✅ redirect after submit

    return redirect("home")

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Form submitted successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)