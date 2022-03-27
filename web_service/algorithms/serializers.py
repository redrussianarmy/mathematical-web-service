from rest_framework.serializers import Serializer
from rest_framework.fields import IntegerField


class FibonacciParameterSerializer(Serializer):
    n = IntegerField(min_value=0, help_text="n:th Fibonacci Number")


class AckermannParameterSerializer(Serializer):
    m = IntegerField(min_value=0)
    n = IntegerField(min_value=0)


class FactorialParameterSerializer(Serializer):
    n = IntegerField(min_value=0, help_text="n:th Factorial")
