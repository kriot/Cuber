import logging.config
logging.config.dictConfig({
    'version': 1,
    'handlers': {
        'telegram': {
            'class': 'telegram_handler.TelegramHandler',
            'token': '384096575:AAEYB6b_7aRqETcYboh74_oqO2j2M32Q5EQ',
            'chat_id': 122007383,
            'level': 'CRITICAL',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
    },
    "loggers": {
        "": {
            "level": "DEBUG",
            "handlers": ["telegram", 'console'],
            "propagate": "no"
        }
    },
    'formatters': {
        'console': {
            'format': '%(levelname)s: %(asctime)s ::: %(name)-10s: %(message)s (%(filename)s:%(lineno)d)',
        }
    }
})
