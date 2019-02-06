def median(first):
    sortedList = sorted(lst)
    listLen = len(lst)
    index = (lstLen - 1) // 2

    if (listLen % 2):
        return sortediLst[index]
    else:
        return (sortedList[index] + sortedList[index + 1])/2.0
