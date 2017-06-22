from cuber import cube
import logging

logger = logging.getLogger(__name__)

class CubeTrivial(cube.Cube):
    def __init__(self, param = 1):
        logger.info('Init: param = {}'.format(param))
        self.param = param

    def name(self):
        '''
        It have to be uniue for each case of params
        '''
        return 'trivial_{}'.format(self.param)

    def eval(self):
        logger.info('Evaluating')
        # Here have to be a heavy calculation
        n = 0
        for i in range(9999):
            n += self.param
            n %= 1000
        logger.info('Done')
        return {
            'n': n,
        }
