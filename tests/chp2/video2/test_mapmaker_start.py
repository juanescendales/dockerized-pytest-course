from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("Medellin", 13.4432, 17.6345)
    assert p1.latitiude_longitude == (13.4432, 17.6345)
