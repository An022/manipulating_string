"""
File: caesar.py
Name:An Lee
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    Use the concept of Caesar Cipher to cipher the secret message.
    Pre-condition: Inform user entered the secret number and the ciphered string.
    Post-condition: Give user the correct message from the ciphered string.
    """
    secret_number = int(input('Secret number: '))
    ciphered_string = input('What\'s the ciphered string?')
    # Let each letter of ciphered string transforms into uppercase letter.
    upper_ciphered_string = ciphered_string.upper()
    new_string = find_new_order(secret_number)
    print('The deciphered string is: '+tell_truth(new_string, upper_ciphered_string))


def tell_truth(new_string, upper_ciphered_string):
    cs = upper_ciphered_string
    ns = new_string
    os = ALPHABET
    ans = ''
    # Let us replace each letter of the cipher string with original letter.
    for i in range(len(cs)):
        new_ch = cs[i]
        if ALPHABET.find(new_ch) > -1:
            n_ch_n = ns.find(new_ch)
            o_ch = os[n_ch_n]
            ans += o_ch
        # If any string is not included in ALPHABET, then maintain the original string.
        else:
            ans += cs[i]
    return ans


def find_new_order(secret_number):
    os = ALPHABET
    new_alphabet = ''
    # Use the secret number to change the index of ALPHABET, then we can get a new alphabet.
    for i in range(len(os)):
        # Use the length of original string to judge when to let the new string began to cycle.
        if i+secret_number < len(os):
            ch = os[i - secret_number]
            new_alphabet += ch
        else:
            ch = os[i - secret_number-len(os)]
            new_alphabet += ch
    return new_alphabet



#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
