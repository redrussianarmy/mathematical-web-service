from functools import wraps

from rest_framework import status
from rest_framework.response import Response


def validator(serializer_cls):
    def deco_validator(func):
        @wraps(func)
        def func_validator(*args, **kwargs):
            request = args[0]
            serializer = serializer_cls(data=request.GET)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return func(*args, **kwargs, parameters=serializer)
        return func_validator
    return deco_validator
