import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node1 = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node1, node2)
    
    def test_eq2(self):
        node1 = TextNode("This is a text node", TextType.LINK_TEXT, None)
        node2 = TextNode("This is a text node", TextType.LINK_TEXT)
        self.assertEqual(node1, node2)
    
    def test_not_eq1(self):
        node1 = TextNode("hihi-haha", TextType.PLAIN_TEXT, "helloeveryone.com")
        node2 = TextNode("hihi-haha", TextType.PLAIN_TEXT)
        self.assertNotEqual(node1, node2)
    
    def test_not_eq2(self):
        node1 = TextNode("hihi-haha", TextType.PLAIN_TEXT)
        node2 = TextNode("hihi-haha", TextType.IMAGE_TEXT)
        self.assertNotEqual(node1, node2)



if __name__ == "__main__":
    unittest.main()