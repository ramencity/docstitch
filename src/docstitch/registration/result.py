from dataclasses import dataclass

from docstitch.registration.transform import Transform


@dataclass(slots=True)
class RegistrationResult:
    transform: Transform