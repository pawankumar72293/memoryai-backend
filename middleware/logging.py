import time

from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from core.logger import logger


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start = time.time()

        response = await call_next(
            request
        )

        duration = (
            time.time() - start
        )

        logger.info(
            f"""
{request.method}
{request.url.path}
{duration:.2f}s
"""
        )

        return response