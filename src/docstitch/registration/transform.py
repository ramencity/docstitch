from dataclasses import dataclass

import numpy as np


@dataclass(slots=True)
class Transform:
    """Estimated alignment between two scans."""

    matrix: np.ndarray

    tx: float
    ty: float

    rotation_deg: float

    matches: int
    inliers: int

    rms_error: float

    confidence: float