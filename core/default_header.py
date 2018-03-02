# -*- coding: utf-8 -*-
"""
MLT
default_header
TODO

Created by pavel on 02.03.18 14:28
"""

DEFAULT_HEADER = [
    ('documentclass', '\\documentclass[twoside]{article}', '\\documentclass[@1]{@2}'),
    ('inputenc', '\\usepackage[utf8x]{inputenc} % Включаем поддержку UTF8 ', '\\usepackage[@1]{inputenc}'),
    ('babel', '\\usepackage[english, russian]{babel}  % Включаем пакет для поддержки русского языка  ', '\\usepackage@L{babel}'),
    ('fontenc', '\\usepackage[T1]{fontenc} % Use 8-bit encoding that has 256 glyphs', '\\usepackage[@1]{fontenc}'),
    ("linespread", "\\linespread{1.05} % Line spacing - Palatino needs more space between lines", "\\linespread{@1}"),
    ("microtype", "\\usepackage{microtype} % Slightly tweak font spacing for aesthetics", None),
    ("geometry", "\\usepackage[hmarginratio=1:1,top=32mm,columnsep=20pt]{geometry} % Document margins", '\\usepackage@L'),
    ("multicol", "\\usepackage{multicol} % Used for the two-column layout of the document", None),
    ("caption", "\\usepackage[hang, small,labelfont=bf,up,textfont=it,up]{caption} % Custom captions under/above floats in tables or figures", '\\usepackage@L'),
    ("booktabs", "\\usepackage{booktabs} % Horizontal rules in tables", None),
    ("float", "\\usepackage{float} % Required for tables and figures in the multi-column environment - they need to be placed in specific locations with the [H] (e.g. \\begin{table}[H])", None),
    ("hyperref", "\\usepackage{hyperref} % For hyperlinks in the PDF", None),
    ("lettrine", "\\usepackage{lettrine} % The lettrine is the first enlarged letter at the beginning of the text", None),
    ("paralist", "\\usepackage{paralist} % Used for the compactitem environment which makes bullet points with less space between them", None),
    ("abstract", "\\usepackage{abstract} % Allows abstract customization", None),
    (None, "\\renewcommand{\\abstractnamefont}{\\normalfont\\bfseries} % Set the 'Abstract' text to bold", None),
    (None, "\\renewcommand{\\abstracttextfont}{\\normalfont\\small\\itshape} % Set the abstract itself to small italic text", None),
    ("titlesec", "\\usepackage{titlesec} % Allows customization of titles", None),
    (None, "\\renewcommand\\thesection{\Roman{section}} % Roman numerals for the sections", None),
    (None, "\\titleformat{\section}[block]{\large\scshape\centering}{\\thesection.}{1em}{} % Change the look of the section titles", None),  # TODO дать возможность поправить формат
    (None, "\\titleformat{\subsection}[block]{\large}{\\thesubsection.}{1em}{} % Change the look of the section titles", None), # TODO дать возможность поправить формат
    ("fancyhdr", "\\usepackage{fancyhdr} % Headers and footers", None),
    ("fancy", "\\pagestyle{fancy} % All pages have headers and footers", None),
    ("graphicx", "\\usepackage{graphicx}", None),
    ("tikz", "\\usepackage{tikz}", None),
    ("textcomp", "\\usepackage{textcomp}", None),
    ("usetikzlibrary", "\\usetikzlibrary{shapes,arrows}", "\\usetikzlibrary@S"),
    ("amsmath", "\\usepackage{amsmath} % для \\begin{equation*} ... \\end{equation*}", None),
    ("bm", "\\usepackage{bm} % для жирного математического выделения $\bm{...}$ = \textbf{...}", None),
    ("amssymb", "\\usepackage{amssymb} % для \\boxminus", None),
    ("amsfonts", "\\usepackage{amsfonts} % Для команды \mathbb {NZQRC}", None),
    ("longtable", "\\usepackage{longtable}", None),
    ("wrapfig", "\\usepackage{wrapfig} % Обтикания", None),
]

assert len(set(x[0] for x in DEFAULT_HEADER if x[0] is not None)) == len([1 for x in DEFAULT_HEADER if x[0] is not None])


# TODO
"""

\fancyhead[C]{
Слипенчук Павел
$\bullet$ на правах рукописи
} % Custom header text

\fancyfoot[RO,LE]{\thepage} % Custom footer text
"""