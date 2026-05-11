from enum import Enum

class BlockTypes(Enum):
    PARAGRAPH      = "paragraph"
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   = "ordered_list"

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        if block.split("#")[-1].startswith(" "):
            return BlockTypes.HEADING

    if block.startswith("```\n") and block.endswith("```"):
        return BlockTypes.CODE
    
    for line in block.split("\n"):
        if not line.startswith(">"):
            break
    else:
        return BlockTypes.QUOTE
    
    for line in block.split("\n"):
        if not line.startswith("- "):
            break
    else:
        return BlockTypes.UNORDERED_LIST
    
    number = 1
    for line in block.split("\n"):
        if line.startswith(f"{number}. "):
            number += 1
        else:
            break
    else:
        return BlockTypes.ORDERED_LIST
    
    return BlockTypes.PARAGRAPH

def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        block = block.strip()
        if block != "":
            result.append(block)
    return result