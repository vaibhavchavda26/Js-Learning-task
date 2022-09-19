from register import models as register_model
from register import serializers as register_serializer
from rest_framework import views as rest_framework_views

from register.utils import create_response

class Register(rest_framework_views.APIView):
    def post(self,request):
        serializer_instance = register_serializer.RegisterSerializer(data=request.data)

        if not serializer_instance.is_valid():
            return create_response("Enter valid Data",400)
        else:
            register_model.RegisterForm.objects.create(
                first_name = request.data.get("first_name"),
                last_name = request.data.get("last_name"),
                phone_no = request.data.get("phone_no"),
                email = request.data.get("email"),
                password = request.data.get("password"),

            )
            return create_response("Data Added Successfully",200)

    def get(self,request):
        register_data = register_model.RegisterForm.objects.all()
        print("Get all the data",[obj.get_details() for obj in register_data])
        return create_response([obj.get_details() for obj in register_data],200)

class RegisterData(rest_framework_views.APIView):
    def get(self,request,id):
        register_data = register_model.RegisterForm.objects.filter(id=id).last()
        if register_data:
            return create_response(register_data.get_details(),200)
        else:
            return create_response("Enter valid id",200)

    def put(self,request,id):
        register_data = register_model.RegisterForm.objects.filter(id=id).last()
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone_no = request.data.get("phone_no")
        email = request.data.get("email")
        password = request.data.get("password")
        register_data.first_name = first_name
        register_data.last_name = last_name
        register_data.phone_no = phone_no
        register_data.email = email
        register_data.password = password
        if register_data:
            register_data.save()
            return create_response("Data Updated Successfully",200)
        else:
            return create_response("Please enter valid id",400)


    def delete(self,request,id):
        creds_data = register_model.RegisterForm.objects.filter(id=id).last()
        if creds_data:
            creds_data.delete()
            return create_response("Data Deleted Successfully",200)
        else:
            return create_response("Please Enter valid id",400)

       

        