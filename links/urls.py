from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.ShowLinksView.as_view(), name='links'),
    path('links/<str:username>', views.ShowCreatorLinksView.as_view(), name='creator-links'),
    path('news/add', views.Createlinks.as_view(), name='news-add'),

]