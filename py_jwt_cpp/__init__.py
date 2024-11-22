from typing import Dict
from .jwt_cpp import cpp_encode

class InvalidClaimError(Exception):
    pass

def encode(
    data: Dict[str, str],
    private_key: str,
    headers: Dict[str, str] = {}
):
    _validate_string_keys(data, 'payload')
    _validate_string_keys(headers, 'headers')

    return cpp_encode(data, private_key, headers)


def _validate_string_keys(data: dict, name):
    invalid_keys = [k for k, v in data.items() if not isinstance(v, str)]
    if invalid_keys:
        raise InvalidClaimError(
            f"all values in {name} should be string. Invalid keys: {invalid_keys}"
        )
