import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(
        prog="docstitch",
        description="Stitch two overlapping flatbed scans."
    )

    parser.add_argument("top", type=Path)
    parser.add_argument("bottom", type=Path)
    parser.add_argument("output", type=Path)

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Write debug images."
    )

    args = parser.parse_args()

    print("docstitch")
    print(f"Top    : {args.top}")
    print(f"Bottom : {args.bottom}")
    print(f"Output : {args.output}")
    print(f"Debug  : {args.debug}")