import logging
import json
import numpy as np
import hashlib
import numbers
logger = logging.getLogger(__name__)

def sha224(s):
    return hashlib.sha224(s).hexdigest()

def object_hash(obj, fields = None):
    if fields is not None:
        d = {key: value for key, value in obj.__dict__.iteritems() if key in fields}
    else:
        d = obj.__dict__
    return universal_hash(d)

def universal_hash(obj):
    try:
        return sha224(obj)
    except:
        if isinstance(obj, unicode):
            return sha224(obj.encode('utf-8'))
        if isinstance(obj, numbers.Number):
            return sha224(repr(obj))
        if isinstance(obj, dict):
            return reduce(lambda x,y : universal_hash(x + y),
                    sorted([universal_hash((universal_hash(key), universal_hash(value))) for key, value in obj.iteritems()])
                )
        if isinstance(obj, tuple):
            return json_hash(list(universal_hash(item) for item in obj))
        if isinstance(obj, list):
            return universal_hash(tuple(obj))
        if isinstance(obj, np.ndarray):
            return sha224(obj.tostring())
        if obj is None:
            return sha224('none' + 'salt123')
        logger.error('Unsupported type: {}'.format(type(obj))) 
        raise NotImplementedError('Unspported type for hashing: {}. Object: {}'.format(type(obj), obj))

def json_hash(obj):
    raise NotImplementedError('Do not use json hashing, beacuse it is not pure. The order of dict`s keys is not totally specified.')
    return sha224(json.dumps(obj))
