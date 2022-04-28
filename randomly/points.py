import numpy as np
from scipy.stats import poisson, uniform
from typing import Tuple


def generate_poisson_points(
        bounds: Tuple[float, float, float, float], rate: float
) -> np.ndarray:
    """
    Get the haystack using bounds and rate... something rather mathy. I have no idea what the module does.

    Args:
        bounds (tuple): A tuple containing four bound elements
        rate (float): The rate

    Returns:
        np.hstack: A haystack... maybe...

    """
    dx = bounds[2] - bounds[0]
    dy = bounds[3] - bounds[1]

    # Get the poisson?
    N = poisson(rate * dx * dy).rvs()
    xs = uniform.rvs(0, dx, ((N, 1))) + bounds[0]
    ys = uniform.rvs(0, dy, ((N, 1))) + bounds[1]

    return np.hstack((xs, ys))
