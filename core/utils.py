import logging

logger = logging.getLogger("info_logger")

def info_logger(request_id, log):
    logger.info(f"[Request ID: {request_id}] {log}")
