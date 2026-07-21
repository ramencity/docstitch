from dataclasses import dataclass

import numpy as np

from .transform import Transform


@dataclass(slots=True)
class RegistrationResult:
    image: np.ndarray
    transform: Transform