# coding: utf-8


class ExecutionContext(dict):

    def __init__(self, cpu=1, ram=2, disk=10, parallel=1):
        super(ExecutionContext, self).__init__({
            # Nb CPU per task
            'cpu': cpu,
            # RAM for each task (in Go)
            'ram': ram,
            # Disk size for each task  (in Go)
            'disk': disk,
            # Number of task in parallel
            'parallel': parallel,
        })

    @property
    def cpu(self):
        return self.get('cpu')

    @cpu.setter
    def cpu(self, value):
        self['cpu'] = value

    @property
    def ram(self):
        return self.get('ram')

    @ram.setter
    def ram(self, value):
        self['ram'] = value

    @property
    def disk(self):
        return self.get('disk')

    @disk.setter
    def disk(self, value):
        self['disk'] = value

    @property
    def parallel(self):
        return self.get('parallel')

    @parallel.setter
    def parallel(self, value):
        self['parallel'] = value

    def with_kv(self, key, value):
        self[key] = value
        return self

    def __str__(self):
        return '{{{}}}'.format(', '.join(['{}: {}'.format(key, self.get(key))
                                          for key in sorted(self.keys())]))
        





