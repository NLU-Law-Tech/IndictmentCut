import re

def find_evidence(cj_doc, break_line='\r\n'):

    reg_break_line = break_line.replace('\r','\\\r')
    reg_break_line = reg_break_line.replace('\n','\\\n')

    rgs1 = '\\s*證\\s*據\\s*並\\s*所\\s*犯\\s*法\\s*條\\s*' + reg_break_line

    rgs2 = "\\s此\\s*致\\s*" + reg_break_line + "|\\s*此\\s致\\s*"
    rgs22 = "此致|\\s{3}此致|此\\s*致"

    data = ""
    # 抓證據
    evidence = re.search(rgs1, cj_doc)
    if evidence != None:
        cj_doc = cj_doc[evidence.end():]
        
        # 抓此致
        sincere = re.search(rgs2, cj_doc)
        if sincere == None:
            sincere = re.search(rgs22, cj_doc)

        if sincere != None:
            data = cj_doc[:sincere.start()] 
        else:
            print('該篇沒有抓到此　致-----\n')
            print(cj_doc + '\n')
            print('----------------------\n')
    else:
        print('該篇沒有抓到證據並所犯法條-----\n')
        print(cj_doc + '\n')
        print('-----------------------------\n')
    
    return data

def find_evidence_plus(cj_doc, break_line='\r\n'):

    reg_break_line = break_line.replace('\r','\\\r')
    reg_break_line = reg_break_line.replace('\n','\\\n')

    rgs2 = "\\s此\\s*致\\s*" + reg_break_line + "|\\s*此\\s致\\s*"
    rgs22 = "此致|\\s{3}此致|此\\s*致"

    data = ""
    # 抓證據
    start = cj_doc.rfind('證據並所犯法條')
    if start != -1:
        cj_doc = cj_doc[start+len('證據並所犯法條'):]
        
        # 抓此致
        sincere = re.search(rgs2, cj_doc)
        if sincere == None:
            sincere = re.search(rgs22, cj_doc)

        if sincere != None:
            data = cj_doc[:sincere.start()] 
        else:
            print('該篇沒有抓到此　致-----\n')
            print(cj_doc + '\n')
            print('----------------------\n')
    else:
        print('該篇沒有抓到證據並所犯法條-----\n')
        print(cj_doc + '\n')
        print('-----------------------------\n')
    
    return data


if __name__ == "__main__":
    with open('test.txt','r',encoding='utf-8') as f:
        text = f.read()

    print(find_evidence(text, break_line='\n'))