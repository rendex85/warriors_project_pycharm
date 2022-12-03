from django.db import transaction
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from warriors.models import Warrior
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from django.http import Http404
from django.shortcuts import render
from warriors.serializer import *

from .models import *


def get_warrior_data(request, id):  # отдельная страничка владельца функционально
    try:
        warrior = Warrior.objects.get(id=id)
    except Warrior.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'html/warrior.html', {'warrior': warrior})


class SkillAPIView(APIView):

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response({"Skills": serializer.data})


class SkillCreateView(APIView):

    def post(self, request):
        skill = request.data.get("skill")
        serializer = SkillCreateSerializer(data=skill)

        if serializer.is_valid(raise_exception=True):
            skill_saved = serializer.save()
            return Response({"Success": "Skill '{}' created".format(skill_saved.title)})
        else:
            return Response(status=400, data={"message": "not valid data"})


class WarriorAPIView(APIView):
    def get(self, request):
        warriors = Warrior.objects.all()
        serializer = WarriorSerializer(warriors, many=True)
        return Response({"Warriors": serializer.data})


class ProfessionCreateView(APIView):

    def post(self, request):
        print("REQUEST DATA", request.data)
        profession = request.data.get("profession")
        print("PROF DATA", profession)

        serializer = ProfessionCreateSerializer(data=profession)

        if serializer.is_valid(raise_exception=True):
            profession_saved = serializer.save()

        return Response({"Success": "Profession '{}' created succesfully.".format(profession_saved.title)})


class WarriorListAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorListRelatedAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorRelatedSerializer


class WarriorListDepthAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorDepthSerializer


class WarriorListNestedAPIView(generics.ListAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorNestedSerializer

    def post(self, request):
        serializer = WarriorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        serializer = WarriorSerializer(warrior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        warrior = get_object_or_404(Warrior, pk=pk)
        try:
            warrior.delete()
            return Response(status=200)
        except:
            return Response(status=400)


class WarriorCreateAPIView(generics.ListCreateAPIView):
    serializer_class = WarriorSerializer
    queryset = Warrior.objects.all()


class WarriorDestroyView(generics.DestroyAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorUpdateView(generics.UpdateAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


class WarriorDetailsView(generics.RetrieveAPIView):
    queryset = Warrior.objects.all()
    serializer_class = WarriorSerializer


# from rest_framework import generics
# Код для юрлов
# path('warrior/create', WarriorCreateAPIView.as_view()),
# path('warrior/detail/<int:pk>', WarriorDetailsView.as_view()),
# path('warrior/delete/<int:pk>', WarriorDestroyView.as_view()),
# path('warrior/update/<int:pk>', WarriorUpdateView.as_view()),


def get_warrior_data(request, id):  # отдельная страничка владельца функционально
    try:
        warrior = Warrior.objects.get(id=id)
    except Warrior.DoesNotExist:
        raise Http404("owner does not exist")
    return render(request, 'warrior.html', {'warrior': warrior})


class ProfessionCreateAPIView(generics.CreateAPIView):
    serializer_class = ProfessionCreateSerializer
    queryset = Profession.objects.all()


# @transaction.atomic
@api_view(['POST'])
def create_prof_and_connect_to_warrior(request):
    """
    Эндпоинт на создания профессии и привязки его к воину
    принимает следюущий словарь на вход:
    {
    "prof_name":"имя профессии",
    "prof_description":"Описание профессии",
    "warrior_id":2
    }
    """
    data = request.data
    new_prof = Profession.objects.create(title=data["prof_name"],
                                         description=data["prof_description"])
    warrior = Warrior.objects.get(id=data["warrior_id"])

    warrior.profession = new_prof
    warrior.save()

    return Response(status=201, data={"message": "objects created"})
