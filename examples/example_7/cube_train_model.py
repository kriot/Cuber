from cuber import cube
import logging
from cuber import utils
import importlib

logger = logging.getLogger(__name__)

class CubeTrainModel(cube.Cube):
    def __init__(self, model_module, model_class, **kwargs):
        logger.info('Init')
        self.kwargs = kwargs
        self.model_module = model_module
        self.model_class = model_class

    def name(self):
        return 'model_{}_{}_{}'.format(self.model_module, self.model_class, utils.universal_hash(self.kwargs))

    def eval(self):
        logger.info('Evaluating')
        module = importlib.import_module(self.model_module)
        model = getattr(module, self.model_class)()
        return {
            'models': [model_.serialise() for model_ in model.fit(**self.kwargs)] # sequence of learned models
        }

