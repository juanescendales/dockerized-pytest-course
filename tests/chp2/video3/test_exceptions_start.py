from scripts.chp2.video3.mapmaker_exceptions_start import Point
import pytest


def test_make_one_point():
    p1 = Point("Medellin", 13.4432, 17.6345)
    assert p1.latitiude_longitude == (13.4432, 17.6345)


def test_invalid_point_generation():  # TO DO
    with pytest.raises(ValueError) as exp:
        Point("Medellin", 0, -105)
    assert str(exp.value) == "Not valid latitude or longitude"
