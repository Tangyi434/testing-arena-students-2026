"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""
import pytest
from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)


def test_parse_time_normal_values():
    assert parse_time("14:21") == 861
    assert parse_time("00:00") == 0
    assert parse_time("23:59") == 1439

def test_parse_time_invalid_values():
    with pytest.raises(ValueError):
        parse_time("30:80") # Invalid Time
        parse_time("9:5") # not enough numbers
        parse_time("10:10:10") # too many numbers
        parse_time("")

def test_parse_time_datatype():
    with pytest.raises(AttributeError):
        parse_time(29)
        parse_time(None)





def test_parse_measurement_normal_value():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    assert parse_measurement("Köln;14:21;21.7   ") == ("Köln", 861, 21.7)
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)

def test_parse_measurement_invalid_values():
    with pytest.raises(ValueError):
        parse_measurement("Köln;30:80;21.7") # Invalid Time
        parse_measurement("Köln;14:21;21.7;21.8") # too many parts
        parse_measurement("Köln;14:21;") # not enough parts
        parse_measurement(["Köln", "14:21", "21.7"])
        parse_measurement(None)
        parse_measurement("")






def test_filter_by_temperature_normal_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]

def test_filter_by_temperature_errors():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]
    
    with pytest.raises(ValueError):
        filter_by_temperature(measurements, 20.0, 15.0) # min > max
        filter_by_temperature(measurements, "20.0", "15.0") # Invalid Datatype
        filter_by_temperature(measurements, -5.0, -10.0) # measurements > max
        filter_by_temperature(None)






def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0

def test_average_temperature_errors():
    measurements = [
            ("Köln", 600, 10.0),
            ("Köln", 720, 20.0),
    ]
    with pytest.raises(ValueError):
        average_temperature(measurements, "Düsseldorf") # No Measurements
        average_temperature(None)
        average_temperature(232992)
        average_temperature(measurements, "koeln")







def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    measurements_multiple_max = [
                    ("Köln", 600, 25.0),
                    ("Düsseldorf", 720, 25.0),
                    ("Bonn", 600, 25.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)
    assert hottest_measurement(measurements_multiple_max) == ("Köln", 600, 25.0)
    assert hottest_measurement(measurements_multiple_max) == ("Köln", 600, 25.0)


def test_hottest_measurement_with_unique_maximum_errors():
    measurements = [
            ("Köln", 600, 10.0),
            ("Düsseldorf", 720, 25.0),
            ("Bonn", 900, 20.0),
    ]

    measurements_multiple_max = [
                ("Köln", 600, 25.0),
                ("Düsseldorf", 720, 25.0),
                ("Bonn", 900, 20.0),
    ]

    with pytest.raises(TypeError):
        hottest_measurement(None)
        hottest_measurement(3409)
        hottest_measurement(("Köln", 600, None))
        hottest_measurement(("Köln", 600))
