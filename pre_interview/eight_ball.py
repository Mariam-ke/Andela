import sys
import time
import random

class MagicBall():

    # these are the answers that will display after questions load.
    answers = [
               'May be','That is a bad idea','Thats a great idea',
               'It is possible', 'I would advise so', 'No, No, No!', 'It is an unexpected move',
               'it looks great', 'Yes', 'I am not sure', 'Choose to share ',
               'This is a random answer', 'The best it can be', 'Horrifingly doubtful'
              ]

    #Request for user to input question with a 3 secs waiting time to load answer from the string above
    def question(self):
        print('Ask me a question.')
        input('>')
        print("Thinking...")
        time.sleep(3)
        print(random.choice(self.answers))
        self.replay()


    #Ask another question, if answer is yes reload the above function to ask another question. If answer is no exit program
    #If answer is neither yes or a no output 'I apologies, I did not catch that. Please repeat' 
    #after 3 failed attempts output 'I apologies, I did not catch that. Please repeat' and exit game.
    
    def replay(self):
        user_reply, play_attempts = "yes", 0
        while user_reply != "no":
            print("Would you like to ask another question? [yes or no]")
            user_reply = str(input(">")).lower()
            if user_reply == "yes":
                self.question()
            elif user_reply == "no":
                print("\n You\'ve chosen to EXIT the game. Goodbye!")
                sys.exit(0)
            else:
                if(play_attempts > 3):
                    print("I apologies, I did not catch that too. game will EXIT Goodbye!")
                    sys.exit(0)
                else:
                    print("I apologies, I did not catch that. Please repeat. \n")
                play_attempts += 1

    #Since it's case sensetive, if answer entered in uppercase change to lowercase
    def mock_replay_inputs(self):
        user_reply = str(input(">")).lower()
        print("input text '{}' has been detected.".format(user_reply))
        return user_reply


#The below is to initialize with the test file
if __name__ == '__main__':
    mgb = MagicBall()
    mgb.question()
