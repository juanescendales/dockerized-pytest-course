from scripts.chp2.video4.mapmaker_challenge import Point
import pytest


def test_make_one_point():
    p1 = Point("Medellin", 13.4432, 17.6345)
    assert p1.latitiude_longitude == (13.4432, 17.6345)


def test_invalid_point_generation():
    with pytest.raises(ValueError) as exp:
        Point("Medellin", 0, -1500)
    assert str(exp.value) == "Invalid latitude, longitude combination."

    with pytest.raises(TypeError) as exp:
        Point(12, 0, -105)
    assert str(exp.value) == "Invalid city, must be a string"


