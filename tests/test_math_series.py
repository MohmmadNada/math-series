from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series
def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_0():
    exept_result=0
    acual_result=fibonacci(0)
    assert exept_result == acual_result

def test_fibonacci_1():
    exept_result=1
    acual_result=fibonacci(1)
    assert exept_result == acual_result


def test_fibonacci_7():
    exept_result=13
    acual_result=fibonacci(7)
    assert exept_result == acual_result

def test_lucas_zero():
    except_result=2
    acual_result=lucas(0)
    assert except_result==acual_result
def test_lucas_one():
    except_result=1
    acual_result=lucas(1)
    assert except_result==acual_result
def test_lucas_seven():
    except_result=29
    acual_result=lucas(7)
    assert except_result==acual_result
def test_sum_series():
    except_result_7=13
    acual_result_7=sum_series(7)
    # input or 0, 0,
    except_result_0=0
    acual_result_0=sum_series(0)
    # input 5 ,2,1
    except_result_5=11
    acual_result_5=sum_series(5,2,1)
    # inpit irrgual (3,3,1)
    except_result_irrgual=5
    acual_result_irrgual=sum_series(3,3,1)
    assert except_result_7==acual_result_7 and except_result_7==sum_series(7,0,1)
    assert except_result_0==acual_result_0 and except_result_0==sum_series(0,0,1)
    assert except_result_irrgual==acual_result_irrgual