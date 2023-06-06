from collections.abc import Iterator
from typing import Any, Literal

from django.utils.functional import _StrOrPromise

class FieldDoesNotExist(Exception): ...
class AppRegistryNotReady(Exception): ...

class ObjectDoesNotExist(Exception):
    silent_variable_failure: bool

class MultipleObjectsReturned(Exception): ...
class SuspiciousOperation(Exception): ...
class SuspiciousMultipartForm(SuspiciousOperation): ...
class SuspiciousFileOperation(SuspiciousOperation): ...
class DisallowedHost(SuspiciousOperation): ...
class DisallowedRedirect(SuspiciousOperation): ...
class TooManyFieldsSent(SuspiciousOperation): ...
class RequestDataTooBig(SuspiciousOperation): ...
class RequestAborted(Exception): ...
class BadRequest(Exception): ...
class PermissionDenied(Exception): ...
class ViewDoesNotExist(Exception): ...
class MiddlewareNotUsed(Exception): ...
class ImproperlyConfigured(Exception): ...
class FieldError(Exception): ...

NON_FIELD_ERRORS: Literal["__all__"]

class ValidationError(Exception):
    error_dict: dict[str, list[ValidationError]]
    error_list: list[ValidationError]
    message: _StrOrPromise
    code: str | None
    params: dict[str, Any] | None
    def __init__(
        self,
        # Accepts arbitrarily nested data structure, mypy doesn't allow describing it accurately.
        message: _StrOrPromise | ValidationError | dict[str, Any] | list[Any],
        code: str | None = ...,
        params: dict[str, Any] | None = ...,
    ) -> None: ...
    @property
    def message_dict(self) -> dict[str, list[str]]: ...
    @property
    def messages(self) -> list[str]: ...
    def update_error_dict(self, error_dict: dict[str, list[ValidationError]]) -> dict[str, list[ValidationError]]: ...
    def __iter__(self) -> Iterator[tuple[str, list[str]] | str]: ...

class EmptyResultSet(Exception): ...
class SynchronousOnlyOperation(Exception): ...
