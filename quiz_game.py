import colorama

class make_your_question(): # if user want to make there own quiz game then this class are run
      def __init__(self,name:str,how_many:int):
          self.quiz_name = name # here we are aking for quizz name
          self.how_many = how_many # here we asking for how many question user want to add

      def asking_questions(self) -> None:
          self.question_dictionary = {} # this dictionary used to store for quizz game question 
          self.question_dictionary_1 = {} # here we are pass that all upper quizz game question to conncetd with there quiz name
          # becuse quizz name are connceted with all question we are use ferther for iterating and showing to user for play game.
          self.how_many_options = int(input(f"Enter How Many Opption Are There For Per Question :- ")) # asking how many option for per question that in quiz
          asking_which_op = input("Enetr What Is You Like For You opptions Decoration [\"A\" or \"a\"]:- ")# give some option decoration to chose by user
          
          # this loop is main working loop all loging that used in this all are here.
          i = 1 # i start form 1 to user give value that we ask as how many question
          while i <= self.how_many: 
                self.asking_question = input(f"Enter Your Question {i}:- ") # asking Question
                print()
                # asking for opption 
                if asking_which_op == "A": # if user choos a Decoradtion "A" then run this
                   self.option_list = [64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84]
                elif asking_which_op == "a": # if user choos a Decoradtion "a" then run this
                    self.option_list = [96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116]   
                # this loop are used for option asking 
                j = 1 # j start 1 to till how many option that we ask from the user
                self.options_dictionary = {} # we are stord all options in dictionary
                while j <= self.how_many_options: 
                      self.asking_options = input(f"Enter Your Option {j}:- ") # asking optionas
                      self.options_dictionary.update(dict(zip({chr(self.option_list[j])},{self.asking_options}))) # adding in dictionay by useing update method
                      j += 1 # incremeting j's value by 1
                print()
                # aking for answer and there explnation 
                self.answer = input(f"Enter your Question {i} Answer:- ") # asking anser aslo to comparing with user answer
                # if user anser are true then we need to see then there question expling 
                self.asking_expling = input(f"Enter you Answer Explnation Here:- ") # here we asking expling of that question

                # add data in dictionary 
                # frist add all question,option of the question,answer of question,explaing of question in this below dictinary.
                self.question_dictionary.update({i:{"Question_"+str(i):self.asking_question,"Options_"+str(i):self.options_dictionary,"Answer_"+str(i):self.answer,"Explnation Of Question_"+str(i):self.asking_expling}})
                # after add in data we are connect the all question to there quiz name.
                self.question_dictionary_1.setdefault(self.quiz_name,self.question_dictionary)
                print()                    
                i += 1  # incremeting i's value by 1
                
      def saving_infile(self) -> None: # here we are saving question in file for playing quizz game.
           with open("Question_file.txt","a") as adding_title: # opening file in append mode to add data
                adding_title.write(f"\t{self.quiz_name}\n".expandtabs(25)) # here we frist adding titile that was quiz name
           m = 1 # m start value was 1 to till length of question_dictionary [ex :- if question dictionary have 3 as length the this loop run for 1,2,3]
           while m <= len(self.question_dictionary): # loop conditions
                with open("Question_file.txt","a") as adding:# agin open filr for adding data
                       # adding quizz questions
                       adding.write(f"{'Question_'+str(m)}\n{m}. {self.question_dictionary_1[self.quiz_name][m]['Question_'+str(m)]}\n")
                       # adding all options for quiz question
                       for op_saving in range(1,self.how_many_options+1):
                               # fist value befor dot that print a,b,c... value and after point that print options
                               adding.write(f"{chr(self.option_list[op_saving])}. {self.question_dictionary_1[self.quiz_name][m]['Options_'+str(m)] [chr(self.option_list[op_saving])]}\t".expandtabs(30))
                       # adding there anser and explaing of that question
                       adding.write(f'\n{"Answer_"+str(m)} :- {self.question_dictionary_1[self.quiz_name][m]["Answer_"+str(m)]}\n{"Explnation Of Question_"+str(m)} :- {self.question_dictionary_1[self.quiz_name][m]["Explnation Of Question_"+str(m)]}\n')
                       adding.write(f"\n") # adding this for new line
                m += 1 # incremeting m's value by 1
           print() 
           print("Your Quiz Is Redy...")

class playing_quiz(): # and if user only play defult quiz that was buit inside that measn this class are run.
      # showing some option when user want to play only game.
      def dispaly_defult_quizz_options(self) -> None: # use to showing deful quizz options for choose to play quizz game
          with open("question_file.txt","r") as read_data: # here we are opening file for reading question data that is inside that.
              g =  read_data.readlines() # we are user realines method that read all data at a time and return a list
              print()
              print(f"\t'Welcome To Our Quizz Game'".expandtabs(50)) # showing message
              print()
              # logic was :- we are sepret all quiz name and there data in new list.
              count = 1 # count's value was 1
              for i in range(0,len(g)): # here we iter thta list for checking quiz name so our loop run like 0 to len(that list means g)
                  if g[i][0:25] == "                         ": # here we are checking there is 0 10 25 position are sapace if yes that meas that was quiz name
                        print(f"{count}.   {g[i][25:]}",end="") # now are display that for chosing quiz name when user only want to play game.
                        count +=1  # increase count by 1
              print()
              self.user_choice = input("Enter Your Choise That You Like To Play For Quiz:- ") # here we are assking which quiz user want to play

      def dispaly_defult_quizz_question(self) -> None: # now after choosing quiz name by user we need only that quiz related question.
          with open("question_file.txt","r") as reading_data: # agin we are one that file for reading questions that related with user chosce option.
               k = reading_data.readlines() # here we are read that file agin with readlines options that reaturn all files lines as list
               print()
               print(f"\t{self.user_choice +' Game'}".expandtabs(50)) # showing message
               print()
               self.user_score = 0
               print(colorama.Fore.LIGHTBLUE_EX+f"\t'Users Score = {self.user_score}'\t"+"[ Remember It Each Question Give 1 Score Point ]".expandtabs(25)) # showing message
               print(colorama.Fore.WHITE) # chaning agin as white color
               # here we are checing quiz name
               quiz_position_in_file = [] #adding index position of quiz sapce
               for checking_space in range(0,len(k)): # here we are checking all file that why we are take for loop to 0 to len(k) and here k have all file data in form of list
                   if k[checking_space][0:25] == "                         ": # checkign here frist 0 - 25 position are sapce if it is space the that is quiz name
                           g = k.index(k[checking_space][0:]) # here we are take index of quiz 
                           quiz_position_in_file.append(g) # append that in quiz position in list
               # after checking quiz space now we are check quiz name becuse of there is multiplse quiz name that means that is multiplse space now
               # we need to find only user wanted quiz that why here we are checking quiz name also.
               questin_position_in_file = [] 
               for checking_characters in range(0,len(k)):  # here we are checking all file that why we are take for loop to 0 to len(k) and here k have all file data in form of list
                   if k[checking_characters][25:] == self.user_choice+"\n": # now here we are checking quiz name that is started position after 25 to till
                       d = k.index(k[checking_characters][0:]) # serching quizz name index position in k list with combile sapce and quiz name 
                       f = quiz_position_in_file.index(d) # now we are checking is index position are there or not 
                       if quiz_position_in_file[-1]: # here if user choose last quiz to play game then print all from starting to end
                            v = k[d:] # now here d hev position and k have list that meas it slicing one by one
                       else: # and if user not chose last quiz that meas we need to stop after next space
                           v = k[d:quiz_position_in_file[f+1]] # now here same d have index position and inside quize position in file list hev quiz name end 
                           # f + 1 means next quiz name to present quiz name for breaking to only user wanted quiz 
                       # and "v" have only user wantes quiz question
                       for checking_question_position in range(1,len(k)):# now here we are checking question number are there or not.
                            try:# here we frist try becuse we need to check only present question are printed
                                   h = v.index('Question_'+str(checking_question_position)+"\n") # here we are checking in v as question_1
                                   questin_position_in_file.append(h) #now if question_1 is there then we are append in question_postion_in_file
                            except: # if question number are not present in that that measn we need to break that.
                                 break
                       
                       self.counting_question = 0  # now we are also count user score for that at beginig user have 0 score.
                       for printing_question in range(0,len(questin_position_in_file)): # now we are iterate that all questions for showing interminal
                                   n = colorama.Style.NORMAL+colorama.Fore.WHITE+v[questin_position_in_file[printing_question]] # now inside v have question 
                                   n1 = v[questin_position_in_file[printing_question]+1] # after we are increse position to +1 for next value that was our question
                                   n2 = v[questin_position_in_file[printing_question]+2] # after we are increase position to +2 for next value that was oue options that is realted to question
                                   print(n) # now here in this we are get ouptu as question_1
                                   print(n1,end="")  # now here we are get answer as question
                                   print(n2) # now hwere we are showing options that is reated to perticular question
                                   # after showing user to we need to check ther answer 
                                   asking_answer = input("Enter Your Question Answer Here By Choosign [a , b ,  c , d]:- ") # asking user to that questions answer
                                   n3 = v[questin_position_in_file[printing_question]+3] # now here we are checking question answer that pereset in file
                                   def question_iteration_1(): # this function is checkig for only single digit value. and if single digit value is here then we are showing somw message
                                        if n3[12:] == asking_answer+"\n": # now here our answer satrt position was 12 so we are directly checking that from 12
                                            n4 = colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+v[questin_position_in_file[printing_question]+4] # now if answer was write then we need show then explanination for that answer
                                            print(n4) # here we are printting that explaniantion 
                                            self.user_score += 1 # and incresed user score by one becue user answer was true.
                                            print(f"Congratulations Your Answer Was True That Why Your Score Increse By 1 Point🎉👌✅😊") # showing message
                                            print(colorama.Style.NORMAL+colorama.Fore.WHITE)
                                        else:# if user answer is not true then show thaen wrong anser message and then write answers.
                                                print(colorama.Style.NORMAL+colorama.Fore.RED+"wrong Anser") # showing meassage as wrong
                                                print()
                                                print(colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+"Write Answer Was:- ",n3[12:],end="") # then showing write message
                                                n4 = v[questin_position_in_file[printing_question]+4]  # now if answer was write then we need show then explanination for that answer
                                                print(n4) # here we are printting that explaniantion                                            
                                                print(f"Sorry Becuse Of Your Answer Was wrong That Why This Question 1 Point are not Incresed👎❌😒") # showing message
                                                print(colorama.Style.NORMAL+colorama.Fore.WHITE)
                                   def question_iteration_2(): # this function is checkig for only double digit value. and if single digit value is here then we are showing somw message
                                        if n3[13:] == asking_answer+"\n": # becuse of this is checking by there position value for that we are change position in double value
                                            n4 = colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+v[questin_position_in_file[printing_question]+4] # now if answer was write then we need show then explanination for that answer
                                            print(n4) # here we are printting that explaniantion
                                            self.user_score += 1 # agin incresed score by one 
                                            print(f"Congratulations Your Answer Was True That Why Your Score Increse By 1 Point🎉👌✅😊")# then showing write message
                                            print(colorama.Style.NORMAL+colorama.Fore.WHITE)
                                        else:
                                                print(colorama.Style.NORMAL+colorama.Fore.RED+"wrong Anser")  # showing meassage as wrong
                                                print()
                                                print(colorama.Style.BRIGHT+colorama.Fore.LIGHTGREEN_EX+"Write Answer Was:- ",n3[13:],end="")# then showing write message
                                                n4 = v[questin_position_in_file[printing_question]+4]  # now if answer was write then we need show then explanination for that answer
                                                print(n4) # here we are printting that explaniantion  
                                                print(f"Sorry Becuse Of Your Answer Was wrong That Why This Question 1 Point are not Incresed👎❌😒")
                                                print(colorama.Style.NORMAL+colorama.Fore.WHITE)
                                   if printing_question <= 9:# if qustion have single digit then run frist function.
                                        question_iteration_1()
                                   elif printing_question >= 10:
                                        question_iteration_2()
                                 # else question have double digit then run second function.
                                   self.counting_question += 1 # here it is count how many question are there for forther communication
               print()
              

      def showing_messages(self) -> None: # now after completed all question we need to show user score
            print("\t----------------------------------------------------------------------------------------------------".expandtabs(40))
            print(f"\tHow Many Question = {self.counting_question}".expandtabs(52),end="    ") # now here we are print how many question that we count with user playing
            print(f"Wrong Answer Questions = {self.counting_question - self.user_score}",end="\t") # now is is user score
    
            f = int(self.counting_question / 2) # here we are divided by 2 of all questions that related to perticulare quiz
            if self.user_score > f: # now user score are gereter then that divided value that means user have good knolage
                 print(colorama.Style.BRIGHT+colorama.Fore.GREEN+f" User Score = {self.user_score} ") # showing user score
                 print()
                 print(f"\t 🎉🎊🥳  Well Done Your Knoledge Is Good For This {self.user_choice} Game nice played. 🎉🎊🥳 ".expandtabs(45)) # showing message
                 print(colorama.Style.NORMAL+colorama.Fore.WHITE)
            else: # and if user score are less then when we are divided value then user have not good knolage
                 print(colorama.Fore.RED+f" User Score = {self.user_score} ") # showing user score
                 print()
                 print(colorama.Fore.RED+f"\t 😒❌👎 Sorry But Your Knoledge about this {self.user_choice} is not Good Beter Luck Next Time. 😒❌👎 ".expandtabs(40))# showing message
                 print(colorama.Fore.WHITE)
            print("\t----------------------------------------------------------------------------------------------------".expandtabs(40))
            print("Thank You For Playing Our Game.") 






chowing_for_quizz = ["play game","make question"] # here we are alredy sahve options for chose only chose from that
asking_user = None # starting value is none
while asking_user not in chowing_for_quizz: # that means this loop start becuse it check user value is not in list is it is not in list that means it become true elae it false and break
    asking_user = input("What do You Want [play Game / make question] :- ") # her we are asking to user what they want to do

if asking_user.lower() == "make question": # if user choose makeing question for thater own quiz game that means we need to run make_question class
    g = make_your_question(input("Enter Your Quizz Name:- "),int(input("Enter How Many Question Do You Want to Add in that Quizz:- ")))
    g.asking_questions() 
    g.saving_infile()
    print()
elif asking_user.lower() == "play game":# if user choose play game for that means we need to run playing_quiz class
    p = playing_quiz()
    p.dispaly_defult_quizz_options()
    p.dispaly_defult_quizz_question()
    p.showing_messages()