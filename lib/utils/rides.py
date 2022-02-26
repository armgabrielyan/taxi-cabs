import numpy as np

def get_rides_indices(occupancy):
    is_one = np.concatenate(([0], np.equal(occupancy, 1).view(np.int8), [0]))
    absdiff = np.abs(np.diff(is_one))
    ranges = np.where(absdiff == 1)[0].reshape(-1, 2)

    return ranges