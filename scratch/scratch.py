import numpy as np
from numpy.typing import NDArray


def get_linear_design_matrix(x: NDArray) -> NDArray:
    assert isinstance(x, np.ndarray)
    assert x.ndim == 1, "x must be a 1D array"
    x = x[:, np.newaxis]
    ones = np.ones_like(x)
    return np.hstack([ones, x])


x = np.array([1, 2, 3, 4, 5])
print(get_linear_design_matrix(x))
