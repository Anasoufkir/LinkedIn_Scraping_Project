from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_429_TOO_MANY_REQUESTS

class ScrapingRateLimitException(HTTPException):
    def __init__(self, detail: str = "Rate limit exceeded. Please wait before making more requests."):
        super().__init__(status_code=HTTP_429_TOO_MANY_REQUESTS, detail=detail)

class ResourceNotFoundException(HTTPException):
    def __init__(self, resource: str):
        detail = f"{resource} not found."
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)

class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Invalid request parameters."):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)
