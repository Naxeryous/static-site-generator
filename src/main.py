from textnode import TextNode, TextType

def main():
    a = TextNode("merhaba", TextType.LINK, "https://www.boot.dev")
    print(a)

main()