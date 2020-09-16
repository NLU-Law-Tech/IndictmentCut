import re
from .find_roles import find_roles

def find_fact(Indictment_text,break_line="\r\n"):
    fact = extract_fact(Indictment_text, break_line)
    return fact
    


def extract_fact(Indictment_text, break_line="\r\n"):
    '''
    input: 整個判決書文本(judgement欄位)
    output:	從判決書全文擷取出"事實"的部分
    '''
    reg_break_line = break_line.replace('\r', '\\\r')
    reg_break_line = reg_break_line.replace('\n', '\\\n')

    rgs_fact_start = '\\s*犯\\s*罪\\s*事\\s*實\\s*' + break_line
    rgs_fact_end = '\\s*證\\s*據\\s*並\\s*所\\s*犯\\s*法\\s*條\\s*' + reg_break_line
    fact_start_position = re.search(rgs_fact_start, Indictment_text)
    fact_end_position = re.search(rgs_fact_end, Indictment_text)
    if fact_start_position != None:
        fact=Indictment_text[fact_start_position.end():fact_end_position.start()]
    else:
        fact=Indictment_text

    return fact