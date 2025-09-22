import unittest

from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_repr1(self):
        node = HtmlNode()
        res = "HtmlNode(None, None, None, None)"
        self.assertEqual(node.__repr__(), res)

    def test_repr2(self):
        node = HtmlNode("h1", "hello world", None, None)
        res = "HtmlNode(h1, hello world, None, None)"
        self.assertEqual(node.__repr__(), res)

    def test_repr_children(self):
        childrenNode = HtmlNode("h1", "hello from child node", None, None)
        childrenNode2 = HtmlNode("a", None, None, {
            "href" : "https://boot.dev/courses",
            "target" : "GO STUDY"
        })
        kids = [childrenNode, childrenNode2]
        node = HtmlNode("p", "this is a parent node", kids, None)
        res = "HtmlNode(p, this is a parent node, [HtmlNode(h1, hello from child node, None, None), HtmlNode(a, None, None, {'href': 'https://boot.dev/courses', 'target': 'GO STUDY'})], None)"
        self.assertEqual(node.__repr__(), res)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "I am link", {"href" : "https://www.boot.dev/"})
        self.assertEqual(node.to_html(), '<a href="https://www.boot.dev/">I am link</a>')
    
    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello world")
        self.assertEqual(node.to_html(), "<h1>Hello world</h1>")