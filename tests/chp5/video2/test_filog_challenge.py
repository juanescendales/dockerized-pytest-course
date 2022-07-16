from datetime import datetime
import pytest
from scripts.fitness_log import FitnessLog


@pytest.fixture(scope='function')
def activity_data():
    yield {
        'activity': 'run',
        'start_time': datetime(year=2017, month=1, day=1, hour=5, minute=12),
        'end_time': datetime(year=2017, month=1, day=1, hour=5, minute=55)
    }


@pytest.fixture(scope='function')
def create_tracker(activity_data):
    fitness_tracker = FitnessLog()
    # breakpoint()
    fitness_tracker.log_activity(
        activity_data['activity'],
        activity_data['start_time'], activity_data['end_time'])

    yield fitness_tracker


def test_add_valid_activities(create_tracker):
    fitness_tracker = create_tracker
    # breakpoint()
    activities = fitness_tracker.get_activities()

    assert len(activities) == 1
    assert activities[0][0] == 'run'


@pytest.fixture(scope='session')
def create_overlapping_times():
    overlapping_start_time = datetime(year=2017, month=1, day=1, hour=5, minute=14)
    overlapping_end_time = datetime(year=2017, month=1, day=1, hour=5, minute=53)

    return overlapping_start_time, overlapping_end_time


def test_add_invalid_activity(create_tracker, create_overlapping_times):
    fitness_tracker = create_tracker
    overlapping_start_time, overlapping_end_time = create_overlapping_times

    with pytest.raises(Exception) as exp:
        fitness_tracker.log_activity("cook", overlapping_start_time, overlapping_end_time)

    assert str(exp.value) == ('A new activity must not conflict with a logged activity. ' +
                              'Please delete the old activity before proceeding')
"""
 TO DO: Add a new test.
 You can run the following to expose which test functions
 and paths are covered:

 pytest --cov scripts
"""


def test_delete_activity(create_tracker, activity_data):  # change function name here
    fitness_tracker = create_tracker
    activities = fitness_tracker.get_activities()
    assert len(activities) == 1

    fitness_tracker.delete_activity(
        "cooking",
        activity_data['start_time'], activity_data['end_time'])
    activities = fitness_tracker.get_activities()
    assert len(activities) == 1

    fitness_tracker.delete_activity(
        activity_data['activity'],
        activity_data['start_time'], activity_data['end_time'])

    activities = fitness_tracker.get_activities()
    assert len(activities) == 0
