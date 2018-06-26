
def countSpaces(input_array):
    spaces_count = 0 
    for i in input_array:
        if i == " ":
            spaces_count += 1
    return spaces_count

def replaceSpaces(input_array, totalReplaces):
    result_array = []
    space_array = ['&','3','2']
    replaces = 0
    for i in input_array:
        if i == ' ':
            if replaces < totalReplaces:
                replaces += 1
                result_array = result_array + space_array
            else:
                return result_array
        else:
            result_array.append(i)
    return result_array

def run(input_array,input_size):
    totalReplaces = countSpaces(input_array)/3
    result = replaceSpaces(input_array,totalReplaces)
    print(result)
    #If you wanna read string result
    print(''.join(result))

if __name__ == '__main__':
    #Creating a array of char
    char_array = [c for c in "User is not allowed       "]
    run(char_array,19)
