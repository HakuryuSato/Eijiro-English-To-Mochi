import pyperclip

#単語の情報をペースト
def input_data():
    lines = []
    text = pyperclip.paste()
    lines = text.split("\r\n")   
    return lines

def edit_data(lines):
    parts_of_speech = ["名", "動", "形", "副", "代", "前", "接", "感","自","他"]
    #単語と例文を分ける(最初の文字が"・"かどうか)
    lines = [item for item in lines if not item == ""]
    sentence = [item for item in lines if not item.startswith("・")]
    example = [item for item in lines if item.startswith("・")]

    #本文の編集
    #1文字目が数字なら削除
    sentence = [item[1:] if item and item[0].isdigit() else item for item in sentence]

    sentence_2 = []
    for i, word in enumerate(sentence):
        if i==1:
            sentence_2.append(word)
            continue

        elif word[0] in parts_of_speech: #1文字目に品詞の頭文字があるか
            sentence_2.append("")
            sentence_2.append(word)

        else:
            sentence_2.append(word)

            
    #例文の編集
    example_2 = []
    
    example = [item[1:] for item in example] #"・"削除


    for line_example in example: #":"を空白データ化
        if ":" in line_example:
            data_split = line_example.split(" : ")
            example_2.append(data_split[0])
            example_2.append(data_split[1])
            example_2.append("")
        else:
            example_2.append(line_example)


    example_2.insert(0,'') #例文の先頭に空白データ


    #全体を結合する
    sentence_2.extend(example_2)
    sentence_2.insert(1,"---")

    #各行に改行を加える
    data_for_mochi = '\n'.join(sentence_2)

    # print("mochi用テキスト:")
    # print(data_for_mochi)

    return data_for_mochi


text = input_data()
#text = ['massive', '形', '〔通常の物に比べて〕巨大な、非常に重い', '・The massive mountain is located near our village. : 大きな山が私たちの村の近くにある。', '〔通常の数量に比べて〕極めて多い、大量の', '〔規模や程度などが〕圧倒的な、壮大な、大規模な', '《医》〔がんなどが〕病巣が広がった', '《医》〔病気などが〕重度の', '《鉱物》塊状の◆結晶構造がない、非結晶質のもの。', '《地学》〔岩石が〕層理のない', '〈俗〉〔限度を超えていて〕大変な、ひどい', '・I had a massive argument with him. : 彼とひどい口げんかをしてしまった。']
data = edit_data(text)
pyperclip.copy(data)