from textnode import TextNode, TextType
from htmlnode import HtmlNode, LeafNode

def main():
    leaf1 = LeafNode("p", "This is a paragraph of text.").to_html()
    leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html();
    print(f"leaf1 is : {leaf1}")
    print(f"leaf2 is : {leaf2}")

if __name__ == "__main__":
    main()