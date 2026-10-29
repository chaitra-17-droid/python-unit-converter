from converter import celsius_to_fahrenheit, km_to_miles, kg_to_pounds

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212

def test_km_to_miles():
    assert round(km_to_miles(10), 2) == 6.21

def test_kg_to_pounds():
    assert round(kg_to_pounds(10), 2) == 22.05
