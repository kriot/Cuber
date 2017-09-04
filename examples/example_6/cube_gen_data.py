from cuber import cube
import logging
import numpy as np

logger = logging.getLogger(__name__)

class CubeGenData(cube.Cube):
    def __init__(self, a, b, noise, n, seed):
        self.seed = seed
        self.a = a
        self.b = b
        self.noise = noise
        self.n = n

    def name(self):
        '''
        It have to be uniue for each case of params
        '''
        return 'data_{}_{}_{}_{}_{}'.format(self.a, self.b, self.n, self.noise, self.seed)

    def eval(self):
        logger.info('Evaluating')
        np.random.seed(self.seed)
        X = np.random.randn(self.n)
        y = self.a * X + self.b + np.random.randn(self.n) * self.noise
        logger.info('Done')
        return {
            'X': X,
            'y': y,
        }
