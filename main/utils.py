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
                     {'title': 'Заявка онлайн', 'url_name': 'online_application'},
                     {'title': 'Правила пребывания', 'url_name': 'stay_rules'},
                     {'title': 'Условия размещения', 'url_name': 'accommodation_conditions'},
                     {'title': 'Памятка для родителей', 'url_name': 'memo_for_parents'},
                     {'title': 'Необходимые документы', 'url_name': 'required_docs'},
                     {'title': 'Часто задаваемые вопросы', 'url_name': 'FAQ'},
                     {'title': 'Лекториум', 'url_name': 'lecture_hall'}
                     ]},
        {'title': 'Педагогам', 'url_name': 'teachers',
         'submenu': [{'title': 'Программы', 'url_name': 'programs'},
                     {'title': 'Методическое сопровождение', 'url_name': 'methodological_support'}
                     ]},
        {'title': "Добавить документ", 'url_name': 'add_page'},
        {'title': 'Программы', 'url_name': 'programs',
         'submenu': [{'title': 'Наука', 'url_name': 'science_program'},
                     {'title': 'Спорт', 'url_name': 'sports_program'},
                     {'title': 'Культура', 'url_name': 'culture_program'}
                     ]},

        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('article'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(3)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

