import logging
import json
import numpy as np
logger = logging.getLogger(__name__)

def universal_hash(obj):
    try:
        return hash(obj)
    except:
        if isinstance(obj, dict):
            return reduce(lambda x,y : x^y,
                    [hash((universal_hash(key), universal_hash(value))) for key, value in obj.iteritems()]
                )
        if isinstance(obj, tuple):
            return hash((universal_hash(item) for item in obj))
        if isinstance(obj, list):
            return universal_hash(tuple(obj))
        if isinstance(obj, np.ndarray):
            return hash(obj.tostring())
        raise NotImplementedError()

def json_hash(obj):
    return hash(json.dumps(obj))
