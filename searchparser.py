import re

class Parser:
    def parse_images(file, search_text):
    result = []
    tag_pattern = r'([a-zA-Z][^\t\n\r\f />\x00]*)'
    alt_pattern = r'alt="(.*)"'
    img_pattern = r'([-\w]+\.(?:jpg|gif|png|webp))'

    with open(file, 'r') as HTML_file:
        for raw in HTML_file:
            tag = re.findall(tag_pattern, raw, re.IGNORECASE)
            if len(tag) > 0:
                if tag[0] == 'img':
                    alt_attribute = re.findall(alt_pattern, raw, re.IGNORECASE)
                    if alt_attribute[0] != '':
                        alt_text = alt_attribute[0]
                        if search_text == alt_text:
                            result.append(raw)
                    else:
                        src_file = re.findall(img_pattern, raw, re.IGNORECASE)
                        if search_text == src_file[0].split('.')[0]:
                            result.append(raw)
    return ''.join(result)