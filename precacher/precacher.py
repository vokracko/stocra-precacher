import asyncio
from asyncio import Semaphore
from logging import getLogger

import sentry_sdk
from stocra.asynchronous.client import Stocra
from stocra.asynchronous.error_handlers import (
    retry_on_bad_gateway,
    retry_on_connection_error,
    retry_on_service_unavailable,
    retry_on_timeout_error,
)

from precacher.config import CONFIG

logger = getLogger("precacher")

if CONFIG.sentry_dsn:
    sentry_sdk.init(  # pylint: disable=abstract-class-instantiated
        dsn=CONFIG.sentry_dsn,
        environment=CONFIG.environment,
        traces_sample_rate=0.001,
    )


async def stream_all_blocks_and_transactions() -> None:
    subdomain = CONFIG.environment
    stocra_client = Stocra(
        api_key=CONFIG.unlimited_token,
        semaphore=Semaphore(200),
        error_handlers=[
            retry_on_service_unavailable,
            retry_on_connection_error,
            retry_on_bad_gateway,
            retry_on_timeout_error,
        ],
    )

    while True:
        try:
            async for block, transaction in stocra_client.stream_new_transactions(
                blockchain=subdomain, sleep_interval_seconds=1
            ):
                logger.info("%s: %s", block.height, transaction.hash)
        except Exception:  # pylint: disable=broad-except
            logger.exception("Refresh latest block")
