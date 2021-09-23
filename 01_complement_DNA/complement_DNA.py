"""
File: complement.py
Name: An Lee
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    User can input a DNA strand, and this program can find the complement.
    pre-condition: Inform user enter a DNA strand.
    post-condition: Show the complement of DNA to user.
    """
    dna = input('Please give me a DNA strand and I\'ll find the complement:')
    # Check the input DNA strand only included letters of A,T,G and C.
    check_input_dna(dna)
    # If the len(dna) is equal to len(check_input_dna(dna)), then means input data is correct.
    # Then, we can go to build a complement DNA.
    if len(dna) == len(check_input_dna(dna)):
        upper_dna = check_input_dna(dna).upper()
        build_complement(upper_dna)
        print('The complement of '+str(upper_dna)+' is '+str(build_complement(upper_dna)))
    # If the len(dna) is not equal to len(check_input_dna(dna)), then means input data is wrong.
    else:
        print('Hey!! careful! you input a wrong DNA strand.')
        print('DNA strand only included letters of A,T,G and C. (BTW, input DNA strand is case-insensitive.)')
        print('please rerun the program.')


def check_input_dna(dna):
    normal = 'aAtTcCgG'
    check = ''
    # If the input DNA strand included wrong character, then replace it with space.
    # We can use the value of len to check.
    for i in range(len(dna)):
        if dna[i] not in normal:
            check += ""
        else:
            check += dna[i]
    return check


def build_complement(upper_dna):
    ans = ''
    # Replace each letter in upper_dna into the complement letter.
    for i in range(len(upper_dna)):
        ch = upper_dna[i]
        if ch == 'A':
            ans += 'T'
        elif ch == 'T':
            ans += 'A'
        elif ch == 'G':
            ans += 'C'
        elif ch == 'C':
            ans += 'G'
    return ans


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
