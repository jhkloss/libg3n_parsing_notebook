import unittest

from parse_manual.parser import tokenize, split_token_array, parse_token, parse_class, parse_function

from parse_manual.parsed_token import ParsedToken
from parse_manual.parsed_function import ParsedFunction
from parse_manual.parsed_class import ParsedClass


class TestManualParse(unittest.TestCase):

    # File Contents
    content: str = ''

    # Content Tokens
    tokenized_content = ['function', 'test1', ':', 'return', 'value1', 'function', 'test2', ':', 'return', 'value2',
                         'class', 'Train', 'property', 'mass', ':', 'int', 'property', 'model', ':', 'str', 'class',
                         'Train2', ':', 'MetaModel', 'property', 'mass', ':', 'int', 'property', 'model', ':', 'str']

    split_token_array = [['function', 'test1', ':', 'return', 'value1'],
                         ['function', 'test2', ':', 'return', 'value2'],
                         ['class', 'Train', 'property', 'mass', ':', 'int', 'property', 'model', ':', 'str'],
                         ['class', 'Train2', ':', 'MetaModel', 'property', 'mass', ':', 'int', 'property', 'model',
                          ':', 'str']]

    # Function Token
    function_token = ['function', 'test1', ':', 'return', 'value1']

    function_name = 'test1'
    function_type = 'return'
    function_value = 'value1'

    # Class Tokens
    class_token = ['class', 'Train', 'property', 'mass', ':', 'int', 'property', 'model', ':', 'str']

    class_name = 'Train'
    class_property1_name = 'mass'
    class_property1_type = 'int'
    class_property2_name = 'model'
    class_property2_type = 'str'

    class_token_meta = ['class', 'Train', ':', 'MetaModel', 'property', 'mass', ':', 'int', 'property', 'model',
                        ':', 'str']

    class_metaclass = 'MetaModel'

    @classmethod
    def setUpClass(cls) -> None:
        with open('sample.gen') as f:
            cls.content = f.read()

    @classmethod
    def tearDownClass(cls) -> None:
        del cls.content

    def test_tokenize(self):
        sample_tokenized_content = tokenize(self.content)
        self.assertListEqual(sample_tokenized_content, self.tokenized_content)

    def test_split_token_array(self):
        sample_split_token_array = split_token_array(self.tokenized_content)
        self.assertListEqual(sample_split_token_array, self.split_token_array)

    def test_parse_function(self):
        sample_function = parse_function(self.function_token)
        self.assertIsInstance(sample_function, ParsedToken)
        self.assertIsInstance(sample_function, ParsedFunction)

        self.assertEqual(sample_function.name, self.function_name)
        self.assertEqual(sample_function.type, self.function_type)
        self.assertEqual(sample_function.value, self.function_value)

    def test_parse_class(self):
        sample_class = parse_class(self.class_token)
        self.assertIsInstance(sample_class, ParsedToken)
        self.assertIsInstance(sample_class, ParsedClass)

        self.assertEqual(self.class_name, sample_class.name)
        self.assertEqual(self.class_property1_name, sample_class.properties[0].name)
        self.assertEqual(self.class_property1_type, sample_class.properties[0].type)
        self.assertEqual(self.class_property2_name, sample_class.properties[1].name)
        self.assertEqual(self.class_property2_type, sample_class.properties[1].type)

    def test_parse_meta_class(self):
        sample_class = parse_class(self.class_token_meta)
        self.assertIsInstance(sample_class, ParsedToken)
        self.assertIsInstance(sample_class, ParsedClass)

        self.assertEqual(self.class_name, sample_class.name)
        self.assertEqual(self.class_metaclass, sample_class.meta_class)
        self.assertEqual(self.class_property1_name, sample_class.properties[0].name)
        self.assertEqual(self.class_property1_type, sample_class.properties[0].type)
        self.assertEqual(self.class_property2_name, sample_class.properties[1].name)
        self.assertEqual(self.class_property2_type, sample_class.properties[1].type)

    def test_parse_token(self):
        sample_parsed_token_function = parse_token(self.function_token)
        self.assertIsInstance(sample_parsed_token_function, ParsedFunction)

        sample_parsed_token_class = parse_token(self.class_token)
        self.assertIsInstance(sample_parsed_token_class, ParsedClass)


if __name__ == '__main__':
    unittest.main()
