from converter import celsius_to_fahrenheit, km_to_miles

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 213

def test_km_to_miles():
    assert round(km_to_miles(10), 2) == 6.21
