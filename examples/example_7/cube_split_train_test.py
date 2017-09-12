from cuber import cube
from cuber import utils
import logging
import numpy as np

logger = logging.getLogger(__name__)

class CubeSplitTrainTest(cube.Cube):
    def __init__(self, X, y, test_ratio, seed):
        self.seed = seed
        self.X = X
        self.y = y
        self.test_ratio = test_ratio

    def name(self):
        return 'data_{}_{}_{}'.format(self.test_ratio, self.seed, utils.universal_hash((self.X, self.y)))

    def eval(self):
        logger.info('Evaluating')
        np.random.seed(self.seed)
        test_mask = np.random.binomial(n = 1, size = self.y.shape[0], p = self.test_ratio).astype(bool)
        X_test = self.X[test_mask]
        y_test = self.y[test_mask]
        X_train = self.X[~test_mask]
        y_train = self.y[~test_mask]
        logger.info('Done')
        return {
            'X_test': X_test,
            'y_test': y_test,
            'X_train': X_train,
            'y_train': y_train,
        }
