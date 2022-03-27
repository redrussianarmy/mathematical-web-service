from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator

from algorithms.serializers import AckermannParameterSerializer
from algorithms.decorators import validator
from algorithms.math.ackermann import ackermann
from algorithms.helpers import prepare_response


class Ackermann(APIView):

    @method_decorator(validator(AckermannParameterSerializer))
    def get(self, _, parameters):
        '''
            Ackermann Function
            Args:
                m: int
                n: int
            Return:
                {
                    "result": int
                }
        '''
        m = parameters.data.get("m")
        n = parameters.data.get("n")
        result = ackermann(m, n)

        return Response(data=prepare_response(result), status=status.HTTP_200_OK)
