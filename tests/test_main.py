from tests.helpers import press_sequence
from app.main import calculate_execution

list_addition = ["5+5", "10+5", "3+3", "-5+5"]
list_addition_results =["10", "15", "6", "0"]

list_substraction = ["5-5", "200-15", "400-40", "500-200"]
list_substraction_results =["0", "185", "360", "300"]

list_division = ["10/5", "200/10", "30/5", "-10/2"]
list_division_results =["2", "20", "6", "-5"]

list_multiplication = ["5*5", "200*10", "2*5", "2*25"]
list_multiplication_results =["25", "2000", "10", "50"]

list_decimals = ["0.5*5", "2+0.10", "0.2-0.5", "2/0.25"]
list_decimals_results =["2.5", "2.1", "-0.3", "8"]

list_composite = ["2*3*3*2", "3+2+6-2", "2.5+2.5*3*4-2", "-2/-2+4+5"]
list_composite_results =["36", "9", "30.5", "10"]


#Testing Inputs 
def test_input_sum():
    assert press_sequence('1 + 2 =') == '3'

def test_input_sub():
    assert press_sequence('5 - 1 5 =') == '-10'

def test_input_negneg():
    assert press_sequence('- 1 - - 2 =') == '1'

def test_input_clear_screen():
    assert press_sequence('1 + 2 AC') == ''

def test_input_decimals():
    assert press_sequence('0 . 2 * 0 . 5 =') == '0.1'

def test_zero_division():
    assert press_sequence('5 / 0 =') == 'Error'


#Testing the str(eval) function to make sure its working well
def test_addition():
    position = 0
    for i in list_addition:
        calculation = list_addition[position]
        result = calculate_execution(calculation)
        assert result == list_addition_results[position]
        position = position + 1

def test_substraction():
    position = 0
    for i in list_substraction:
        calculation = list_substraction[position]
        result = calculate_execution(calculation)
        assert result == list_substraction_results[position]
        position = position + 1

def test_division():
    position = 0
    for i in list_division:
        calculation = list_division[position]
        result = calculate_execution(calculation)
        assert result == list_division_results[position]
        position = position + 1

def test_multiplication():
    position = 0
    for i in list_multiplication:
        calculation = list_multiplication[position]
        result = calculate_execution(calculation)
        assert result == list_multiplication_results[position]
        position = position + 1

def test_decimals():
    position = 0
    for i in list_decimals:
        calculation = list_decimals[position]
        result = calculate_execution(calculation)
        assert result == list_decimals_results[position]
        position = position + 1

def test_composite_operations():
    position = 0
    for i in list_composite:
        calculation = list_composite[position]
        result = calculate_execution(calculation)
        assert result == list_composite_results[position]
        position = position + 1

        
