from cuber import cube
import copy
import inspect

def to_cube(**cube_static_params):
    for key in cube_static_params.keys():
        assert key in {'immutable_args', 'restorable', 'version'}
    def to_cube_spec(fn):
        possible_args = inspect.getargspec(fn)[0]
        class CubeTmp(cube.Cube):
            def __init__(self, **kwargs):
                kwargs = copy.deepcopy(kwargs)
                for key in kwargs:
                    if key not in possible_args:
                        raise ValueError('Argument "{}" is passed, but cube can accept only these arguments: {}'.format(key, kwargs))

                for possible_arg in possible_args:
                    if possible_arg not in kwargs and possible_arg != 'cuber_name':
                        kwargs[possible_arg] = None

                self.__dict__ = kwargs

            def eval(self):
                if 'cuber_name' in possible_args:
                    return fn(cuber_name = self.name(), **self.__dict__)
                else:
                    return fn(**self.__dict__)
        CubeTmp.__name__ = fn.__name__
        for key, value in cube_static_params.iteritems():
            setattr(CubeTmp, key, value)
        return CubeTmp
    return to_cube_spec
