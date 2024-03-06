from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.v1.products.serializers import *
from products.models import Category




@api_view(['POST'])
@permission_classes((AllowAny,))
def create_category(request):
    try:

        user_group = request.user.groups.all()[0]
    except:
        user_group = None
    user_group = str(user_group)

    serializer = CreateCategorySerializer(data=request.data)
    if serializer.is_valid():
        if user_group == "None":

            title = serializer.data["title"]
            featured_image = serializer.validated_data['featured_image']


            category, created = Category.objects.get_or_create(
                title=title,
            )

            if created:
                category.featured_image = featured_image

                category.save()
                response_data = {
                    "status": 6000,
                    "title": "success",
                    "message": "category created"
                }

            else:
                response_data = {
                    "status": 6001,
                    "title": "failed",
                    "message": "category already existed"
                }
        else:
            response_data = {
                "status": 6001,
                "title": "permission denied",
                "message": "you are not permitted to do this action!!!"
            }

    else:
        response_data = {
            "status": 6000,
            "title": "failed",
            "message": serializer._errors
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((AllowAny,))
def fetch_categories(request):
    instances = Category.objects.all()
    if instances:
        serializer = FetchCategoriesSerializer(instance=instances, many=True, context={"request": request})

        response_data = {
            "status": 6000,
            "title": "success",
            "data": serializer.data
        }

    else:
        response_data = {
            "status": 6000,
            "title": "failed",
            "message": "Data not found"
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_product(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_product(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_category(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_featured(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_featured(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_product_image(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_product_image(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_product_size(request):
    pass


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def edit_product_size(request):
    pass