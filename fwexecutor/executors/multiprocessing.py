# coding: utf-8
import logging

import multiprocessing
import sys
import os
from fwexecutor.context import ExecutionContext
from fwexecutor.executors.base import BaseExecutor

logger = logging.getLogger('executor.parallel')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))


class ParallelExecutor(BaseExecutor):

    def __init__(self, context=None):
        self._context = context or ExecutionContext()
        try:
            nb_cpu = len(os.sched_getaffinity(0))
        except AttributeError:
            nb_cpu = os.cpu_count()
        self._usable_cpu = min(self._context.cpu, nb_cpu)

    def execute(self, func, items):
        try:
            logger.info('in parallel executor')

            pool = multiprocessing.Pool(processes=self._usable_cpu)
            rv = pool.map(func, items)
            pool.terminate()
            return rv
        finally:
            logger.info('parallel executor done')
