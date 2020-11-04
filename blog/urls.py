from django.urls import path
from . import views
from Blognow import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('blog/', views.article, name='bloger'),
    path('blog/about', views.test, name='sell'),
    path('blog/categories/', views.homepage, name='blogero'),
    path('blog/categories/<int:id>', views.filto, name='filter'),
    path('blog/article/<int:id>', views.article_det, name='board_topics'),
    path('', views.landpage, name='land')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)