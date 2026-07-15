def commaCode(listArgument):
    result = ''
    for item in listArgument:
        if listArgument.index(item) != (len(listArgument)-1):
            result += item + ', '
        else:
            result += 'and ' + item
    return result
