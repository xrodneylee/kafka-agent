import logging, logging.config

# logging
LOGGING_CONFIG = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simpleFormatter',
            'filename': 'kafka-agent.log',
            'maxBytes': 1024000,
            'backupCount': 1
        }
    },
    'formatters': {
        'simpleFormatter': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },
    'loggers': {
        'kafka-agent': {
            'level': 'INFO',
            'handlers': ['file']
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)
LOG = logging.getLogger('kafka-agent')
