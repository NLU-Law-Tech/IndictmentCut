import re


def find_laws(Indictment_text, break_line="\r\n"):
    # 找附錄法條
    # appendix_laws_list = find_appendix_laws(Indictment_text, break_line)
    laws_list = extract_law(Indictment_text, break_line)
    return laws_list


def extract_law(Indictment_text, break_line="\r\n"):
    laws_list = []
    Indictment_text_list = Indictment_text.split(break_line)
    focus_laws_list = get_all_laws_list()
    for focus_law in focus_laws_list:
        regex_focus_law = "^"+focus_law
        for Indictment_text_a_line in Indictment_text_list:
            if re.search(regex_focus_law, Indictment_text_a_line) != None:
                laws_list.append(clean_data(Indictment_text_a_line, break_line))
    return laws_list


def get_all_laws_list():
    # 取得法條的名稱
    all_laws_list = ['中華民國刑法', '陸海空軍刑法', '國家機密保護法', '國家情報工作法',
                     '國家安全法', '洗錢防制法', '臺灣地區與大陸地區人民關係條例', '台灣地區與大陸地區人民關係條例', '貿易法',
                     '組織犯罪防制條例', '人口販運防制法', '社會秩序維護法', '戰略性高科技貨品輸出入管理辦法',
                     '山坡地保育利用條例', '公司法', '公民投票法', '公職人員選舉罷免法',
                     '水土保持法', '水污染防治法', '水利法', '兒童及少年性交易防制條例',
                     '空氣污染防制法', '金融控股公司法', '律師法', '政府採購法', '毒品危害防制條例',
                     '區域計畫法', '國有財產法', '票券金融管理法', '貪污治罪條例',
                     '都市計畫法', '期貨交易法', '森林法', '稅捐稽徵法', '農田水利會組織通則',
                     '農會法', '農業金融法', '槍砲彈藥刀械管制條例', '漁會法', '銀行法',
                     '廢棄物清理法', '總統副總統選舉罷免法', '懲治走私條例', '藥事法', '證券交易法',
                     '資恐防制法', '畜牧法', '破產法', '商標法', '商業登記法', '光碟管理條例',
                     '個人資料保護法', '健康食品管理法', '妨害國幣懲治條例', '通訊保障及監察法',
                     '化粧品衛生管理條例', '金融資產證券化條例', '食品安全衛生管理法',
                     '動物傳染病防治條例', '多層次傳銷管理法', '商業會計法', '信託業法',
                     '電信法', '動物用藥品管理法', '消費者債務清理條例', '專利師法',
                     '傳染病防治法', '嚴重特殊傳染性肺炎防治及紓困振興特別條例',
                     '農藥管理法', '飼料管理法', '管理外匯條例', '野生動物保育法',
                     '植物防疫檢疫法', '遺產及贈與稅法', '電子支付機構管理條例',
                     '電子票證發行管理條例', '營業秘密法', '信用合作社法', '菸酒管理法',
                     '保險法', '證券投資信託及顧問法', '證券投資人及期貨交易人保護法', '刑法']
    return all_laws_list


# 資料清洗
def clean_data(dirty_law, break_line):
    # 先去空白 再去\r\n
    clean_law = re.sub(break_line, "", re.sub(r"\s+", "", dirty_law))
    return clean_law
