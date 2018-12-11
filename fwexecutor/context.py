# coding: utf-8


class ExecutionContext:

    def __init__(self, cpu=1, ram=2, disk=10, parallel=1, framework=None):
        # Nb CPU per task
        self._cpu = cpu
        # RAM for each task (in Go)
        self._ram = ram
        # Disk size for each task  (in Go)
        self._disk = disk
        # Number of task in parallel
        self._parallel = parallel
        self._framework = framework

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, value):
        self._cpu = value

    def with_cpu(self, value):
        self._cpu = value
        return self

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value):
        self._ram = value

    def with_ram(self, value):
        self._ram = value
        return self

    @property
    def disk(self):
        return self._disk

    @disk.setter
    def disk(self, value):
        self._disk = value

    def with_disk(self, value):
        self._disk = value
        return self

    @property
    def parallel(self):
        return self._parallel

    @parallel.setter
    def parallel(self, value):
        self._parallel = value

    def with_parallel(self, value):
        self._parallel = value
        return self

    def __str__(self):
        return '{{{}}}'.format(', '.join(['{}: {}'.format(key, self.__dict__[key])
                                          for key in sorted(self.__dict__.keys())]))
        





