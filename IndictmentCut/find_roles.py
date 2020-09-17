import re

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

if __name__ == "__main__":
    with open('test.txt','r',encoding='utf-8') as f:
        text = f.read()

    people = []
    people = find_roles(text, target_roles = ['被告'], break_line='\n')
    for p in people:
        print(p)