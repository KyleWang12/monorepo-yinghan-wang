class Logger:
    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead of direct instantiation")
    
    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.messages = []
            print("Logger created exactly once")
        else:
            print("logger already created")
        return cls._instance

    def add_message(self, message):
        self.messages.append(message)


def main():
    for i in range(3):
        logger = Logger.instance()
        logger.add_message(f"Adding message number: {i}")


if __name__ == "__main__":
    main()
