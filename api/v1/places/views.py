import datetime

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.v1.places.serializers import PlaceSerializer, PlaceDetailSerializer, CommentSerializer
from places.models import Place, Comment
from django.db.models import Q
from django.contrib.auth.models import User

from api.v1.places.pagination import StandadResultSetPagination

@api_view(["GET"])
@permission_classes([AllowAny])
def places(request):
    instances = Place.objects.filter(is_deleted=False)

    q = request.GET.get("q")
    if q:
        ids = q.split(",")
        instances = instances.filter(category__in=ids)

    paginator = StandadResultSetPagination()
    paginator_results = paginator.paginate_queryset(instances, request)

    context = {
        "request": request
    }

    serializer = PlaceSerializer(paginator_results, many=True, context=context)

    response_data = {
        "status_code": 6000,
        "count" : paginator.page.paginator.count,
        "links" : {
            "next" : paginator.get_next_link(),
            "previous" : paginator.get_previous_link(),
        },
        "data": serializer.data,
    }

    return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def place(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)

        context = {
            "request": request
        }

        serializer = PlaceDetailSerializer(instance, context=context)
        
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Place not exists",
        }

        return Response(response_data)


@api_view(["GET"])
@permission_classes([AllowAny])
def places(request):
    instances = Place.objects.filter(is_deleted=False)

    context = {
        "request": request
    }

    serializer = PlaceSerializer(instances, many=True, context=context)

    response_data = {
        "status_code": 6000,
        "data": serializer.data,
    }

    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)

        context = {
            "request": request
        }

        serializer = PlaceDetailSerializer(instance, context=context)
        
        response_data = {
            "status_code": 6000,
            "data": serializer.data,
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Place not exists",
        }

        return Response(response_data)



@api_view(["GET"])
@permission_classes([AllowAny])
def comment(request, pk):
    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)

        instances = Comment.objects.filter(place=place)

        context = {
            "request": request
        }

        serializer = CommentSerializer(instances, many=True, context=context)

        response_data = {
            "status_code": 6000,
            "data": serializer.data,
        }
         
    else:
        response_data = {
            "status_code": 6001,
            "message": "Place not exists",
        }

    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def comment_create(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)
        comment = request.data['comment'] 

        Comment.objects.create(
            user=request.user,
            comment=comment,
            place=instance,
            date=datetime.datetime.now()
        )

        response_data = {
            "status_code": 6000,
            "data": "successfully created",
        }

    else:
        response_data = {
            "status_code": 6001,
            "message": "Place not exists",
        }

    return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def like(request, pk):
    if Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)

        if instance.likes.filter(username=request.user.username).exists():
            instance.likes.remove(request.user)
            message = "Liked removed"
        else:
            instance.likes.add(request.user)
            message = "Liked added"

        response_data = {
            "status_code": 6000,
            "data": message,
        }

    else:
        response_data = {
            "status_code": 6001,
            "message": "Place not exists",
        }

    return Response(response_data)




    # if Place.objects.filter(pk=pk).exists():
    #     place = Place.objects.get(pk=pk)
    #     user = request.user

    #     liked = Like.objects.filter(user=user, place=place).count()

    #     if not liked:
    #         liked = Like.objects.create(user=user, place=place)
    #     else:
    #         liked = Like.objects.filter(user=user, place=place).delete()

    #     place.likes = Like.objects.filter(place=place).count()

    #     context = {
    #         "request": request
    #     }

    #     serializer = PlaceDetailSerializer(place, context=context)
        
    #     response_data = {
    #         "status_code": 6000,
    #         "data": serializer.data,
    #     }

    # else:
    #     response_data = {
    #         "status_code": 6001,
    #         "message": "Place not exists",
    #     }

    # return Response(response_data)

            
