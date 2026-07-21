from pathlib import Path

import cv2
import numpy as np


def load(path: Path) -> np.ndarray:
    """Load an image from disk."""

    image = cv2.imread(str(path), cv2.IMREAD_COLOR)

    if image is None:
        raise FileNotFoundError(path)

    return image


def save(path: Path, image: np.ndarray) -> None:
    """Save an image."""

    cv2.imwrite(str(path), image)


def gray(image: np.ndarray) -> np.ndarray:
    """Convert BGR image to grayscale."""

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)