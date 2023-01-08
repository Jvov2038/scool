from django.conf.urls.static import static
from django.urls import path, re_path

from scool import settings
from .views import *


urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MainCategory.as_view(), name='category'),
    path('gallery/', Gallery.as_view(), name='gallery'),
    path('info/', info, name='info'),
    path('p_advice/', p_advice, name='p_advice'),
    path('e_advice/', e_advice, name='e_advice'),
    path('docs/', docs, name='docs'),
    path('partners/', partners, name='partners'),
    path('m_park/', m_park, name='m_park'),
    path('news/', News.as_view(), name='news'),
    path('contacts/', contacts, name='contacts'),
    path('big_challengers/', big_challengers, name='big_challengers'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('how_to_get/', how_to_get, name='how_to_get'),
    path('selection_criteria/', selection_criteria, name='selection_criteria'),
    path('online_application/', online_application, name='online_application'),
    path('stay_rules/', stay_rules, name='stay_rules'),
    path('accommodation_conditions/', accommodation_conditions, name='accommodation_conditions'),
    path('memo_for_parents/', memo_for_parents, name='memo_for_parents'),
    path('required_docs/', required_docs, name='required_docs'),
    path('faq', faq, name='FAQ'),
    path('lecture_hall/', lecture_hall, name='lecture_hall'),
    path('teachers/', teachers, name='teachers'),
    path('educational_programs/', programs, name='programs'),
    path('methodological_support/', methodological_support, name='methodological_support'),
    path('science_program/', science_program, name='science_program'),
    path('sports_program/', sports_program, name='sports_program'),
    path('culture_program/', culture_program, name='culture_program'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

