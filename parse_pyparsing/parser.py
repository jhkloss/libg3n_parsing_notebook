import os.path

from pyparsing import Word, Literal, Opt, ZeroOrMore, OneOrMore, alphanums


function = Literal('function') + Word(alphanums) + Opt(':' + Word(alphanums)) + Word(alphanums)

property = Literal('property') + Word(alphanums) + Literal(':') + Word(alphanums)

cls = Literal('class') + Word(alphanums) + Opt(':' + Word(alphanums)) + ZeroOrMore(property)

grammar = OneOrMore(function ^ cls)


def parse(file: str):

    if os.path.exists(file):
        parsed = grammar.parseFile(file)
        return parsed
