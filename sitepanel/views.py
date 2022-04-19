from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.db import transaction
from django.shortcuts import render, redirect
from sitepanel.forms import *
from verify_email.email_handler import send_verification_email
from .edit_errors import from_errors_to_list


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user_name = request.user
            return render(request, 'index.html', {'user_name': user_name})
        else:
            return render(request, 'index.html')


# ----------------------users view--------------------------------


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    @transaction.atomic
    def post(self, request):
        form = RegisterForm(request.POST)

        if form.errors:
            from_errors_to_list(form, request)

            return render(request, 'register.html', {'form': form})

        if not form.is_valid():
            return render(request, 'register.html', {'form': form})

        user = form.save()
        user.save()
        parent = ProfileParent()
        parent.user = user
        parent.save()

        send_verification_email(request, form)

        messages.success(request, 'Rejestracja przebiegła prawidłowo. Sprawdź skrzynkę mailową. '
                               'Otrzymałeś link aktywacyjny.')

        return redirect('login')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form, 'login': login})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.error(request, 'Błędny login lub hasło')
                return render(request, 'login.html', {'form': form})
        else:
            messages.error(request, 'Nastąpił błąd. Skontaktuj sie z nami!!!')
            return redirect('home')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# _____________________________


class UserView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        form = User.objects.get(id=user.id)
        if user.parent is False:
            kids = Kids.objects.get(kids_id=user)
            return render(request, 'user.html', {'form': form, 'kids': kids})
        return render(request, 'user.html', {'form': form})


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        form = EditProfileForm(initial={"username": user.username,
                                        "first_name": user.first_name,
                                        "last_name": user.last_name,
                                        "email": user.email})

        return render(request, 'edit_profile.html', {'form': form})

    def post(self, request):
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user = request.user

        if User.objects.filter(username=username) and username != user.username:
            form = EditProfileForm(initial={"username": user.username,
                                            "first_name": user.first_name,
                                            "last_name": user.last_name,
                                            })
            is_active = user.is_active
            messages.error(request, 'Login zajęty. Wybierz inny.')
            return render(request, 'edit_profile.html', {'is_active': is_active, 'form': form})

        else:
            User.objects.filter(id=user.id).update(username=username,
                                                   first_name=first_name,
                                                   last_name=last_name)
        return redirect('edit_profile')


class EditPasswordView(LoginRequiredMixin, View):
    def get(self, request):
        form = EditPasswordForm(request.user, request.POST)
        return render(request, 'edit_password.html', {"form": form})

    def post(self, request):
        form = EditPasswordForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            messages.success(request, 'Hasło zmienione poprawnie!')
            return redirect('edit_password')

        else:
            from_errors_to_list(form, request)
            return redirect('edit_password')


class KidsView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        kids = Kids.objects.filter(user_id=user.id)
        return render(request, 'kids.html', {"kids": kids})

    def post(self, request):
        form = EditPasswordForm(request.user, request.POST)


class AddKidsView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddKidsForm()
        return render(request, 'add_kids.html', {"form": form})

    def post(self, request):
        form = AddKidsForm(request.POST)

        if form.errors:
            from_errors_to_list(form, request)

            return render(request, 'add_kids.html', {'form': form})

        if not form.is_valid():
            return render(request, 'add_kids.html', {'form': form})

        if form.is_valid():
            parent = request.user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, parent=False)
            user.save()
            kid = Kids(user_id=parent, kids_id=user)
            kid.save()

        return redirect('kids')
