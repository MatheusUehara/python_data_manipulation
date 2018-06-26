
def typoRemove(first_string, second_string):
    string_size = len(first_string)
    for i in range(string_size):
        new_string = first_string[:i] + first_string[(i+1):]
        if new_string == second_string:
            #print("TYPO REMOVE FIND!!")
            return 1
    #print("TYPO REMOVE NOT FOUND")
    return 0

#TODO IMPLEMENTAR ADD TYPO METHOD
def typoAdd(first_string, second_string):
    #print("TYPO ADD CALLED")
    return 0

#TODO IMPLEMENTAR REPLACE TYPO METHOD
def typoReplace(first_string, second_string):
    #print("TYPO REPLACE CALLED")
    return 0

def run(first_string,second_string):
    typos_count = 0 
    typos_count += typoRemove(first_string,second_string)
    typos_count += typoAdd(first_string,second_string)
    typos_count += typoReplace(first_string,second_string)

    #Checking if 2 strings have one or more typos
    return True if typos_count >= 1 else  False

if __name__ == '__main__':
    print(" pale, ple -> %s" %( run('pale','ple') ) )
    print(" pales, pale -> %s" %( run('pales','pale') ) )
    print(" pale, bale -> %s" %( run('pale','bale') ) )
    print(" pale, bake -> %s" %( run('pale','bake') ) )
    print(" bake, cake -> %s" %( run('bake','cake') ) )
