from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

FAKE_USER = "admin"
FAKE_PASS = "admin123"

@csrf_protect
def login_fake(request):
    if request.method == "POST":
        usuario = request.POST.get("username", "").strip()
        clave = request.POST.get("password", "").strip()

        if usuario == FAKE_USER and clave == FAKE_PASS:
            response = redirect("panel")
            response.set_cookie('fake_logged', 'true', max_age=3600)
            response.set_cookie('fake_user', usuario, max_age=3600)
            return response
        else:
            # Si falla, enviamos un mensaje de error simple a la plantilla
            return render(request, "registration/login.html", {"error": "Usuario o contraseña incorrectos"})

    return render(request, "registration/login.html")

def logout_fake(request):
    response = redirect("login")
    response.delete_cookie('fake_logged')
    response.delete_cookie('fake_user')
    return response

def panel_general(request):
    if request.COOKIES.get('fake_logged') != 'true':
        return redirect("login")
        
    return render(request, "panel.html", {
        "usuario": request.COOKIES.get('fake_user', 'Invitado'),
    })