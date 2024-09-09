from django.shortcuts import redirect, render
from app.models import (
    GeneralInfo,
    Service,
    Testimonial,
    FrequentlyAskedQuestion,
)


def index(request):

    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    faqs = FrequentlyAskedQuestion.objects.all()

    context= {
        "company_name": general_info.company_name,
        "location": general_info.location,
        "email": general_info.email,
        "phone": general_info.phone,
        "open_hours": general_info.open_hours,
        "video_url": general_info.video_url,
        "x_url": general_info.x_url,
        "facebook_url": general_info.facebook_url,
        "instagram_url": general_info.instagram_url,
        "linkedin_url": general_info.linkedin_url,

        "services": services,
        "testimonials": testimonials,
        "faqs": faqs,
    }
    return render(request, "index.html", context)

def contact_form(request):

    if request.method  == "POST":
        print("\nUser has submitted a contact form\n")
        print(f"request.POST : {request.POST}")
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(f"name : {name}")
        print(f"email : {email}")
        print(f"subject : {subject}")
        print(f"message : {message}")
 
    return redirect("home")