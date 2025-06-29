import re

def to_bold_unicode(text: str) -> str:
    def bold_char(c):
        if 'A' <= c <= 'Z':
            return chr(ord(c) - ord('A') + 0x1D400)
        elif 'a' <= c <= 'z':
            return chr(ord(c) - ord('a') + 0x1D41A)
        elif '0' <= c <= '9':
            return chr(ord(c) - ord('0') + 0x1D7CE)
        else:
            return c
    return ''.join(bold_char(c) for c in text)


def convert_markdown_bold_to_unicode(text: str) -> str:
    return re.sub(r'\*\*(.*?)\*\*', lambda m: to_bold_unicode(m.group(1)), text)


def format_model_output(raw_text: str) -> str:
    # Convert **bold** to Unicode bold
    formatted = convert_markdown_bold_to_unicode(raw_text)
    # Optional: clean long spacing from broken responses
    formatted = re.sub(r'\n{3,}', '\n\n', formatted)
    formatted = re.sub(r' +', ' ', formatted)
    return formatted.strip()
