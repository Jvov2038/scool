from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.forms import *
from .models import *
from .utils import *


class MainHome(DataMixin, ListView):
    paginate_by = 10
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Образовательный центр")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('personal_area')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('personal_area')


def logout_user(request):
    logout(request)
    return redirect('home')


class ShowPost(DataMixin, DetailView):
    paginate_by = 1
    model = Article
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class Gallery(DataMixin, ListView):
    paginate_by = 50
    model = Article
    template_name = 'main/gallery.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Галерея")
        return dict(list(context.items()) + list(c_def.items()))


# Пункт главного меню №1#
class About(DataMixin, ListView):
    paginate_by = 3
    model = Article
    template_name = 'main/about.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О центре")
        return dict(list(context.items()) + list(c_def.items()))

 #   def get_queryset(self):
  #      return Article.objects.filter(is_published=True)


def personal_area(request):
    if request.method == 'POST':
        form = PersonalAreaForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('personal_area'))
    else:
        form = PersonalAreaForm(instance=request.user)
    context = {'form': form}
    return render(request, 'main/personal_area.html', context)


#Также является пунктом главного меню №5#
class Program(DataMixin, ListView):
    paginate_by = 10
    model = Prog
    template_name = 'main/educational_programs.html'
    context_object_name = 'progs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Образовательные программы')
        return dict(list(context.items()) + list(c_def.items()))


class LectureHall(DataMixin, ListView):
    paginate_by = 10
    model = Lecture
    template_name = 'main/lecture_hall.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Лекториум")
        return dict(list(context.items()) + list(c_def.items()))


class ShowProgram(DataMixin, DetailView):
    model = Prog
    template_name = 'main/program.html'
    slug_url_kwarg = 'program_slug'
    context_object_name = 'prog'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['prog'])
        return dict(list(context.items()) + list(c_def.items()))


class Info(DataMixin, ListView):
    paginate_by = 10
    model = Article
    template_name = 'main/info.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Общая информация")
        return dict(list(context.items()) + list(c_def.items()))


class P_advice(DataMixin, ListView):
    paginate_by = 50
    model = User
    template_name = 'main/p_advice.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Попечительский совет")
        return dict(list(context.items()) + list(c_def.items()))


def e_advice(request):
    return HttpResponse('Экспертный совет')


class Docs(DataMixin, ListView):
    paginate_by = 50
    model = Article
    template_name = 'main/docs.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Документы")
        return dict(list(context.items()) + list(c_def.items()))


def partners(request):
    return HttpResponse('Партнеры')


def m_park(request):
    return HttpResponse('Математический парк')


class News(DataMixin, ListView):
    paginate_by = 10
    model = Article
    template_name = 'main/news.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новости")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class Contacts(DataMixin, ListView):
    paginate_by = 3
    model = Article
    template_name = 'main/contacts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Контакты")
        return dict(list(context.items()) + list(c_def.items()))


def big_challengers(request):
    return HttpResponse('Большие вызовы')


#Пункт главного меню №2#
def how_to_get(request):
    return HttpResponse('Как попасть')


def selection_criteria(request):
    return HttpResponse('Критерии отбора')


def online_application(request):
    return HttpResponse('Заявка онлайн')


def stay_rules(request):
    return HttpResponse('Правила пребывания')


def accommodation_conditions(request):
    return HttpResponse('Условия размещения')


def memo_for_parents(request):
    return HttpResponse('Памятка для родителей')


def required_docs(request):
    return HttpResponse('Необходимые документы')


def faq(request):
    return HttpResponse('Часто задаваемые вопросы')



#Пункт главного меню №3#
def events(request):
    return HttpResponse('Мероприятия')



def methodological_support(request):
    return HttpResponse('Методическое сопровождение')


def sirius_leto(request):
    return HttpResponse('Сириус лето')


def sports_program(request):
    return HttpResponse('Спорт')


def culture_program(request):
    return HttpResponse('Культура')


class MainCategory(DataMixin, ListView):
    paginate_by = 3
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление документа")
        return dict(list(context.items()) + list(c_def.items()))


#def pageNotFound(request, exception):
#    return HttpResponseNotFound(request, "<h3>Страница не найдена</h3>")

