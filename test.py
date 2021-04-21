from io import StringIO
import subprocess as sp
import os
from main import calculate_execution

list_addition = ["5+5", "10+5", "3+3"]
list_addition_results =["10", "15", "6"]

def test_addition():
    position = 0
    for i in list_addition:
        calculation = list_addition[position]
        result = calculate_execution(calculation)
        assert result == list_addition_results[position]
        position = position + 1
