from health_app.health import Health
import pytest
import math

## Test __init__
def test_health_init_valid():
    user = Health("Nasir", 98, 1.85)

    assert user.name == "Nasir"
    assert user.weight_kg == 98
    assert user.height_m == 1.85

def test_health_init_invalid_empty_name():
    with pytest.raises(ValueError):
        Health("", 65, 1.74)

def test_health_init_invalid_empty_blank_name():
    with pytest.raises(ValueError):
        Health(" ", 65, 1.74)

def test_health_init_invalid_weight():
    with pytest.raises(ValueError):
        Health("John", -1, 1.90)

def test_health_init_invalid_height():
    with pytest.raises(ValueError):
        Health("Dave", 86, 0)

## Test calculate_bmi()
def test_health_calculate_bmi():
    user = Health("Shoaib", 74,1.76)
    result = user.calculate_bmi()

    assert result == round((74 / (1.76  ** 2)), 2)


## Test category_bmi()
def test_health_category_bmi_underweight():
    user = Health("Jake", 40, 1.7)
    result = user.category_bmi()

    assert result == "Underweight"

def test_health_category_bmi_normal():
    user = Health("Mariam", 65, 1.63)
    result = user.category_bmi()

    assert result == "Normal"

def test_health_category_bmi_overweight():
    user = Health("Bro", 90, 1.83)
    result = user.category_bmi()

    assert result == "Overweight"

def test_health_category_bmi_obese():
    user = Health("Jake", 200, 1.4)
    result = user.category_bmi()

    assert result == "Obese"

## Test get_health_advice()
def test_health_get_health_advice_underweight():
    user = Health("Jake", 40, 1.7)
    result = user.get_health_advice()

    assert result == "You are underweight. Consider increasing calorie intake with nutrient-dense foods. Strength training may help build muscle mass."

def test_health_get_health_advice_normal():
    user = Health("Mariam", 65, 1.63)
    result = user.get_health_advice()

    assert result == "Your BMI is in the healthy range. Maintain a balanced diet and regular physical activity. Continue your current habits."

def test_health_get_health_advice_overweight():
    user = Health("Bro", 90, 1.83)
    result = user.get_health_advice()

    assert result == "You are in the overweight range. Consider increasing physical activity. Small dietary improvements can help improve results."

def test_health_get_health_advice_obese():
    user = Health("Jake", 200, 1.4)
    result = user.get_health_advice()

    assert result == "Your BMI is in the obese range. Consider improving diet and increasing physical activity. Small consistent changes can improve health over time."

## Test get_ideal_weight()
def test_health_get_ideal_weight():
    user = Health("Dummy", 69, 1.75)
    result = user.get_ideal_weight()

    assert result == round(22 * math.pow(1.75, 2), 1)