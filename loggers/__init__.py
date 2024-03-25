from src.loggers.main import main_logger

from src.loggers.app import app_logger
from src.loggers.flow import flow_logger, update_flow, log_time


def setup_loggers():
    main_logger.add_handler_to_queue(app_logger.StdoutHandler())
    main_logger.add_handler_to_queue(app_logger.JsonHandler())
    main_logger.add_handler_to_queue(
        app_logger.DebugHandler(),
        [app_logger, flow_logger],
    )
    main_logger.add_handler_to_queue(
        app_logger.InfoHandler(),
        [app_logger, flow_logger],
    )
    main_logger.add_handler_to_queue(
        flow_logger.FlowFileHandler(),
        [flow_logger],
    )
    main_logger.add_handler_to_queue(
        flow_logger.FlowStdoutHandler(),
        [flow_logger],
    )



__all__ = [
    "setup_loggers",
    "app_logger",
    "flow_logger",
    "update_flow",
    "log_time",
]
