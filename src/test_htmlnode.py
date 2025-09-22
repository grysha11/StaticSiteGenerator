import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_a_lot_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def exception_check_html_node(self):
        node = HtmlNode()
        with self.assertRaises(NotImplementedError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "Not implemented")

    def test_leafnode_no_value(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "No value present in LeafNode")

    def test_parentnode_no_tag(self):
        node = ParentNode(None, [LeafNode("p", "Hello")])
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "No tag present in ParentNode")

    def test_parentnode_no_children(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "No children present in ParentNode")
