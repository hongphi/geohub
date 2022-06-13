import json

from rest_framework.generics import ListAPIView, RetrieveAPIView

from geohub.core.adapters.product_adapter import ProductAdapter
from geohub.core.utils import create_log
from geohub.services.api.serializers import ProductSerializer


class BaseAPIView:
    def create_log(self):
        data = self.create_request_meta_json_object(self.request.META)
        path = self.request.get_full_path()
        create_log(path, data)

    def create_request_meta_json_object(self, meta_data):
        return {
            "REQUEST_METHOD": meta_data.get("REQUEST_METHOD"),
            "SERVER_SOFTWARE": meta_data.get("SERVER_SOFTWARE"),
            "REQUEST_METHOD": meta_data.get("REQUEST_METHOD"),
            "SCRIPT_NAME": meta_data.get("SCRIPT_NAME"),
            "PATH_INFO": meta_data.get("PATH_INFO"),
            "QUERY_STRING": meta_data.get("QUERY_STRING"),
            "REQUEST_URI": meta_data.get("REQUEST_URI"),
            "RAW_URI": meta_data.get("RAW_URI"),
            "REMOTE_ADDR": meta_data.get("REMOTE_ADDR"),
            "REMOTE_PORT": meta_data.get("REMOTE_PORT"),
            "SERVER_NAME": meta_data.get("SERVER_NAME"),
            "SERVER_PORT": meta_data.get("SERVER_PORT"),
            "SERVER_PROTOCOL": meta_data.get("SERVER_PROTOCOL"),
            "HTTP_X_REAL_IP": meta_data.get("HTTP_X_REAL_IP"),
        }


class ServicesView(BaseAPIView, ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        objs = []
        self.create_log()
        data = self.request.GET
        if data.get('query'):
            objs = ProductAdapter().search_product(data.get('query'))
        else:
            objs = ProductAdapter().find_all()

        sort_by = data.get('sort_by')
        if sort_by and sort_by in ['name', 'price']:
            objs = objs.order_by(sort_by)
        return objs


class ServiceDetailView(BaseAPIView, RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_object(self):
        self.create_log()
        return ProductAdapter().get_product(self.kwargs['slug'])
