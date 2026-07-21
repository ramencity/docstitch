from docstitch.common import Image
from docstitch.registration.result import RegistrationResult


class Registrar:
    """Register two overlapping document scans."""

    def register(
        self,
        top: Image,
        bottom: Image,
    ) -> RegistrationResult:
        raise NotImplementedError