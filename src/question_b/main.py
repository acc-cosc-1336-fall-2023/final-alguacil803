import question_b #Strings

option = str(input("Enter Y to create a string and substring: ")).lower()
while True:
    if option in ('y', 'yes'):
        while True:
            string1 = str(input("Enter your string with 8 -16 charaters: "))
            if question_b.validate_string_length(string1) == "Invalid":
                print("try again")
            else:
                break
        while True:
            string2 = str(input("Enter your substring (4 characters): "))
            if question_b.validate_substring_length(string2) == "Invalid":
                print(" not 4 characters")
            else:
                break
        result = question_b.get_most_likely_ancestor_consensus(string1, string2)
        print("results: ",end="")
        for i in range(len(result)):
            if i == (len(result)-1):
                print(result[i])
            else:
                print(result[i], end=',')
        print("")
        option = str(input("Enter Y to create a another: ")).lower()
    else:
        print("Exiting")
        break
