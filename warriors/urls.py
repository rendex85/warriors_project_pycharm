"""warriors_project_pycharm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from warriors import views
from django.urls import path
from .views import *

urlpatterns = [
    path('warrior/<int:id>/', views.get_warrior_data),
    path('skills/', SkillAPIView.as_view()),
    path('skills/create/', SkillCreateView.as_view()),
    path('warriors/', WarriorAPIView.as_view()),
    path('warrior/create', WarriorCreateAPIView.as_view()),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),

    path('warrior_templ/<int:id>/', get_warrior_data),


    path('warriors1/', WarriorAPIView.as_view()),
    path('warriors/list/', WarriorListAPIView.as_view()),
    path('warriors/list/related/', WarriorListRelatedAPIView.as_view()),
    path('warriors/list/depth/', WarriorListDepthAPIView.as_view()),
    path('warriors/list/nested/', WarriorListNestedAPIView.as_view()),

    path('profession/create/', ProfessionCreateView.as_view()),
    path('profession/generic_create/', ProfessionCreateAPIView.as_view()),
    path('profession/create_with_warrior', create_prof_and_connect_to_warrior),

    path('warrior/create1', WarriorCreateAPIView.as_view()),
    path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
    path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
    path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),

]
