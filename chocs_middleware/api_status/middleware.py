from chocs import HttpRequest, HttpResponse
from chocs.middleware import Middleware, MiddlewareHandler

__all__ = ["ApiStatusMiddleware"]


class ApiStatusMiddleware(Middleware):
    def handle(self, request: HttpRequest, next: MiddlewareHandler) -> HttpResponse:
        pass
