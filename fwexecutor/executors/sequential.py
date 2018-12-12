# coding: utf-8
import logging
import sys
from fwexecutor.executors.base import BaseExecutor

logger = logging.getLogger('executor.sequential')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.propagate = False


class SequentialExecutor(BaseExecutor):

    kind = 'sequential'
    
    def execute(self, func, items):
        try:
            logger.info('in sequential executor')
            rv = []
            for item in items:
                logger.info('Executing {} on {}'.format(func.__name__, item))
                rv.append(func(item))
            return rv
        finally:
            logger.info('sequential executor done')
