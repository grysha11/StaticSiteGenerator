import unittest

from convert import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import HtmlNode, LeafNode

class Convert(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_plain_text(self):
        node = TextNode("Hello world", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello world")
        self.assertEqual(html_node.props, None)
        self.assertEqual(html_node.to_html(), "Hello world")

    def test_bold_text(self):
        node = TextNode("Bold stuff", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold stuff")
        self.assertEqual(html_node.to_html(), "<b>Bold stuff</b>")

    def test_italic_text(self):
        node = TextNode("Italic words", TextType.ITALIC_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic words")
        self.assertEqual(html_node.to_html(), "<i>Italic words</i>")

    def test_code_text(self):
        node = TextNode("print('hi')", TextType.CODE_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hi')")
        self.assertEqual(html_node.to_html(), "<code>print('hi')</code>")

    def test_link_text_with_url(self):
        node = TextNode("Boot.dev", TextType.LINK_TEXT, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
        self.assertEqual(
            html_node.to_html(),
            '<a href="https://boot.dev">Boot.dev</a>'
        )

    def test_link_text_missing_url(self):
        node = TextNode("Broken link", TextType.LINK_TEXT)
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Missing link in link text node")

    def test_image_text_with_url(self):
        node = TextNode("Alt text", TextType.IMAGE_TEXT, "image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "image.png", "alt": "Alt text"}
        )
        self.assertEqual(
            html_node.to_html(),
            '<img src="image.png" alt="Alt text"></img>'
        )

    def test_image_text_missing_url(self):
        node = TextNode("Missing image", TextType.IMAGE_TEXT)
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Missing link in link text node")

    def test_unsupported_text_type(self):
        class NotAType:
            pass
        node = TextNode("Something", NotAType())
        with self.assertRaises(ValueError) as cm:
            text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Text type doesn't exist")