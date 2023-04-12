from django.db.models import Count

from .models import *

menu = [
    {'title': "О центре", 'url_name': 'about',
     'submenu': [{'title': 'Общая информация', 'url_name': 'info'},
                 {'title': 'Попечительский совет', 'url_name': 'p_advice'},
                 {'title': 'Экспертный совет', 'url_name': 'e_advice'},
                 {'title': "Документы", 'url_name': 'docs'},
                 {'title': 'Новости', 'url_name': 'news'},
                 {'title': 'Контакты', 'url_name': 'contacts'},
                 ]},
    {'title': 'Как попасть', 'url_name': 'how_to_get',
     'submenu': [{'title': 'Критерии отбора', 'url_name': 'selection_criteria'},
                 {'title': 'Правила пребывания', 'url_name': 'stay_rules'},
                 {'title': 'Условия размещения', 'url_name': 'accommodation_conditions'},
                 {'title': 'Памятка для родителей', 'url_name': 'memo_for_parents'},
                 {'title': 'Необходимые документы', 'url_name': 'required_docs'},
                 {'title': 'Часто задаваемые вопросы', 'url_name': 'FAQ'},
                 {'title': 'Лекториум', 'url_name': 'lecture_hall'}
                 ]},
    {'title': "Мероприятия", 'url_name': 'events',
     'submenu': [{'title': 'Большие вызовы', 'url_name': 'big_challengers'},
                 {'title': 'Сириус лето', 'url_name': 'sirius_leto'},
                 ]},
    {'title': 'Программы', 'url_name': 'educational_programs'}]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
