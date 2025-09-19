from textnode import TextNode, TextType
from htmlnode import HtmlNode

def main():
    childrenNode = HtmlNode("h1", "hello from child node", None, None)
    childrenNode2 = HtmlNode("a", None, None, {
        "href" : "https://boot.dev/courses",
        "target" : "GO STUDY"
    })
    kids = [childrenNode, childrenNode2]
    node = HtmlNode("p", "this is a parent node", kids, None)
    print(node)

if __name__ == "__main__":
    main()