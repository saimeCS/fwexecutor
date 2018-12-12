# coding: utf-8
import unittest

from fwexecutor.factory import get_executors, get_executor


class TestExecutorFactory(unittest.TestCase):

    def test_get_executors(self):
        executors = get_executors()
        print(executors)
        self.assertGreaterEqual(len(executors), 3)

    def test_get_executor_no_args(self):
        executor = get_executor()
        self.assertEqual(executor.kind, 'sequential')
        self.assertEqual(executor.__class__.__name__, 'SequentialExecutor')

    def test_get_executor_kind_sequential(self):
        executor = get_executor(kind='sequential')
        self.assertEqual(executor.kind, 'sequential')
        self.assertEqual(executor.__class__.__name__, 'SequentialExecutor')

    def test_get_executor_kind_parallel(self):
        executor = get_executor(kind='parallel')
        self.assertEqual(executor.kind, 'parallel')
        self.assertEqual(executor.__class__.__name__, 'ParallelExecutor')