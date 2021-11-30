import os.path

from parse_manual.parsed_token import ParsedToken
from parse_manual.parsed_function import ParsedFunction
from parse_manual.parsed_class import ParsedClass
from parse_manual.parsed_property import ParsedProperty

from parse_manual.exceptions.KeywordNotFoundException import KeywordNotFoundException

KEYWORDS_LEVEL1 = ['function', 'class']
KEYWORDS_LEVEL2 = ['property']
SYMBOLS = [':']

NULLWORDS = [' ', '\n']
STOPWORDS = [':'] + NULLWORDS
KEYWORDS = KEYWORDS_LEVEL1 + KEYWORDS_LEVEL2 + SYMBOLS


def parse(path: str):
    content = get_file_contents(path)

    result = {}

    if content:
        tokenized_content = tokenize(content)

        split_tokenized_content = split_token_array(tokenized_content)

        for token in split_tokenized_content:
            parsed_token = parse_token(token)
            if parsed_token:
                result[parsed_token.name] = parsed_token

        return result


def tokenize(content: str) -> list:
    lex = ''
    result = []
    max_length = len(content) - 1

    for i, char in enumerate(content):

        if lex in KEYWORDS:
            result.append(lex)
            lex = ''

        if char not in NULLWORDS:
            lex += char

        if i == max_length or content[i + 1] in STOPWORDS:
            if lex:
                result.append(lex)
                lex = ''

    return result


def get_file_contents(path: str) -> str:
    result = ''
    if os.path.exists(path):
        with open(path) as f:
            result = f.read()
    return result


def split_token_array(token_array: list) -> list:

    result = []
    part = []
    length = len(token_array) - 1

    for i, token in enumerate(token_array):

        if token in KEYWORDS_LEVEL1:
            if part:
                result.append(part)
                part = []

        part.append(token)

        if i == length:
            result.append(part)

    return result


def parse_token(token: list) -> ParsedToken:

    ident = token[0]
    result = None

    if ident in KEYWORDS_LEVEL1:
        if ident == 'function':
            result = parse_function(token)
        elif ident == 'class':
            result = parse_class(token)
        else:
            raise KeywordNotFoundException

    return result


def parse_function(token: list) -> ParsedFunction:
    result = ParsedFunction()
    result.name = token[1]
    result.type = token[3]
    result.value = token[4]
    return result


def parse_class(token: list) -> ParsedClass:
    result = ParsedClass()

    result.name = token[1]

    if token[2] in SYMBOLS:
        result.meta_class = token[3]

    for i, tkn in enumerate(token):
        if tkn == 'property':
            property = ParsedProperty()
            property.name = token[i+1]
            property.type = token[i+3]

            result.properties.append(property)

    return result
