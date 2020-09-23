if __name__ == "__main__":
    with open('test.txt','r',encoding='utf-8') as f:
        text = f.read()

    no_breakline_text = text.replace('\r','').replace('\n','')

    print(no_breakline_text)