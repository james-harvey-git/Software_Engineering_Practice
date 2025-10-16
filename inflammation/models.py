"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2d inflammation data array."""
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2d inflammation data array."""
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2d inflammation data array."""
    return np.min(data, axis=0)

import numpy as np
import pytest
def patient_normalise(data):
    """
    Normalise patient data from a 2D inflammation data array.

    NaN values are ignored, and normalised to 0.

    Negative values are rounded to 0.
    """
    ...
    if np.any(data < 0):
        raise ValueError('Inflammation values should not be negative')
    max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised
...

import numpy as np

class Patient:
    def __init__(self, id, data):
        self.id = id
        self.data = data

    def data_mean(self):
        """Calculate the mean of patient's inflammation data."""
        return np.mean(self.data)

    def data_max(self):
        """Calculate the max of patient's inflammation data."""
        return np.max(self.data)

    def data_min(self):
        """Calculate the min of patient's inflammation data."""
        return np.min(self.data)


class Trial:
    def __init__(self, data, id):
        self.data = data
        self.id = id
    
    @classmethod
    def from_csv(cls, filename, id):
        """
        Class method to create a Trial instance from data in a CSV file.

        Parameters:
        filename (str): The file path of the CSV file to read.
        id (str): The id to assign to the Trial instance.

        Returns:
        Trial: A Trial instance with the data and id from the CSV file.
        """
        data = cls.load_csv(filename)
        return cls(data, id)

    @staticmethod
    def load_csv(filename):
        """Load a Numpy array from a CSV

        :param filename: Filename of CSV to load
        """
        return np.loadtxt(fname=filename, delimiter=',')

    def daily_mean(self):
        """Calculate the daily mean of a 2d inflammation data array."""
        return np.mean(self.data, axis=0)

    def daily_max(self):
        """Calculate the daily max of a 2d inflammation data array."""
        return np.max(self.data, axis=0)

    def daily_min(self):
        """Calculate the daily min of a 2d inflammation data array."""
        return np.min(self.data, axis=0)

    def patient_normalise(self):
        """
        Normalise patient data from a 2D inflammation data array.

        NaN values are ignored, and normalised to 0.

        Negative values are rounded to 0.
        """
        if np.any(self.data < 0):
            raise ValueError('Inflammation values should not be negative')
        if not isinstance(self.data, np.ndarray):
            raise TypeError('data input should be ndarray')
        if len(self.data.shape) != 2:
            raise ValueError('inflammation array should be 2-dimensional')
        max_data = np.nanmax(self.data, axis=1)
        with np.errstate(invalid='ignore', divide='ignore'):
            normalised = self.data / max_data[:, np.newaxis]
        normalised[np.isnan(normalised)] = 0
        normalised[normalised < 0] = 0
        return normalised
    
    def get_patient(self, row):
        """Return a Patient object for the given patient ID."""
        if row < 0 or row >= self.data.shape[0]:
            raise IndexError("Patient ID out of range")
        return Patient(row, self.data[row])
    
