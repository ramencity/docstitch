from pathlib import Path

import cv2

from docstitch.common import Image

PathLike = str | Path

def load_image(path: PathLike) -> Image:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(path)

    image = cv2.imread(str(path), cv2.IMREAD_COLOR)

    if image is None:
        raise RuntimeError(f"Could not read image: {path}")

    return image


def save_image(path: PathLike, image: Image) -> None:
    """Save an image to disk."""

    success = cv2.imwrite(str(path), image)

    if not success:
        raise IOError(f"Could not write image to {path}")


def to_grayscale(image: Image) -> Image:
    """Convert a BGR image to grayscale."""

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
