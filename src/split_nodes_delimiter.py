from textnode import TextNode, TextType

def split_nodes_delimiter(nodes, delimeter, text_type):
    new_nodes = []
    for node in nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue

        if delimeter not in node.text:
            raise Exception(f"The text do not contain {delimeter} delimeter")
        
        texts = node.text.split(delimeter)
        
        result = []
        for i in range(len(texts)):
            if texts[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(texts[i], TextType.PLAIN_TEXT))
            else:
                result.append(TextNode(texts[i], text_type))
        
        new_nodes.extend(result)
        return new_nodes

        
