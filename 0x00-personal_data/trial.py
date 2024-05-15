import logging

# class CustomLogRecord(logging.LogRecord):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.custom_attribute = 'CUSTOM'

# def record_factory(*args, **kwargs):
#     return CustomLogRecord(*args, **kwargs)

# logging.setLogRecordFactory(record_factory)
# logger = logging.getLogger('my_logger')
# logger.error('This is a test.')

# # Setup a simple console output
# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(levelname)s - %(custom_attribute)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.error('This is a test.')


# Create a formatter with a specific format string
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Manually create a LogRecord
log_record = logging.LogRecord(
    name='example_logger', 
    level=logging.INFO, 
    pathname=__file__,
    lineno=10, 
    msg='This is a test log message.',
    args=(),
    exc_info=None,
    func=None,
    sinfo=None
)
log_record.message = "Message changed"
# Format the LogRecord using the formatter
formatted_message = formatter.format(log_record)

print(formatted_message)
print()
