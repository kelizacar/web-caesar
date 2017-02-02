import string

def alphabet_position(letter):
    letter=letter.lower()
    letter_position=string.ascii_lowercase.index(letter)
    return letter_position
    #letter=input("Please enter a letter.")
    #alphabet_position(letter)

def rotate_character(char,rot):
    char=str(char)

    if char in string.ascii_lowercase:
        char_index=string.ascii_lowercase
        char_index=char_index.index(char)
        rot=int(rot)
        new_char_index=(char_index+rot)%26
        new_char=string.ascii_lowercase[new_char_index]
        return new_char

    elif char in string.ascii_uppercase:
        char_index=string.ascii_uppercase
        char_index=char_index.index(char)
        rot=int(rot)
        new_char_index=(char_index+rot)%26
        new_char=string.ascii_uppercase[new_char_index]
        return new_char

    else:
        return char

    #char=input("Which character would you like to begin with?")
    #rot=input("How many times would you like to rotate?")
    #rotate_character(rot,char)

def user_input_is_valid(cl_args):
    if len(cl_args)>1:
        if cl_args[1].isdigit():
            return True
        else:
            return False
    else:
        return False


def encrypt(text, rot):
    old_list=list(text)
    new_list=""
    for char in old_list:
        new_char=rotate_character(char,rot)
        new_list=new_list+new_char
    return new_list
