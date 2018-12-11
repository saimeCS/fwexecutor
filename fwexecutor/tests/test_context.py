# coding: utf-8
import unittest

from fwexecutor.Context import ExecutionContext


class TestContext(unittest.TestCase):

    def test_init_with_no_arg(self):
        ctx = ExecutionContext()
        self.assertEqual(1, ctx._cpu)
        self.assertEqual(2, ctx._ram)
        self.assertIsNone(ctx._framework)

    def test_init_with_no_args(self):
        ctx = ExecutionContext(cpu=4, ram=16)
        self.assertEqual(4, ctx._cpu)
        self.assertEqual(16, ctx._ram)
        self.assertIsNone(ctx._framework)

    def test_cpu_property(self):
        ctx = ExecutionContext()
        self.assertEqual(1, ctx.cpu)
        ctx.cpu = 5
        self.assertEqual(5, ctx.cpu)

    def test_with_cpu(self):
        ctx = ExecutionContext().with_cpu(5)
        self.assertEqual(5, ctx.cpu)

    def test_with_cpu_and_ram(self):
        ctx = ExecutionContext().with_cpu(5).with_ram(16)
        self.assertEqual(5, ctx.cpu)
        self.assertEqual(16, ctx.ram)

    def test_print(self):
        self.assertEqual('{_cpu: 1, _disk: 10, _framework: None, _parallel: 1, _ram: 2}', str(ExecutionContext()))
