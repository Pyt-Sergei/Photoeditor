from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import ImageModel
from . import utils
from . import filters


class List(APIView):
    def get(self, request):
        images = []
        for img in ImageModel.objects.all():
            images.append({
                'image': request.build_absolute_uri(img.image.url),
                'meta': {
                    'width': img.image.width,
                    'height': img.image.height,
                    'size': img.image.size,
                    'datetime': str(img.date)
                }
            })
        return Response(images)


class Resize(APIView):
    def post(self, request):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        width = int(request.data.get('width', img.image.width))
        height = int(request.data.get('height', img.image.height))

        utils.resize(img.image.path, (width, height))

        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class Scale(APIView):
    def post(self, request):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        width = int(request.data.get('width', img.image.width))
        height = int(request.data.get('height', img.image.height))

        utils.scale(img.image.path, size=(width, height))
        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class ScaleDynamic(APIView):
    def post(self, request, scaling):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        scaling = float(scaling)
        utils.scale(img.image.path, scaling=scaling)
        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class Crop(APIView):
    def post(self, request):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        left = int(request.data.get('left', 0))
        upper = int(request.data.get('upper', 0))
        right = int(request.data.get('right', img.image.width))
        lower = int(request.data.get('lower', img.image.height))

        utils.crop(img.image.path, (left, upper, right, lower))

        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class Rotate(APIView):
    def post(self, request, angle):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        utils.rotate(img.image.path, angle)

        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class Reverse(APIView):
    def post(self, request):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        utils.reverse(img.image.path)

        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size
            }
        })


class Filter(APIView):
    def post(self, request):
        img = request.data.get('image', '')
        if img == '':
            return Response({
                'status': 'Failed',
                'message': 'Please, upload an image'
            }, status=HTTP_204_NO_CONTENT)

        img = ImageModel(image=img)
        img.save()

        filter_name = request.data.get('filter', None)
        filter = filters.filters_dict.get(filter_name, None)
        if filter:
            if filter_name == 'blur':
                radius = int(request.data.get('radius', 5))
                filter(img.image.path, radius)
            elif filter_name == 'oil_painting':
                dst = int(request.data.get('dst', 7))
                filter(img.image.path, dst)
            else:
                filter(img.image.path)

        return Response({
            'status': 'OK',
            'image': request.build_absolute_uri(img.image.url),
            'meta': {
                'width': img.image.width,
                'height': img.image.height,
                'size': img.image.size,
            }
        })


