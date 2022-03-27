from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from algorithms.serializers import FibonacciParameterSerializer
from algorithms.decorators import validator
from algorithms.math.fibonacci import fibonacci
from algorithms.helpers import prepare_response


class Fibonacci(APIView):

    @method_decorator(validator(FibonacciParameterSerializer))
    def get(self, _, parameters):
        '''
            nth Fibonacci Number
            Args:
                n: int
            Return:
                {
                    "result": int
                }
        '''
        n = parameters.data.get("n")
        result = fibonacci(n)

        return Response(data=prepare_response(result), status=status.HTTP_200_OK)
