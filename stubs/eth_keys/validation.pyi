from typing import Any

def validate_integer(value: int) -> None: ...
def validate_bytes(value: bytes) -> None: ...
def validate_gte(value: int, minimum: int) -> None: ...
def validate_lte(value: int, maximum: int) -> None: ...

validate_lt_secpk1n: Any

def validate_message_hash(value: bytes) -> None: ...
def validate_public_key_bytes(value: bytes) -> None: ...
def validate_private_key_bytes(value: bytes) -> None: ...
def validate_signature_bytes(value: bytes) -> None: ...
