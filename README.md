# Cuber
## Для чего нужен
Пусть у вас есть процесс, который декомпозируется на несколько этапов. Может быть, вы хотите менять одни этапы на другие, наблюдая за измением результата. Тогда вы можете обернуть свой процесс в кубики (cube.Cube) и задвать расчет графом на этих кубиках. Пеперь, конфигурация всей системы будет задавать исключительно одним файлом, что позволит избежать проблем со слежкой за ыерсиями (это особенно важно, если в комнде несколько человек или вы делаете большие перерывы в разработке). Так же, система будет кешировать результаты, поэтому кубик не будет счиаться дважды на одних и тех же данных.

# Usage
* Create your cubes and other files (per project)
* Configure workflow via graph (create separate .wf file per configuration)
* Run configuration: `python -m cuber run your_graph.wf` from dirctory of project (it is important, becuase it imports your modules)

Also, you may use cubes separately. You need just call `MyCube(params_of_the_cube).get()`. It will load the cached result, if it exist, or make a calculations. The result is equal to result of fucntion `eval`.

# Config
You are able to specify config with `.cuber` file in current (`cd`) directory.

* Specifeing checkpoints folder makes you able to use checkpoints in common. It is usefull for server-based development of ML.
* Message delay: cuber will send message if graph is done or failed, but only if there is `message_delay` minutes form start. It is useful for not-spamming at testing.
* Hash function to use as base for `universal_hash`

Example:
```
[cuber]
checkpoints_dir = /olo/common/checkpoints_for_our_common_project
message_delay = 3
hash_type = sha224

[telegram]
token = ...
chat_id = ...
```

# Cube development
Suggestion: make .py file per each cube and name is `cube_<smth>.py` and name class `Cube<Smth>`. Then it would be easier to write configurations.
Cube is an abstract evaluation result. It may be iterpreted like a function.
All parameters have to be parameters of constructor (`__init__`). The result of cube have to be fully determined by the params.

Abstrct cube class:
```
class Cube(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def name(self):
        '''
            Unique name for cube and params. This name is key for cache.
        '''
        return

    def get(self):
        '''
            Checks if there is a cached verison and loads it.
            If there is no cached version, runs calcualtions via eval function.
            If you want to get cube's result, use only this function.
        '''
        ...

    @abc.abstractmethod
    def eval(self):
        '''
            This method should contain meaningful calculations. It have to return dict with result.
        '''
        return
```

# Workflow module
This module parses graphs from `.wf` file and runs cubes. See `__main__.py` file for example.

# Examples
Note: you are able to turn on logging of all packages (not only your cubes) with option `--logging` and set logging level to debug via `--debug`.
```
python -m cuber --logging --debug run with_train_test_split.wf
```

## Example 1
See code, it is simple.
Note, it does not evaluate function for the second time:
```
gborisenko@switch-toolset:~/projects/Cuber/examples/example_1$ python -m cuber trivial.wf
INFO: 2017-06-22 17:26:57,574 ::: cube_trivial: Init: param = 7 (cube_trivial.py:8)
INFO: 2017-06-22 17:26:57,574 ::: cuber.cube: Pickle name: checkpoints/trivial_7.pkl (cube.py:18)
INFO: 2017-06-22 17:26:57,575 ::: cuber.cube: Cache is not ok. Evaluating... (cube.py:20)
INFO: 2017-06-22 17:26:57,575 ::: cube_trivial: Evaluating (cube_trivial.py:18)
INFO: 2017-06-22 17:26:57,576 ::: cube_trivial: Done (cube_trivial.py:24)
INFO: 2017-06-22 17:26:57,576 ::: cuber.cube: Writing cache (cube.py:22)
INFO: 2017-06-22 17:26:57,576 ::: cuber.cube: Loading from cache (cube.py:29)
INFO: 2017-06-22 17:26:57,576 ::: cuber.cube: Loaded (cube.py:32)
n: 993
CRITICAL: 2017-06-22 17:26:57,576 ::: root      : trivial.wf:
n: 993
 (__main__.py:21)
gborisenko@switch-toolset:~/projects/Cuber/examples/example_1$ python -m cuber trivial.wf
INFO: 2017-06-22 17:27:04,502 ::: cube_trivial: Init: param = 7 (cube_trivial.py:8)
INFO: 2017-06-22 17:27:04,502 ::: cuber.cube: Pickle name: checkpoints/trivial_7.pkl (cube.py:18)
INFO: 2017-06-22 17:27:04,502 ::: cuber.cube: Cache is ok (cube.py:28)
INFO: 2017-06-22 17:27:04,502 ::: cuber.cube: Loading from cache (cube.py:29)
INFO: 2017-06-22 17:27:04,502 ::: cuber.cube: Loaded (cube.py:32)
n: 993
CRITICAL: 2017-06-22 17:27:04,502 ::: root      : trivial.wf:
n: 993
 (__main__.py:21)
```

## Example 2
This exmaple has a several cubes, that are near to production cubes. You may use this cube in your own project.
It generates dataset, split it into train and test parts, fits linear model and evaluates the metric.
Note, there is two `.wf` files: they are based on the same cubes, but works in sligthly different ways.
