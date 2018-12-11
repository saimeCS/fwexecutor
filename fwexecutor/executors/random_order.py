# coding: utf-8
import logging
from fwexecutor.executors.sequential import SequentialExecutor

logger = logging.getLogger('executor.randomorder')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


class RandomOrderExecutor(SequentialExecutor):

    def execute(self, func, items):
        logger.info('in random executor')
        import random
        shuffled_items = items[:]
        random.shuffle(shuffled_items)
        return super().execute(func, shuffled_items)

