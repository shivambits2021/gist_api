import contextvars
import sys
from logging import DEBUG, Formatter, StreamHandler, getLogger
from fastapi import Request
from app.core.config import settings
from app.core.logging_service.singleton_utils import Singleton

request_context = contextvars.ContextVar("request_context")


class RequestIDFormatter(Formatter):
    def format(self, record):
        request = request_context.get("request_context")
        record.trace_id = ""
        if isinstance(request, Request):
            record.trace_id = getattr(request.state, "trace_id", "")
        return super().format(record)


class LOGSetup(metaclass=Singleton):
    def __init__(self):
        self._logger = getLogger(name=settings.PROJECT_NAME)
        self._logger.setLevel(DEBUG)

        log_formatter = RequestIDFormatter(
            "[%(asctime)s] [%(thread)d][%(levelname)s] "
            "[%(filename)s] [%(funcName)s:%(lineno)d] : %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S%z",
        )

        log_handler = StreamHandler(sys.stdout)
        log_handler.setFormatter(log_formatter)
        self._logger.addHandler(log_handler)

    def get_logger(self):
        return self._logger


logger = LOGSetup().get_logger()
