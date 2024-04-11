from typing import Counter


def reorganiseString(str):
    splittedStr = Counter(str)
    mostRepeatedNum = sorted(
        splittedStr.items(), key=lambda x: x[1], reverse=True)
    print(mostRepeatedNum)
    # res = []
    # elem = temp[0][1]

    # while elem > 0:
    #     if res is None:
    #         elem.append(elem)
    #     elem


reorganiseString('fggsafd')
