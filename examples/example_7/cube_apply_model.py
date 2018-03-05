from cuber import cube
import logging
from cuber import utils
import importlib

logger = logging.getLogger(__name__)

class CubeApplyModel(cube.Cube):
    def __init__(self, model_module, model_class, model_params, X):
        logger.info('Init')
        self.model_module = model_module
        self.model_class = model_class
        self.model_params = model_params
        self.X = X

    def name(self):
        return 'applied_model_{}_{}_{}'.format(
            self.model_module, self.model_class, 
            utils.universal_hash((
                self.X,
                self.model_class,
                self.model_module,
                self.model_params,
            )))

    def eval(self):
        logger.info('Evaluating')
        module = importlib.import_module(self.model_module)
        model = getattr(module, self.model_class)(**self.model_params)
        res = model.predict(self.X)
        return {
            'prediction': res
        }

