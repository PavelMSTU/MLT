# -*- coding: utf-8 -*-
"""
MLT

mlttree

Created by pavel on 02.03.18 14:10
"""
import datetime
from copy import deepcopy

from core.default_header import DEFAULT_HEADER

__author__ = 'pavel'


def header(mt, line):

    def environment(len_):
        if len_ == 1:
            return 'section'
        if len_ == 2:
            return 'subsection'
        raise NotImplementedError("Only ## and # can be use!")

    if line and line[0] == '#':
        values = line.split(' ')
        assert len(values) >= 2
        h, value = values[0], ' '.join(values[1:])
        value = value.lstrip()

        text = mt.pop()
        mt.add_text(text)

        mt.add_text("\section{"+value+"}")
        mt.push(None)

        return True
    else:
        return False


FUNC_CHECKS = [
    header
]


class MltTree:

    def __init__(self, default_header=DEFAULT_HEADER):
        self.stack = list()
        self.lines = list()
        self.header = deepcopy(DEFAULT_HEADER)

    def push(self, value):
        if value is None:
            return
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            return None
        v = self.stack.pop(-1)
        return v

    def add_text(self, value):
        if value is None:
            return

        self.lines.append(value)

    def add_line(self, line):
        for func_ in FUNC_CHECKS:
            if func_(self, line):
                return
        self.add_text(line)

    def enumerate_header_lines(self):
        for key, value, regexp in self.header:
            yield value

    def enumerate_lines(self, end=""):
        for line in self.enumerate_header_lines():
            yield line+end
        yield '\\begin{document}'
        for line in self.lines:
            yield line+end
        yield '\\end{document}'

    def save2file(self, path_out):
        with open(path_out, 'w') as fw:
            for line in self.enumerate_lines():
                fw.write(line)
                fw.write('\n')


if __name__ == u"__main__":
    print(u'Run mlttree {0}'.format(datetime.datetime.now()))
    