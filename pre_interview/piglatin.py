class PigLatin():    

    def find_subsequent_ques(self, word):
        lword = list(word) # convert word into a list
        lword_subs = []; # initialize an empty list to fill in the separate lists

        # STEP 1: break the lword list at into separate lists whenever you find a digit
        # append the separate lists into a single list called lword_subs
        for i, c in enumerate(lword):
            if (c.isdigit()):
                lword_subs.append(lword[i:])

        matches = [] # initialize an empty list for matches found

        # STEP 2: get the diffrences between the list in the lword_subs, which will be
        # the characters between one digit in lword and the next
        for i in range(len(lword_subs)):
            try:

                ldiff = (len(lword_subs[i]) - len(lword_subs[i+1])) # size of the gap between the two digits
                que_list = [] # initialize empty list to append the question marks

                # loop through the lword_subs checking only the characters in between a digit and
                # the next digit as they appear in the original word
                for _, c in enumerate(lword_subs[i][1:ldiff]):
                    if(c == '?'):
                        que_list.append(c)

                # add the two digits involved (these will be the first of the two subsequent lists)
                digits_sum = int(lword_subs[i][0]) + int(lword_subs[i+1][0])

                if(digits_sum == 10): # check that the two digits in 'digits_sum' add up to 10
                    if(len(que_list) == 3): # check that the list 'que_list' has exactly 3 question marks
                        matches.append(True)
                    else:
                        matches.append(False)

            except IndexError:
                break

        # check if matches list is not empty and only consits of bool: True flags
        if (len(matches) > 0 and all(match == True for match in matches)):
            return True
        else:
            return False


if __name__ == "__main__":
    pgl = PigLatin()

    # word = "5??aaaaaaaaaaaaaaaaaaa?5?5"
    # print(pgl.find_subsequent_ques(word))

    # check multiple strings
    word_list = [
                 "arrb6???4xxbl5???eee5",
                 "acc?7??sss?3rr1??????5",
                 "5??aaaaaaaaaaaaaaaaaaa?5?5",
                 "9???1???9???1???9",
                 "aa6?9"
                ]

    for _, word in enumerate(word_list):
        print(pgl.find_subsequent_ques(word))

