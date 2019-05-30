from django.http import Http404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Contact
from api.serializers import ContactSerializer


def getOwner(request):
    token = request.headers.get('Authorization')
    if token is None:
        return None
    token = token.split(' ')[1]
    owner = Token.objects.get(key=token).user
    return owner


# class TaskListsApi(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

class ContactsApi(APIView):
    # def get(self, request):
    #     contacts = Contact.objects.all()
    #     serializer = ContactSerializer(contacts, many=True)
    #     return Response(serializer.data)

    def get(self, request):

        print(request.query_params)
        query = request.query_params.get('query', [''])
        sort_by_name = request.query_params.get('sort_by_name', False)
        print(query)
        contacts = Contact.objects.filter(name__contains=query)
        if sort_by_name:
            contacts = contacts.order_by('name')

        print(contacts)
        response_data = []
        for c in contacts:
            serializer = ContactSerializer(c)
            my_or_not = False
            owner = getOwner(request)
            if owner is not None:
                if c.owner.id == owner.id:
                    my_or_not = True

            print(type(serializer.data))
            print(serializer.data)

            current = serializer.data

            current['my_or_not'] = my_or_not

            print(current)

            response_data.append(current)
        print(response_data)
        return Response(response_data)

    def post(self, request):
        token = request.headers.get('Authorization')
        token = token.split(' ')[1]
        user = Token.objects.get(key=token).user
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=user)
            my_or_not = True
            response_data = serializer.data
            response_data['my_or_not'] = my_or_not
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ContactApi(APIView):
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)

        my_or_not = False
        owner = getOwner(request)

        if owner is not None:
            if contact.owner.id == owner.id:
                my_or_not = True

        response_data = serializer.data
        response_data['my_or_not'] = my_or_not

        return Response(response_data)

    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(instance=contact, data=request.data)
        owner = getOwner(request)
        if owner is not None:
            if owner.id == contact.owner.id:
                if serializer.is_valid():
                    serializer.save(owner=owner)
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'errors': 'not allowed'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        owner = getOwner(request)
        contact = self.get_object(pk)
        if owner is not None:
            if owner.id == contact.owner.id:
                contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
