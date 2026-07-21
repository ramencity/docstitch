from docstitch.common import Image
from pathlib import Path

import cv2
import numpy as np


def load_image(path: Path) -> Image:
    """Load an image from disk."""

    image = cv2.imread(str(path), cv2.IMREAD_COLOR)

    if image is None:
        raise FileNotFoundError(path)

    return image


def save_image(path: Path, image: np.ndarray) -> None:
    """Save an image to disk."""

    success = cv2.imwrite(str(path), image)

    if not success:
        raise IOError(f"Could not write image to {path}")


def to_grayscale(image: np.ndarray) -> np.ndarray:
    """Convert a BGR image to grayscale."""

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
