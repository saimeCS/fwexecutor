# coding: utf-8
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='executor framework',
    packages=find_packages(),
    version=read('VERSION'),
    entry_points={
        'executors': [
            'sequential = fwexecutor.executors.sequential:SequentialExecutor',
            'parallel = fwexecutor.executors.multiprocessing:ParallelExecutor',
            'randomorder = fwexecutor.executors.random_order:RandomOrderExecutor',
        ],
    },
    test_suite='nose.collector',
    tests_require=['nose'],
)
