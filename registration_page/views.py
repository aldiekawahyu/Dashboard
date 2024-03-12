
from django.shortcuts import render, redirect
from django.contrib import messages  # Impor messages
from .models import User  # Sesuaikan dengan path model Anda


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        name = request.POST.get('name', '')

        if password != confirm_password:
            # Jika password tidak cocok, tambahkan pesan dan kembali ke halaman registrasi
            messages.error(request, "Passwords do not match.")
            return render(request, 'registration_page/registration.html')

        # Proses pembuatan user baru
        new_user = User(email=email, name=name)
        new_user.set_password(password)  # Meng-hash password
        new_user.save()  # Menyimpan user
        return redirect('login_page')  # Redirect ke halaman login

    return render(request, 'registration_page/registration.html')
