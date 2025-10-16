"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


def test_daily_mean_zeros():
    """Test that mean function works for an array of zeros."""
    from inflammation.models import daily_mean

    test_input = np.array([[0, 0],
                           [0, 0],
                           [0, 0]])
    test_result = np.array([0, 0])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)


def test_daily_mean_integers():
    """Test that mean function works for an array of positive integers."""
    from inflammation.models import daily_mean

    test_input = np.array([[1, 2],
                           [3, 4],
                           [5, 6]])
    test_result = np.array([3, 4])

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test_input), test_result)

import numpy.testing as npt
@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        (
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None,
        ),
        (
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None,
        ),
        (
            [[float('nan'), 1, 1], [1, 1, 1], [1, 1, 1]],
            [[0, 1, 1], [1, 1, 1], [1, 1, 1]], None,
        ),
        (
            [[1, 2, 3], [4, 5, float('nan')], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.8, 1, 0], [0.78, 0.89, 1]], None,
        ),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]], ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]], None,
        ),
                (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
...

import pytest
from inflammation.models import Patient
import numpy.testing as npt


class TestPatient:
    def setup_class(self):
        self.patient1 = Patient(id=1, data=[1, 2, 3, 4, 5])
        self.patient2 = Patient(id=2, data=[10, 20, 30, 40, 50])

    def test_patient_data_mean(self):
        assert self.patient1.data_mean() == 3.0

    def test_patient_data_max(self):
        assert self.patient1.data_max() == 5

    def test_patient_data_min(self):
        assert self.patient1.data_min() == 1

    def test_patient_attributes(self):
        assert self.patient2.id == 2
        assert self.patient2.data == [10, 20, 30, 40, 50]

from inflammation.models import Trial

@pytest.fixture()
def trial_instance():
    return Trial(np.array([[0, 0],[0, 0]]), 1)

class TestTrial:
    def test_daily_mean_zeros(self, trial_instance):
        """Test that mean function works for an array of zeros."""
        trial_instance.data = np.array([
            [0, 0],
            [0, 0],
            [0, 0]])
        test_result = np.array([0, 0])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_instance.daily_mean(), test_result)


    def test_daily_mean_integers(self, trial_instance):
        """Test that mean function works for an array of positive integers."""

        trial_instance.data = np.array([
            [1, 2],
            [3, 4],
            [5, 6]])
        test_result = np.array([3, 4])

        # Need to use Numpy testing functions to compare arrays
        npt.assert_array_equal(trial_instance.daily_mean(), test_result)


    @pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
            ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [4, 6, 9]),
            ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [4, -1, 9]),
        ])
    def test_daily_max(self, test, expected, trial_instance):
        """Test max function works for zeroes, positive integers, mix of positive/negative integers."""
        trial_instance.data = np.array(test)
        npt.assert_array_equal(trial_instance.daily_max(), np.array(expected))


