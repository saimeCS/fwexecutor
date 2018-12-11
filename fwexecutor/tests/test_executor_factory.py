# coding: utf-8
import unittest

from fwexecutor.Context import ExecutionContext
from fwexecutor.ExecutorFactory import get_executors


class TestExecutorFactory(unittest.TestCase):

    def test_get_executors(self):
        executors = get_executors()
        print(executors)
        self.assertLessEqual(2, len(executors))
