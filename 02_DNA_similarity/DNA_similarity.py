"""
File: similarity.py
Name: An Lee
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Use this program can help user find the homology in a DNA sequence.
    pre-condition: Inform user to input "a DNA sequence to search" and "a DNA sequence to match".
    post-condition: Show user the best match DNA sequence.
    """
    long_sequence = input('Please give me a DNA sequence to search:')
    short_sequence = input('What DNA sequence would you like to match?')
    # Let each letter of long_sequence and short_sequence transform into uppercase letter.(case-insensitive)
    upper_long_sequence = long_sequence.upper()
    upper_short_sequence = short_sequence.upper()
    number = score(upper_short_sequence, upper_long_sequence)
    print('The best match is '+show_ans(number, upper_short_sequence, upper_long_sequence))


def show_ans(number, upper_short_sequence, upper_long_sequence):
    # Build the exactly answer we want to show to user.
    ans = ''
    n = number
    for i in range(n, n+len(upper_short_sequence)):
        ch = upper_long_sequence[i]
        ans += ch
    return ans


def score(upper_short_sequence, upper_long_sequence):
    us = upper_short_sequence
    ul = upper_long_sequence
    maximum = 0
    point = 0
    new_point = point
    # Check every piece in long_sequence and count each piece's point to find the best match.
    for j in range(0, len(ul)-len(us)+1):
        new_us = ''
        # Just show the piece in long_sequence that we are going to check for.
        for k in range(j, j + len(us)):
            ch_long = ul[k]
            new_us += ul[k]
        # check every letter of the specific piece in long_sequence, in order to find the match one.
        for i in range(len(us)):
            check_us = new_us[i]
            ch_short = us[i]
            # In each piece check, if the letter from long_sequence and short_sequence are match
            # We add one point on it; if there are no match, we just pass it.
            if check_us == ch_short:
                point += 1
            else:
                pass
        # If the point is bigger than original one
        # we replace the original one and renew the piece's index as maximum.
        if new_point < point:
            new_point = point
            maximum = j
            point = 0
        else:
            pass
    return maximum


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
