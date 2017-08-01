import logging

from cuber import cube
from cuber import utils

logger = logging.getLogger(__name__)

class CubeFunction(cube.Cube):
    def __init__(self, arg, reg):
        self.arg = arg
        self.reg = reg

    def name(self):
        return 'f_{}_{}'.format(self.arg, self.reg)

    def eval(self):
        x = self.arg
        y = self.reg
        return {
            'f': (x - 2) ** 2 + (y - 5) ** 2
        }
