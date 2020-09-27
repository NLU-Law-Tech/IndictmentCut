import re
# from ckiptagger_interface import ckiptagger

def find_roles(cj_doc, target_roles=['上訴人', '被告', '選任辯護人'], break_line='\r\n', name_length_limit=5, search_rows_limit=100):
    cj_doc_rows = cj_doc.split(break_line)

    role_clean_patterns = ["^即　", "律師$", "（.*）", "\(.*\)"]
    people = []
    encode_reg_role_clean_chars = "|".join(role_clean_patterns)

    last_role_flag = 'undefine'
    last_index = 1
    no_dealwith_list = ['上訴人', '代表人', '選任辯護人']
    for index, cj_doc_row in enumerate(cj_doc_rows):
        cj_doc_row = re.sub(encode_reg_role_clean_chars, "", cj_doc_row)
        # 找到上列被告就可以結束了
        if cj_doc_row.find('上列被告') != -1:
            break
        cj_doc_row_keep_full_space = cj_doc_row
        cj_doc_row = cj_doc_row.replace("　", "").replace(" ", "")
        for role in target_roles:
            encode_reg_roles = r"^"+role
            target_name_list = re.split(' |　|被|告', cj_doc_row_keep_full_space)
            if(re.match(encode_reg_roles, cj_doc_row)):
                for target_name in target_name_list:
                    if len(target_name) > name_length_limit or len(target_name) == 0:
                        continue

                    people.append({"name": target_name, "role": role})
                    last_role_flag = role

                    last_index = index + 1
                    break
                break
            elif(last_role_flag != 'undefine'):
                _role = last_role_flag
                for no_dealwith in no_dealwith_list:
                    if cj_doc_row.find(no_dealwith) != -1:
                        last_role_flag = 'undefine'
                        break

                if last_role_flag == 'undefine':
                    break

                for target_name in target_name_list:
                    if len(target_name) > name_length_limit or len(target_name) == 0:
                        continue
                    people.append({"name": target_name, "role": _role})

                    last_index = index + 1
                    break
                break

    # 過濾抓錯被告
    for person in people[:]:
        if person['name'].find('選任辯護人') != -1:
            people.remove(person)

    return people

def find_roles_plus(cj_doc, ckip, target_roles=['上訴人', '被告', '選任辯護人'], break_line='\r\n', name_length_limit=5, search_rows_limit=100):
    # 濾掉全半形空白
    cj_doc = cj_doc.replace("　", "").replace(" ", "").replace(break_line, "")

    # 只抓上列被告之前的部分
    end = cj_doc.find('上列被告')
    if end != -1:
        cj_doc = cj_doc[:end]

    # 限制長度
    cj_doc = cj_doc[:1000]

    # 提取所有人名
    name_list = []
    sentence = [cj_doc]
    entity_list = ckip.parse(sentence)
    for entity in entity_list:
        for ent in entity:
            (ws, pos, ner) = ent
            if ner == 'PERSON':
                name_list.append(ws)

    # 提取被告
    people = []
    no_dealwith_list = ['上訴人', '代表人', '選任辯護人']
    for role in target_roles:
        if role in no_dealwith_list:
            continue

        for name in name_list:
            name_T_F = True
            start = cj_doc.find(name)
            if start != -1:
                name_start = cj_doc.rfind(role, 0, start)
                # 判斷在出現被告之前是否有出現不處理的單詞
                for no_dealwith in no_dealwith_list:
                    if cj_doc.rfind(no_dealwith, 0, start) != -1:
                        if cj_doc.rfind(no_dealwith, 0, start) > name_start:
                            name_T_F = False
                            break

            if name_T_F:
                people.append({"name": name, "role": role})

    return people

def _filter_unused_defendant(defendant):
    """
    設一些rule刪除明顯不是姓名的字
    是姓名則返回True，反之則返回False
    """
    #被告姓名中有數字
    if re.search(r'[0-9]', defendant):
        return False

    #被告姓名是全英文
    if re.fullmatch(r'[a-zA-Z]+', defendant):
        return True
    #被告姓名長度介於2~5之間
    elif 6>len(defendant)>1:
        return True
    else:
        return False

def find_defendants(SPSuspect):
    """
    從SPSuspect欄位找出找出被告
    input : SPSuspect(String)
    output: defendants_list(List)
    """
    #把括號中的文字去除，避免"陳OO (本名陳XX) 男 30歲"的情況被告會抓到"(本名陳XX)"
    SPSuspect = re.sub(u"\\(.*?\\)|\\（.*?）", "", SPSuspect)
    SPSuspect_list = list(filter(None, re.split(r"\s", SPSuspect)))
    print(SPSuspect_list)
    defendant_list = [SPSuspect_list[i-1] for i in range(1, len(SPSuspect_list)) if SPSuspect_list[i] in ["男", "女"]]
    defendant_list = [defendant for defendant in defendant_list if _filter_unused_defendant(defendant)]

    return list(set(defendant_list))

if __name__ == "__main__":
    ckip = ckiptagger()
    with open('test.txt','r',encoding='utf-8') as f:
        text = f.read()

    people = []
    people = find_roles_plus(text, ckip, target_roles = ['被告'], break_line='\n')
    for p in people:
        print(p)