from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from algorithms.serializers import FactorialParameterSerializer
from algorithms.decorators import validator
from algorithms.math.factorial import factorial
from algorithms.helpers import prepare_response


class Factorial(APIView):

    @method_decorator(validator(FactorialParameterSerializer))
    def get(self, _, parameters):
        '''
            Factorial n! of a non-negative integer
            Args:
                n: int
            Return:
                {
                    "result": int
                }
        '''
        n = parameters.data.get("n")
        result = factorial(n)

        return Response(data=prepare_response(result), status=status.HTTP_200_OK)
