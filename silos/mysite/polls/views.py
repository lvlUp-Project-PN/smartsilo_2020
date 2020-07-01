from django.shortcuts import render, get_object_or_404
from .models import *
from .serialize import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.db import models
# Create your views here.
from django.http import HttpResponse
import os

def index(request):
    return HttpResponse("Hello, world.")

def chart (request, pk):

    silosobj= SilosAvgDay.objects.all().filter(silos_code=pk)
    path1 = os.path.join(os.getcwd(),'polls\static\polls\csv\day_avg.csv')
    if os.path.exists(path1):
        os.remove(path1)
    with open(path1, 'a') as csvfile1:
        csvfile1.write('date,value\n')
        for item in silosobj:
            csvfile1.write(f'{item.day},{int(item.day_avg)}\n')

    silosobj2= SilosAvgWeek.objects.all().filter(silos_code=pk)
    path2 = os.path.join(os.getcwd(),'polls\static\polls\csv\week_avg.csv')
    if os.path.exists(path2):
        os.remove(path2)
    with open(path2, 'a') as csvfile2:
        csvfile2.write('date,value\n')
        for item in silosobj2:
            csvfile2.write(f'{item.start_date},{int(item.week_avg)}\n')

    silosobj3= SilosAvgMonth.objects.all().filter(silos_code=pk)
    path3 = os.path.join(os.getcwd(),'polls\static\polls\csv\month_avg.csv')
    if os.path.exists(path3):
        os.remove(path3)
    with open(path3, 'a') as csvfile3:
        csvfile3.write('date,value\n')
        for item in silosobj3:
            csvfile3.write(f'{item.date},{int(item.month_avg)}\n')

    return render(request, 'graphs.html')

def siloscount(request):

    silosobj= Silos.objects.values('site_id').distinct()

    context = {'count': silosobj}


    return render(request, 'home.html', context )

def silosvalue (request, pk):
    #if(pk=='0000'):

        #silosobj = SilosDataIrt.objects.all()
    silosobj = SilosDataIrt.objects.filter(silos_code__startswith=pk).order_by('-id')[:2]


    #if(pk=='0001'):
        #silosobj = SilosDataIrt.objects.all().order_by('-id').distinct()[0:2]


    silosobj2= Silos.objects.values('site_id').distinct()
    context = {'siteresult': silosobj, 'count': silosobj2}

    return render(request, 'home2.html', context )

class SilosDataIrtTable(APIView):

    def get(self,request):
        silosirtobj= SilosDataIrt.objects.all()
        silosirtserializeobj= SilosDataIrtSerialize(silosirtobj,many=True)
        return Response(silosirtserializeobj.data)

    def post(self,request):
        serializeobj= SilosDataIrtSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosDataIrtUpdateDel(APIView):
    def get_object(self,pk):
        try:
            return SilosDataIrt.objects.get(pk=pk)
        except SilosDataIrt.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosirtobj=self.get_object(pk)
        serializeobj=SilosDataIrtSerialize(silosirtobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosirtobj=self.get_object(pk)
        silosirtserializeobj=SilosDataIrtSerialize(silosirtobj,data=request.data)
        if silosirtserializeobj.is_valid():
            silosirtserializeobj.save()
            return Response(silosirtserializeobj.data,status.HTTP_200_OK)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosirtobj=self.get_object(pk)
        silosirtobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginEmailTable(APIView):

    def get(self,request):
        loginmailobj= LoginEmail.objects.all()
        loginmailserializeobj= LoginEmailSerialize(loginmailobj,many=True)
        return Response(loginmailserializeobj.data)

    def post(self,request):
        loginmailobj= LoginEmailSerialize(data=request.data)
        if loginmailobj.is_valid():
            loginmailobj.save()
            return Response(loginmailobj.data,status=status.HTTP_201_CREATED)
        return Response(loginmailobj.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginEmailUpdateDel(APIView):
    def get_object(self,pk):
        try:
            return LoginEmail.objects.get(pk=pk)
        except LoginEmail.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        loginmailobj=self.get_object(pk)
        serializeobj=LoginEmailSerialize(loginmailobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        loginmailobj=self.get_object(pk)
        loginmailserializeobj=LoginEmailSerialize(loginmailobj,data=request.data)
        if loginmailserializeobj.is_valid():
            loginmailserializeobj.save()
            return Response(loginmailserializeobj.data,status.HTTP_200_OK)
        return Response(loginmailserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        loginmailobj=self.get_object(pk)
        loginmailobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginPermissionsTable(APIView):

    def get(self,request):
        loginpermobj= LoginPermissions.objects.all()
        loginpermserializeobj= LoginPermissionsSerialize(loginpermobj,many=True)
        return Response(loginpermserializeobj.data)

    def post(self,request):
        serializeobj= LoginPermissionsSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginPermissionsUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return LoginPermissions.objects.get(pk=pk)
        except LoginPermissions.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        loginpermobj=self.get_object(pk)
        serializeobj=LoginPermissionsSerialize(loginpermobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        loginpermobj=self.get_object(pk)
        loginpermserializeobj=LoginPermissionsSerialize(loginpermobj,data=request.data)
        if loginpermserializeobj.is_valid():
            loginpermserializeobj.save()
            return Response(loginpermserializeobj.data,status.HTTP_200_OK)
        return Response(loginpermserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        loginpermobj=self.get_object(pk)
        loginpermobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginUserTable(APIView):

    def get(self,request):
        loginuserobj= LoginEmail.objects.all()
        loginuserserializeobj= LoginUserSerialize(loginuserobj,many=True)
        return Response(loginuserserializeobj.data)

    def post(self,request):
        loginuserobj= LoginUserSerialize(data=request.data)
        if loginuserobj.is_valid():
            loginuserobj.save()
            return Response(loginuserobj.data,status=status.HTTP_201_CREATED)
        return Response(loginuserobj.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return LoginUser.objects.get(pk=pk)
        except LoginUser.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        loginuserobj=self.get_object(pk)
        serializeobj=LoginUserSerialize(loginuserobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        loginuserobj=self.get_object(pk)
        loginuserserializeobj=LoginUserSerialize(loginuserobj,data=request.data)
        if loginuserserializeobj.is_valid():
            loginuserserializeobj.save()
            return Response(loginuserserializeobj.data,status.HTTP_200_OK)
        return Response(loginuserserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        loginuserobj=self.get_object(pk)
        loginuserobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosAvgDayTable(APIView):

    def get(self,request):
        silosobj= SilosAvgDay.objects.all()
        silosserializeobj= SilosAvgDaySerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosAvgDaySerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosAvgDayUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosAvgDay.objects.get(pk=pk)
        except SilosAvgDay.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosAvgDaySerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosAvgDaySerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosAvgWeekTable(APIView):

    def get(self,request):
        silosobj= SilosAvgWeek.objects.all()
        silosserializeobj= SilosAvgWeekSerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosAvgWeekSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosAvgWeekUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosAvgWeek.objects.get(pk=pk)
        except SilosAvgWeek.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosAvgWeekSerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosAvgWeekSerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosAvgMonthTable(APIView):

    def get(self,request):
        silosobj= SilosAvgMonth.objects.all()
        silosserializeobj= SilosAvgMonthSerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosAvgMonthSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosAvgMonthUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosAvgWeek.objects.get(pk=pk)
        except SilosAvgWeek.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosAvgMonthSerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosAvgMonthSerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosTable(APIView):

    def get(self,request):
        silosobj= Silos.objects.all()
        silosserializeobj= SilosSerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return Silos.objects.get(pk=pk)
        except Silos.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosSerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosSerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosErrorTable(APIView):

    def get(self,request):
        silosobj= SilosError.objects.all()
        silosserializeobj= SilosErrorSerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosErrorSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosErrorUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosError.objects.get(pk=pk)
        except SilosError.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosErrorSerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosErrorSerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosErrorCategoryTable(APIView):

    def get(self,request):
        silosobj= SilosErrorCategory.objects.all()
        silosserializeobj= SilosErrorCategorySerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosErrorCategorySerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosErrorCategoryUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosErrorCategory.objects.get(pk=pk)
        except SilosErrorCategory.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosErrorCategorySerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosErrorCategorySerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SilosSpecsTable(APIView):

    def get(self,request):
        silosobj= SilosSpecs.objects.all()
        silosserializeobj= SilosSpecsSerialize(silosobj,many=True)
        return Response(silosserializeobj.data)

    def post(self,request):
        serializeobj= SilosSpecsSerialize(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(serializeobj.data,status=status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

class SilosSpecsUpdateDel(APIView):

    def get_object(self,pk):
        try:
            return SilosSpecs.objects.get(pk=pk)
        except SilosSpecs.DoesNotExist:
            return Response(serializeobj.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,pk):
        silosobj=self.get_object(pk)
        serializeobj=SilosSpecsSerialize(silosobj)
        return Response(serializeobj.data)

    def put(self,request,pk):
        silosobj=self.get_object(pk)
        silosserializeobj=SilosSpecsSerialize(silosobj,data=request.data)
        if silosserializeobj.is_valid():
            silosserializeobj.save()
            return Response(silosserializeobj.data,status.HTTP_200_OK)
        return Response(silosserializeobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        silosobj=self.get_object(pk)
        silosobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
