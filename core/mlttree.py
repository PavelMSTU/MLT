# -*- coding: utf-8 -*-
"""
MLT

mlttree

Created by pavel on 02.03.18 14:10
"""
import json
import datetime
from copy import deepcopy

from core.defaults import DEFAULT_HEADER
from core.defaults import DEFAULT_INIT_COMMENT

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

    def __init__(self, json_header_path):
        self.stack = list()
        self.lines = list()

        with open(json_header_path, 'r') as fr:
            self.j_header = json.load(fr)

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

    def make_title(self):
        return """
        \\title{\\vspace{-15mm}\\fontsize{24pt}{10pt}\\selectfont\\textbf{
        """+self.j_header['title']+"""
    }} % Article title
    
    \\author{
        \\large
        \\textsc{ """+self.j_header["author"]["name"]+""" }\\thanks{"""+self.j_header["author"]["post"]+"""}\\\\[2mm] % Your name
        \\normalsize \\href{ """+self.j_header["author"]["organisation_site"]+"""  }{ """+self.j_header["author"]["organisation"]+""" } \\\\ % Your institution
        \\normalsize \\href{mailto: """+self.j_header["author"]["email"]+""" }{"""+self.j_header["author"]["email"]+"""} % Your email address
        \\vspace{-5mm}
    }
    \\date{}"""

    def enumerate_lines(self, end=""):

        for line in DEFAULT_INIT_COMMENT.replace("@date@", str(datetime.datetime.now())).split('\n'):
            yield '% {}{}'.format(line, end)

        for line in self.enumerate_header_lines():
            yield line+end

        yield self.make_title()

        yield '\\begin{document}'

        yield '\\maketitle'

        for line in self.lines:
            yield line+end
        yield '\\end{document}'

    def save2file(self, path_out):
        with open(path_out, 'w') as fw:
            for line in self.enumerate_lines(end='\n'):
                fw.write(line)


if __name__ == u"__main__":
    print(u'Run mlttree {0}'.format(datetime.datetime.now()))
    