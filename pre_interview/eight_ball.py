import sys
import time
import random

class MagicBall():

    answers = [
               'May be','That is a bad idea','Thats a great idea',
               'It is possible', 'I would advise so', 'No, No, No!', 'It is an unexpected move',
               'it looks great', 'Yes', 'I am not sure', 'Choose to share ',
               'This is a random answer', 'The best it can be', 'Horrifingly doubtful'
              ]

    def question(self):
        print('Ask me a question.')
        input('>')
        print("Thinking...")
        time.sleep(3)
        print(random.choice(self.answers))
        self.replay()


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

    def mock_replay_inputs(self):
        user_reply = str(input(">")).lower()
        print("input text '{}' has been detected.".format(user_reply))
        return user_reply



if __name__ == '__main__':
    mgb = MagicBall()
    mgb.question()