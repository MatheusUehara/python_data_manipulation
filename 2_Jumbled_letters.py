from collections import Counter

def getSimilarity(first_string, second_string):
    string_size = len(first_string)
    chars_at_different_position = string_size
    for i in range(string_size):
        if first_string[i] == second_string[i]:
            chars_at_different_position -= 1
    chars_at_different_position = float(chars_at_different_position)
    string_size = float(string_size)
    return chars_at_different_position / string_size

def verifyLetters(first_string,second_string):
    return set(filter(str.isalnum, first_string)) == set(filter(str.isalnum, second_string))

def run(first_string,second_string):
    if len(first_string) != len(second_string):
        #print("FAIL CAUSED BY SIZE DIFFERENCE")
        return False
    if verifyLetters(first_string,second_string) != True:
        #print("FAIL CAUSED BY 2 strings have different characters")
        return False 
    if first_string[0] == second_string[0]:
        if len(first_string) > 3:
            similarity = getSimilarity(first_string, second_string)
            #letters position changed need be less than 2/3 of total letters
            max_modification = float(2) / float(3)
            if similarity <= max_modification:
                return True
            else:
                #print("FAIL CAUSED BY LETTERS MODIFICATION LESS THAN 2/3")
                return False
        else:
            return True
    else:
        #print("FAIL CAUSED BY FIRST LETTER DIFFERENCE")
        return False

if __name__ == '__main__':
    print(" you , yuo -> %s" %( run('you','yuo') ) )
    print(" probably , porbalby -> %s" %( run('probably','porbalby') ) )
    print(" despite , desptie -> %s" %( run('despite','desptie') ) )
    print(" moon , nmoo -> %s" %( run('moon','nmoo') ) )
    print(" misspellings , mpeissngslli -> %s" %( run('misspellings','mpeissngslli') ) )
    print(" bolo , bool -> %s" %( run('bolo','bool') ) )