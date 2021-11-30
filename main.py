
from parse_manual.parser import parse as parse_manual
from parse_pyparsing.parser import parse as parse_pyparsing
from parse_yaml.parser import parse as parse_yaml
from parse_xml.parser import parse as parse_xml

from timer.PerformanceTimer import PerformanceTimer

# Manual Parsing
manual_timer = PerformanceTimer('Manual Parsing')
manual_timer.measure_function(parse_manual, 'sample.gen')
manual_timer.print()

# Pyparsing
pyparsing_timer = PerformanceTimer('Pyparsing')
pyparsing_timer.measure_function(parse_pyparsing, 'sample.gen')
pyparsing_timer.print()

#YAML
yaml_timer = PerformanceTimer('YAML Parsing')
yaml_timer.measure_function(parse_yaml, './parse_yaml/sample.yaml')
yaml_timer.print()

#XML
xml_timer = PerformanceTimer('XML Parsing', 10)
xml_timer.measure_function(parse_xml, './parse_xml/sample.xml')
xml_timer.print()
