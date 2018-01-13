import unittest
from implementation import Parser
import sys
import io
import os


class ParserUnitTests(unittest.TestCase):
    def test_primitive_parser(self):
        newick = "(A, (B, C), (D, E));"
        output = io.StringIO()
        sys.stdout = output
        Parser.Parser(newick, "p")
        correct_response = """Checking format correction...
                    (A, (B, C), (D, E));
                    Format ok.
                    
                       /-A
                      |
                      |   /-B
                    --|--|
                      |   \-C
                      |
                      |   /-D
                       \-|
                          \-E"""
        self.assertEqual(' '.join(output.getvalue().split()), ' '.join(correct_response.split()))

    def test_wrong_value(self):
        wrong_value = ")A, B;"
        output = io.StringIO()
        sys.stdout = output
        Parser.Parser(wrong_value, "p")
        correct_response = """Checking format correction...
                            )A, B;
                            Wrong format. Please try again."""
        self.assertEqual(' '.join(output.getvalue().split()), ' '.join(correct_response.split()))

    def test_draw_and_display(self):
        list_of_nodes = "(((a:0.05645,b:0.05962):0.05546,c:0.12003):0.06922,(d:0.00398,e:0.00113):0.244435);"
        output = io.StringIO()
        sys.stdout = output
        Parser.Parser.parse(self, list_of_nodes, "d")
        self.assertEqual(output.getvalue().split(), [])

    def test_draw_and_save(self):
        list_of_nodes = "(((a:0.05645,b:0.05962):0.05546,c:0.12003):0.06922,(d:0.00398,e:0.00113):0.244435);"
        path = os.getcwd() + "/tree.png"
        try:
            os.remove(path)
        except OSError:
            pass
        Parser.Parser.parse(self, list_of_nodes, "s")
        self.assertTrue(os.path.exists(path))


u = ParserUnitTests()
