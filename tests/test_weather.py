"""Starter tests for the weather module.

These tests deliberately cover only ordinary examples. They show how pytest works,
but they are not a sufficient test suite for the specification in SPECIFICATION.md.
"""

from weather import (
    average_temperature,
    filter_by_temperature,
    hottest_measurement,
    parse_measurement,
    parse_time,
)
import pytest


def test_parse_time_regular_time():
    assert parse_time("14:21") == 861
    with pytest.raises(ValueError):
        parse_time("25:00")  # Invalid hour
        parse_time("14:61")  # Invalid minute
        parse_time("14:2")   # Invalid format
        parse_time("14-21")  # Invalid separator
        parse_time("14:21:00")  # Extra seconds
        parse_time(None)  # Invalid input type


def test_parse_measurement_regular_line():
    assert parse_measurement("Köln;14:21;21.7") == ("Köln", 861, 21.7)
    with pytest.raises(ValueError):
        parse_measurement("Köln;25:00;21.7")  # Invalid time
        parse_measurement("Köln;14:21;21.7;extra")  # Too many parts
        parse_measurement("Köln;14:21")  # Too few parts
        parse_measurement("Köln;14:21;not_a_number")  # Invalid temperature
        parse_measurement("Köln;14:21;")  # Missing temperature
        parse_measurement(";14:21;21.7")  # Missing city
        parse_measurement(123)  # Invalid input type
        parse_measurement(None)  # Invalid input type
        parse_measurement("")  # Empty string
        parse_measurement("Köln ;  14:21 ; 21.7")  # Extra space


def test_filter_by_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 18.5),
        ("Bonn", 900, 25.0),
    ]

    assert filter_by_temperature(measurements, 15.0, 20.0) == [
        ("Düsseldorf", 720, 18.5)
    ]
    with pytest.raises(ValueError):
        filter_by_temperature(measurements, 20.0, 15.0)  # min_temp > max_temp
        filter_by_temperature(None)
        filter_by_temperature(measurements, 15.0, 20.0)  # dopple check for valid range
        filter_by_temperature(measurements, -5.0, -10.0)  # measurement > max_temp


def test_average_temperature_regular_values():
    measurements = [
        ("Köln", 600, 10.0),
        ("Köln", 720, 20.0),
    ]

    assert average_temperature(measurements, "Köln") == 15.0
    with pytest.raises(ValueError):
        average_temperature(measurements, "Düsseldorf")  # No measurements for this city
        average_temperature(measurements, 123)  # Invalid city type
        average_temperature(None, "Köln")  # Empty measurements list
        average_temperature(measurements, "koeln")  # Case-sensitive city name


def test_hottest_measurement_with_unique_maximum():
    measurements = [
        ("Köln", 600, 10.0),
        ("Düsseldorf", 720, 25.0),
        ("Bonn", 900, 20.0),
    ]

    assert hottest_measurement(measurements) == ("Düsseldorf", 720, 25.0)
    with pytest.raises(ValueError):
        hottest_measurement([])  # Empty measurements list
        hottest_measurement([("Köln", 600, "hot")])  # Invalid temperature type
        hottest_measurement([("Köln", None, 10.0)])    # Invalid time type
        hottest_measurement([("Köln", 600)])  # Missing temperature
        hottest_measurement([("Köln",)])  # Missing time and temperature
    with pytest.raises(TypeError):
        hottest_measurement(None)  # Invalid input type
        hottest_measurement("not a list")  # Invalid input type 