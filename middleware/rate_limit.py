import time

from fastapi.responses import JSONResponse

RATE_LIMIT = {}

MAX_REQUESTS = 20

WINDOW = 60


class RateLimitMiddleware:

    def __init__(
        self,
        app
    ):

        self.app = app


    async def __call__(
        self,
        scope,
        receive,
        send
    ):

        if scope["type"] != "http":

            await self.app(
                scope,
                receive,
                send
            )

            return

        client = scope["client"][0]

        now = time.time()

        requests = RATE_LIMIT.get(
            client,
            []
        )

        requests = [

            r for r in requests

            if now - r < WINDOW
        ]

        if len(requests) >= MAX_REQUESTS:

            response = JSONResponse(
                status_code=429,

                content={
                    "message":
                    "Too many requests"
                }
            )

            await response(
                scope,
                receive,
                send
            )

            return

        requests.append(now)

        RATE_LIMIT[client] = requests

        await self.app(
            scope,
            receive,
            send
        )