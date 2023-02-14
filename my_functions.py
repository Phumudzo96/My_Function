def seven_days():                             # create a function that will store my code
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(day)                                # call my function to perform my code

seven_days()

sentence = input("Enter a sentence: ")          # get input from user
word = "Hello"                                  # create a varibale for the word "Hello"
def hello():                                    # create a function
    split = sentence.split(" ")                 # split the users input
    for i in range (len(split)):      
        if i % 2 == 0:                          # get every second word from users input
            print(split[i], end=" ")            # replace every second word
        else:
            print(word, end=" ")                # with the variable you created

hello()