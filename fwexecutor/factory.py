# coding: utf-8
import logging
import pkg_resources

from fwexecutor.context import ExecutionContext

logger = logging.getLogger('executorFactory')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

EXECUTOR_DEFAULT = 'sequential'


def get_executor(kind=None, context=None):
    if kind is None or len(kind) == 0:
        logger.warning("No kind of executor specified. Use default executor '{}'".
                       format(EXECUTOR_DEFAULT))
        kind = EXECUTOR_DEFAULT
    if context is None:
        logger.warning("No context provided. Use default context")
        context = ExecutionContext()
    try:
        executors = get_executors()
        return executors[kind](context)
    except KeyError:
        logger.error("Unable to find executor '{}'. Possible values are '{}'. Using default executor '{}'".
                     format(kind, sorted(executors.keys()), EXECUTOR_DEFAULT))
        return get_executor(EXECUTOR_DEFAULT)


def get_executors():
    executors = {entry_point.name: entry_point.load() for entry_point in
                 pkg_resources.iter_entry_points('executors')}
    return executors
