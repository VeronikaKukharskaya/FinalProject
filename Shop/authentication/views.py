from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from authentication.forms import LoginForm, RegisterForm
from django.views.generic import TemplateView
from .models import Profile
from django.urls import reverse


# Create your views here.
def login_user(request):
    context = {'login_form': LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
            else:
                context = {
                    'login_form': login_form,
                    'attention': f'The user with username {username} and password was not found!'
                }
        else:
            context = {
                'login_form': login_form,
            }

    return render(request, 'auth/login.html', context)


class RegisterView(TemplateView):
    template_name = 'auth/register.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {
            'user_form': user_form
        }
        return render(request, 'auth/register.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('index')

        context = {'user_form': user_form}
        return render(request, 'auth/register.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


def profile(request):
    return render(request, 'auth/profile.html')


class ProfilePage(TemplateView):
    template_name = "auth/profile.html"

    def dispatch(self, request, *args,  **kwargs):
        # try:
        # Определяем, какой раздел Личного кабинета открыть (он может прийти в строке url)
        chapter = 'profile'
        if 'data' in kwargs:
            chapter = kwargs['data']

        if request.user.is_authenticated:
            # Проверяем, есть ли куда вернуться, если нет, назначаем
            if 'return' not in request.session:
                request.session['return'] = 'index'

            # Подготовка и работа с Профилем пользователя
            profile_data = Profile.objects.get(user=request.user)
            profile = profile_data.get_user_data()

            if chapter == 'profile':

                if request.method == 'POST':
                    # Сохраняем данные пользователя не проверяя
                    profile = request.POST
                    profile_data.patronymic = request.POST.get("patronymic")
                    profile_data.phoneNumber = request.POST.get("phoneNumber")
                    profile_data.address = request.POST.get("address")
                    profile_data.save()
                    request.user.first_name = request.POST.get("first_name")
                    request.user.last_name = request.POST.get("last_name")
                    request.user.save()

                    # Функция возврата может быть с параметром или без,
                    # если он был, то будет после разделения строки
                    ret = request.session['return'].split()
                    return redirect(*ret)  # Иначе туда, откуда пришли
            else:
                return redirect(reverse("login"))

            return render(request, self.template_name, locals())