from enum import Enum

class BlockType(Enum):
    NORMAL = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered.append(block)
    return filtered

def block_to_blocktype(markdown):
    block_type = BlockType.NORMAL
    if markdown.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        block_type = BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        block_type = BlockType.CODE
    if markdown.startswith(">"):
        block_type = BlockType.QUOTE
    if markdown.startswith("- "):
        block_type = BlockType.UNORDERED_LIST
    if markdown.startswith("1. "):
        block_type = BlockType.QUOTE
    return block_type