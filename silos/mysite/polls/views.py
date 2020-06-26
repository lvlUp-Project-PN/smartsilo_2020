from django.shortcuts import render
from .models import *
from .serialize import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

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