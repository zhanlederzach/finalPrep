import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apiOld.models import Post
from apiOld.serializers import PostSerializer
from api.models import TaskList
from api.serializers import TaskSerializer2


@csrf_exempt
def posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    # мынау только  не работает пост
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = PostSerializer(data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def postsWithId(request, id):
    try:
        posts = Post.objects.get(id=id)
    except Post.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = PostSerializer(instance=posts, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        posts.delete()
        return JsonResponse({}, status=200)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def postsWithIdLike(request, id):
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
        serializer = TaskSerializer2(data=body)
        if serializer.is_valid():
            # create function from serializer

            task = serializer.save(task_list = TaskList.objects.get(id=id))
            task.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

    # try:
    #     tasklist = TaskList.objects.get(id=id)
    # except TaskList.DoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, status=404)
    # tasks_set = tasklist.task_set
    # tasks = tasks_set.all()
    # response = [x.to_json() for x in tasks]
    # return JsonResponse(response, safe=False)

