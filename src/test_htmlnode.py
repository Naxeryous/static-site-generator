import unittest

from htmlnode import HTMLNode


class TestHtlmNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(None, None, None, {
    "href": "https://www.google.com",
    "target": "_blank",
})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_eq2(self):
        node = HTMLNode(None, None, None, None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()