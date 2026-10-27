from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

# Credenciales falsas para pruebas
FAKE_USER = "Admin"
FAKE_PASS = "admin123"


@csrf_protect
def login_fake(request):
    if request.method == "POST":
        usuario = request.POST.get("username", "").strip()
        clave = request.POST.get("password", "").strip()

        if usuario == FAKE_USER and clave == FAKE_PASS:
            request.session["fake_logged"] = True
            request.session["fake_user"] = usuario
            # "Recordarme" opcional
            if not request.POST.get("remember_me"):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(60 * 60 * 24 * 14)
            return redirect(request.POST.get("next") or "panel")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "registration/login.html")


def logout_fake(request):
    request.session.flush()
    return redirect("login")


def panel_general(request):
    if not request.session.get("fake_logged"):
        return redirect("login")
    return render(request, "panel.html", {
        "usuario": request.session.get("fake_user"),
    })