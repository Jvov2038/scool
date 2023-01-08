from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class MainHome(DataMixin, ListView):
    paginate_by = 4
    model = Article
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Образовательный центр")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

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
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')


class ShowPost(DataMixin, DetailView):
    paginate_by = 3
    model = Article
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


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

    def get_queryset(self):
        return Article.objects.filter(is_published=True)


def info(request):
    return HttpResponse('Общая информация')


def p_advice(request):
    return HttpResponse('Попечительский совет')


def e_advice(request):
    return HttpResponse('Экспертный совет')


def docs(request):
    return HttpResponse('Документы')



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


def contacts(request):
    return HttpResponse('Контакты')


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


def lecture_hall(request):
    return HttpResponse('Лекториум')


#Пункт главного меню №3#
def teachers(request):
    return HttpResponse('Педагогам')


#Также является пунктом главного меню №5#
def programs(request):
    return HttpResponse('Программы')


def methodological_support(request):
    return HttpResponse('Методическое сопровождение')


def science_program(request):
    return HttpResponse('Наука')


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

#def index(request):
#    posts = Article.objects.all()
#    cats = Category.objects.all()

#    context = {
#            'cats': cats,
#            'posts': posts,
#            'menu': menu,
#            'title': 'Главная страница',
#            'cat_selected': 0,
#    }
#    return render(request, 'main/index.html', context=context)


#def about(request):
#    posts = Article.objects.all()
#    return render(request, 'main/about.html', {'menu': menu, 'title': 'О центре'})


#def addpage(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            try:
#                form.save()
#                return redirect('home')
#            except:
#                form.add_error(None, 'Ошибка добавления статьи')
#
#    else:
#        form = AddPostForm()
#    return render(request, 'main/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление документа")
        return dict(list(context.items()) + list(c_def.items()))






#def show_post(request, post_slug):
#    post = get_object_or_404(Article, slug=post_slug)
#
#    context = {
#        'post': post,
#        'menu': menu,
#        'title': post.title,
#        'cat_selected': post.cat_id,
#    }
#    return render(request, 'main/post.html', context=context)


#def show_category(request, cat_id):
#    posts = Article.objects.filter(cat_id=cat_id)
#    cats = Category.objects.all()
#
#    if len(posts) == 0:
#        raise Http404()
#

#    context = {
#        'cats': cats,
#        'posts': posts,
#        'menu': menu,
#        'title': 'Отображение по рубрикам',
#        'cat_selected': cat_id,
#    }
#    return render(request, 'main/index.html', context=context)







def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

