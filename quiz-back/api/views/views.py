import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Contact
from api.serializers import ContactSerializer


def hello(request):
    return HttpResponse('hello')

@csrf_exempt
def contacts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    # мынау только  не работает пост
    elif request.method == 'POST':
        token = request.headers.get('Authorization')
        token = token.split(' ')[1]
        user = Token.objects.get(key=token).user

        body = json.loads(request.body)
        serializer = PostSerializer(data=body)
        if serializer.is_valid():

            serializer.save(created_by=user)
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer2(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            # create function from serializer
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_lists_with_id(request, id):
    # try:
    #     return JsonResponse(TaskList.objects.get(id=id).to_json(), safe=False)
    # except TaskList.DoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, status=404)
    try:
        task_list = TaskList.objects.get(id=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer2(task_list)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(instance=task_list, data=body)
        if serializer.is_valid():
            # update function from serializer
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=200)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def tasks_of_tasklist_with_id(request, id):
    try:
        tasklist = TaskList.objects.get(id=id)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)
    if request.method == 'GET':
        tasks_set = tasklist.task_set
        tasks = tasks_set.all()
        serializer = TaskSerializer2(tasks, many=True)
        response = serializer.data
        return JsonResponse(response, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        # serializer = TasksSerializer(task_list=TaskList.objects.get(id=id), data=body)
        serializer = TaskSerializer2(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

    # try:
    #     tasklist = TaskList.objects.get(id=id)s
    # except TaskList.DoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, status=404)
    # tasks_set = tasklist.task_set
    # tasks = tasks_set.all()
    # response = [x.to_json() for x in tasks]
    # return JsonResponse(response, safe=False)


@csrf_exempt
def task(request, id):
    try:
        task = Task.objects.get(id=id)
        if request.method == 'DELETE':
            task.delete()
            return JsonResponse(task.to_json(), safe=False)
            pass
        elif request.method == 'PUT':
            body = json.loads(request.body)
            serializer = TaskSerializer2(instance=task, data=body)
            if serializer.is_valid():
                # update function from serializer
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors)
        else:
            return JsonResponse(Task.objects.get(id=id).to_json(), safe=False)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=404)
