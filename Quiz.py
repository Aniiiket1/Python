Name = input("Who's playing:")
import os

# Function to clear the screen
def clear_screen():
    # Clear the screen command depends on the operating system
    # For Windows, use 'cls', for Unix-based systems (Linux, macOS) use 'clear'
     os.system('cls' if os.name == 'nt' else 'clear')

# Example usage
# print("This is some text on the screen.")
# input("Press Enter to clear the screen...")

# print("Screen cleared!")\
level = ["1000","10k", "100k", "1m", "10m", "100m"]
o =[["delhi","punjab", "gujrat", "rajasthan"],["texas", "california", "washington dc", "arizona"],["kyoto", "tokyo", "sapporo", "hokkaido"],["beijing", "shanghai", "hangzhou", "suzhou"],["moscow", "moskva", "kazan", "samara"],["Berlin", "Hamburg", "Munich", "Frankfurt"]]
ques = ["What is the capital of India?", "What is the capital of USA?", "What is the capital of Japan?","What is the capital of China?", "What is the capital of Russia?", "What is the capital of Germany?"]
ans = ["Delhi","Washington dc","Tokyo","Beijing","Moscow","Berlin"]
score = 0

def quiz():

  j=1
  a=0
  b=0
  for i in range(len(ques)):
    print("quest no",j,"for USD",level[i],"is :", ques[i],"\n")
    
    print(f"a. {o[i][0]}\n",f"b. {o[i][1]}\n",f"c. {o[i][2]}\n",f"d. {o[i][3]}\n" )
  # Print the result
    # print(result)
    user = input("Ans:-")
    A=user.capitalize()
    if A == ans[i]:
        j=j+1

        print("Congratulations Correct Ans")
        import time

        
        timer_duration = 1  # 5 seconds
        if (i<= (len(ques) - 4 )):
            print(f"Next Ques for  in {timer_duration} seconds.")

      
            time.sleep(timer_duration)

      

            clear_screen()
      
        else:
            clear_screen()
            
 
    else:
        print("Hatt BC")
        break
  return i
a=quiz()

if (a == (len(ques) -1)):
   print(f"congrats {Name} you have won the game" )
else:
  print("You LOSE")
