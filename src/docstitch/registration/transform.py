from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Transform:
    matrix: np.ndarray