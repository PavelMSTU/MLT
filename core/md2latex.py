# -*- coding: utf-8 -*-
"""
MLT

md2latex

Module for convert MarkDown to LaTeX

Created by pavel on 02.03.18 14:03
"""
import os
import datetime

from settings import ROOT_PATH

from core.mlttree import MltTree

__author__ = 'pavel'


def convert(
    file_in,
    file_out
):
    """
    Simple function for convert
    :param file_in:
    :param file_out:
    :return:
    """

    mt = MltTree(None)

    with open(file_in, 'r') as fr:
        for line in fr:
            line = line.replace('\n', '')
            mt.add_line(line)

    mt.save2file(file_out)


if __name__ == u"__main__":
    print(u'Run md2latex {0}'.format(datetime.datetime.now()))

    convert(
        os.path.join(ROOT_PATH, 'example', 'one.mlt'),
        os.path.join(ROOT_PATH, 'example', 'one.tex'),
    )