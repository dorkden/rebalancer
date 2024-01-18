import logging.handlers


class Logger:
    Logger = None
    NotificationHandler = None

    def __init__(self, logging_service="rebalance", enable_notifications=True):
        # Logger setup
        self.Logger = logging.getLogger(f"{logging_service}_logger")
        self.Logger.setLevel(logging.DEBUG)
        self.Logger.propagate = False
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        # default is "logs/rebalance.log"
        fh = logging.FileHandler(f"logs/{logging_service}.log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        self.Logger.addHandler(fh)

        # logging to console
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(formatter)
        self.Logger.addHandler(ch)


    def log(self, message, level="info", notification=True):
        if level == "info":
            self.Logger.info(message)
        elif level == "warning":
            self.Logger.warning(message)
        elif level == "error":
            self.Logger.error(message)
        elif level == "debug":
            self.Logger.debug(message)

    def info(self, message, notification=True):
        self.log(message, "info", notification)

    def warning(self, message, notification=True):
        self.log(message, "warning", notification)

    def error(self, message, notification=True):
        self.log(message, "error", notification)

    def debug(self, message, notification=False):
        self.log(message, "debug", notification)
