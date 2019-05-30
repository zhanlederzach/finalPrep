from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# @api_view(['GET', 'PUT', 'DELETE'])
# def taskFun(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist as e:
#         return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer2(task)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = TaskSerializer2(instance=task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)