from htmlnode import HtmlNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINK_TEXT:
            if text_node.url is None:
                raise ValueError("Missing link in link text node")
            return LeafNode("a", text_node.text, {"href" : text_node.url})
        case TextType.IMAGE_TEXT:
            if text_node.url is None:
                raise ValueError("Missing link in link text node")
            return LeafNode("img", "", {"src" : text_node.url, "alt" : text_node.text})
        case _:
            raise ValueError("Text type doesn't exist")