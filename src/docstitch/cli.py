import argparse
from pathlib import Path

from docstitch.io.image import load_image
from docstitch.registration.engine import Registrar


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="docstitch",
        description="Stitch two overlapping flatbed scans.",
    )

    parser.add_argument("top", type=Path)
    parser.add_argument("bottom", type=Path)
    parser.add_argument("output", type=Path)

    parser.add_argument(
        "--diagnostics",
        action="store_true",
        help="Write diagnostics images.",
    )

    args = parser.parse_args()

    top = load_image(args.top)
    bottom = load_image(args.bottom)

    registrar = Registrar()

    result = registrar.register(top, bottom)

    print(result)

    return 0