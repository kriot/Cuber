from cuber import cube
import logging
import importlib
import math
from cuber import utils

logger = logging.getLogger(__name__)

class CubeRMSE(cube.Cube):
    def __init__(self, prediction, real):
        logger.info('Init')
        self.real = real
        self.prediction = prediction

    def name(self):
        return 'rmse_{}'.format(hash(
            (
                utils.universal_hash(self.prediction),
                utils.universal_hash(self.real),
            )
        ))

    def eval(self):
        rmse = ((self.real - self.prediction) ** 2).mean()**0.5
        return {
            'rmse': rmse,
        }
