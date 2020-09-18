import re
from IndictmentCut.find_laws import find_laws
from IndictmentCut.find_roles import find_roles
from IndictmentCut.find_laws import get_all_laws_list
from IndictmentCut.find_evidence import find_evidence

def match_name_and_law(Indictment,name_list,break_line='\r\n'):
    # 找出所犯法條(法條自己一行)
    laws_list = find_laws(Indictment, break_line)
    # 找出證據及所犯法條的段落
    Evidence = find_evidence(Indictment, break_line)
    # 取出執掌法條
    focus_laws_list = get_all_laws_list()
    # init object for each person
    for name in name_list:
        name_and_law[name] = []
    # 以句點分割
    Evidence_list = Evidence.split("。")
    for Evidence_a_line in Evidence_list:
        for focus_law in focus_laws_list:
            for name in name_list:
                if (name in Evidence_a_line )and (focus_law in Evidence_a_line):
                    print()
    return ""
