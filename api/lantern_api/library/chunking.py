import tiktoken

def chunk_text(text: str, max_tokens: int, token_overlap: int, model: str = "gpt-4.1-nano") -> list[str]:
    """Chunks text into pieces with a maximum number of tokens.

    Args:
        text (str): The text to chunk.
        max_tokens (int): The maximum number of tokens per chunk.
        model (str): The model name for tokenization.

    Returns:
        list[str]: A list of text chunks.
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    chunks = []
    for i in range(0, len(tokens), max_tokens):
        if i != 0:
            i -= token_overlap  # Apply overlap
        chunk_tokens = tokens[i : i + max_tokens]
        chunk_text = encoding.decode(chunk_tokens)
        chunks.append(chunk_text)

    return chunks