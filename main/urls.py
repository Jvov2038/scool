from django.conf.urls.static import static
from django.urls import path, re_path

from scool import settings
from .views import *


urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('programs/', programs, name='programs'),
    path('login/', LoginUser.as_view(), name='login'),
    path('sirius/', sirius, name='sirius'),
    path('big_challengers/', big_challengers, name='big_challengers'),
    path('olimpiada/', olimpiada, name='olimpiada'),
    path('docs/', docs, name='docs'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', MainCategory.as_view(), name='category'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

