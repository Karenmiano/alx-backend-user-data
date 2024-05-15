import logging

# Create a root logger
root_logger = logging.getLogger('parent')
root_logger.setLevel(logging.DEBUG)

# Create a file handler for the root logger
root_file_handler = logging.FileHandler('parent.log')
root_file_handler.setLevel(logging.DEBUG)
root_logger.addHandler(root_file_handler)

# Create a child logger
child_logger = logging.getLogger('child')
child_logger.setLevel(logging.DEBUG)

# Create a file handler for the child logger
child_file_handler = logging.FileHandler('child.log')
child_file_handler.setLevel(logging.DEBUG)
child_logger.addHandler(child_file_handler)

# Log messages
root_logger.debug('This is a message from the parent logger')
child_logger.debug('This is a message from the child logger')
