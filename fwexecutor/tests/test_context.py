# coding: utf-8
import unittest

from fwexecutor.context import ExecutionContext


class TestContext(unittest.TestCase):

    def test_init_with_no_arg(self):
        ctx = ExecutionContext()
        self.assertEqual(1, ctx.cpu)
        self.assertEqual(2, ctx.ram)

    def test_init_with_args(self):
        ctx = ExecutionContext(cpu=4, ram=16)
        self.assertEqual(4, ctx.cpu)
        self.assertEqual(16, ctx.ram)

    def test_cpu_property(self):
        ctx = ExecutionContext()
        self.assertEqual(1, ctx.cpu)
        ctx.cpu = 5
        self.assertEqual(5, ctx.cpu)

    def test_with_cpu(self):
        ctx = ExecutionContext().with_kv('cpu', 5)
        self.assertEqual(5, ctx.cpu)

    def test_with_cpu_and_ram(self):
        ctx = ExecutionContext().with_kv('cpu', 5).with_kv('ram', 16)
        self.assertEqual(5, ctx.cpu)
        self.assertEqual(16, ctx.ram)

    def test_print(self):
        self.assertEqual('{cpu: 1, disk: 10, parallel: 1, ram: 2}', str(ExecutionContext()))
