import re

#Reading Data  From Files       
#Q=Questions , A=Answers, R=Raw, l=lowercase, U=Uppercase, F=Formatted, D=Dictionary


with open('./data/question.txt', 'r') as file:
    DATA_R___Q = file.read().split('\n')
with open('./data/answers.txt', 'r') as file:
    DATA_R___A = file.read().split('\n')
Store_Name = ''

Message_asTitle = 'I can answer your questions realted with Lifestyle For Environment'
Message_Programe_TerminatedByuser = '⚠️Program terminated...🧑‍💻\n\n'
Message_ValidName = '⚠️Please enter a valid name...🧑‍💻\n\n'
Message_NoResponse = 'No response detected'

____PREDECTED_data = []
Prediction___SYSTEM___DATA_BLACKLIST_Array = ['how', 'can', 'i', 'at', 'home', 'explain', 'about','ways']



FORMAT_l___Q = [z.lower() for z in DATA_R___Q]  # for questions
FORMAT_l___A = [x.lower() for x in DATA_R___A]  # for answers




def InvalidResponse(type):
    print(f"Invalid Response Type : {type}")




while True:
    while Store_Name == '':        
      Input_Human_asName = input("✨ Enter your name to procced:: ")
      if(Input_Human_asName == 'exit'):
        print(Message_Programe_TerminatedByuser)
        exit()
        break
      if isinstance(Input_Human_asName, int):
        print(Message_ValidName)
      else :
          Store_Name = Input_Human_asName
          print(f"👋Hello {Store_Name}!\n I am a chatbot. ℹ️{Message_asTitle}\n")
          break

      if Input_Human_asName == 'exit':
        print
        break
    Store_Name = ""
    Input_Human_asQuestion = input(f'❓[{Input_Human_asName}] Input Question :: ').lower()
    if Input_Human_asQuestion == 'exit':
        print
        break
    

    Prediction___SYSTEM = [word for word in re.findall(r'\b\w+\b', Input_Human_asQuestion) if word not in Prediction___SYSTEM___DATA_BLACKLIST_Array]

    for i, question in enumerate(FORMAT_l___Q):
        if all(keyword in question for keyword in Prediction___SYSTEM):
            ____PREDECTED_data.append(DATA_R___Q[i])
            
                    
            

    if ____PREDECTED_data:
        for i, matched_question in enumerate(____PREDECTED_data):
            print(f"{i+1}. {matched_question}")

        __Index_Manager___ = input(f'Which response would you like to see? (1-{len(____PREDECTED_data)}): ')
        try:
            __Index_Manager___ = int(__Index_Manager___)
            if __Index_Manager___ > 0 and __Index_Manager___ <= len(____PREDECTED_data):
                selected_question = ____PREDECTED_data[__Index_Manager___ - 1]
                print(f'Chatbot: {DATA_R___A[DATA_R___Q.index(selected_question)]}')
            else:
                InvalidResponse('number')
        except ValueError:
            InvalidResponse('number')
    else:
        if ____PREDECTED_data == []:
            keywords_Loop = Input_Human_asQuestion.split()
            ____PREDECTED_data = []
            found_response = False
            while not found_response:
                for x in keywords_Loop:
                    print(x)
                    if any(x in question for x in Prediction___SYSTEM):
                    #if x in question:
                        ____PREDECTED_data.append(DATA_R___Q[i])
                        found_response = True
                        break
                if not found_response:
                    print('1. No -----Response')
                    break
        else:
          if ____PREDECTED_data == []:
            keywords_Loop = Input_Human_asQuestion.split()
            ____PREDECTED_data = []
            found_response = False
            while not found_response:
                for x in keywords_Loop:
                    print(x)
                    if any(x in question for x in Prediction___SYSTEM):
                    #if x in question:
                        ____PREDECTED_data.append(DATA_R___Q[i])
                        found_response = True
                        break
                if not found_response:
                    print('No -----Response')
                    break
    

