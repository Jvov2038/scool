from django.db.models import Count

from .models import *

menu = [
        {'title': "О центре", 'url_name': 'about',
         'submenu': [{'title': 'Общая информация', 'url_name': 'info'},
                     {'title': 'Попечительский совет', 'url_name': 'p_sovet'},
                     {'title': 'Экспертный совет', 'url_name': 'e_sovet'}]},
        {'title': "Добавить документ", 'url_name': 'add_page'},
        {'title': "Программы", 'url_name': 'programs',
         'submenu': [{'title': 'Сириус Лето', 'url_name': 'sirius'},
                     {'title': 'Большие вызовы', 'url_name': 'big_challengers'},
                     {'title': 'Всеросийская олимпиада школьников', 'url_name': 'olimpiada'}]},
        {'title': "Документы", 'url_name': 'docs'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('article'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

