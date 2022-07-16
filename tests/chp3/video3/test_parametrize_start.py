import os
import pytest

from scripts import data_processor, data_aggregator


@pytest.fixture(scope="module")
def city_list_location():
    return 'tests/resources/cities/'


@pytest.fixture(scope="module")
def process_data(city_list_location):
    files = os.listdir(city_list_location)

    def _specify_type(file_name_or_type: str):
        for f in files:
            if file_name_or_type in f:
                if not file_name_or_type.endswith('.json'):
                    data = data_processor.csv_reader(city_list_location + f)
                else:
                    data = data_processor.json_reader(city_list_location + f)
        return data

    yield _specify_type


@pytest.mark.parametrize("country,stat,expected", [
    ('Andorra', 'Mean', 1641.42),
    ('Andorra', 'Median', 1538.02),
    ('Argentina', 'Median', 125.0)
])
def test_stat_atitude_per_country(country, stat, expected, process_data):
    data = process_data(file_name_or_type="clean_map.csv")
    andorran_avg_res = data_aggregator.atitude_stat_per_country(data, country, stat)

    assert andorran_avg_res == {'Country': country, stat: expected}
