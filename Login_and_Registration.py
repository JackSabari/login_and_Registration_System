# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:31:05 2022

@author: Sabari
"""

# ******************************** Email Validation ****************************************

import pandas as pd

def registration1():
    
    reg_validation=input("Press [ 1 ] / [ 2 ] : ")
    if reg_validation == '1':
        Registration()
    elif reg_validation == '2':
        print("\n\n   Thank You !!!")
    else:
        registration1()

def Registration(): 
    
    Email_Validation=False
    Password_Validation=False
    global email
    global password
    global email_col
    global password_col
    global spec
    global Numbers
    print('\n########################## Registration ############################\n')
    email=input("Enter Email    : ")
    password= input("Enter Password : ")

    email_len=len(email)
    if email_len >5 :
        At_val=email.find('@')
        Index_of_immediate_At_val=At_val+1
        
        Dot_Index=email.find('.')
        
        
        Dot_Val=email[Index_of_immediate_At_val]

        Num_Spec=email[0]

        spec=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
        Numbers=['0','1','2','3','4','5','6','7','8','9']

        special_character=0
        
        for elem in email[0]:
            val=spec.count(elem)
            special_character=special_character+val

        Number_Count=Numbers.count(Num_Spec)
        
        # *********** Email Already Exist *************
        df2=pd.read_csv('contacts.csv')
        email_col=df2.iloc[:,0].tolist()
        password_col=df2.iloc[:,1].tolist()
        
        already_exist=0
        for elem in email_col:
            if elem == email:
                already_exist=already_exist+1
        if At_val > 0:
            
            if Dot_Val != '.' :
                
                if Number_Count == 0 :
                    
                    if special_character == 0:
                        
                        if Dot_Index > Index_of_immediate_At_val :
                            
                            if already_exist == 0:
                                
                                if email_len >5 :
                                    
                                    Email_Validation=True  
                                else:
                                    print("\n Email Error : \n Provide a Valid Email")

                            else:
                                print("\n Email Error : \n Email Already Exist")
                        else:
                            print("\nEmail Error : \n '.' is missing \n")                                    
                    else:
                        print("\nEmail Error : \nFirst character should not be special character \n")
                else:
                    print("\nEmail Error : \nFirst character should not be a Number \n")
            else:
                print("\nEmail Error : \nThere should not be any '.' immediate next to '@' \n")
        else:
            print("\nEmail Error : \n1.Email should have '@' \n2.First Character Should Not Be '@' \n")
                
        # ******************************* Password Validation **************************************    
        pass_len=len(password)
        spec_count1=0
        Num_count1=0
        lower_val=0
        uppper_val=0

        for elem in password:
            val3=spec.count(elem)
            val4=Numbers.count(elem)
            spec_count1=spec_count1+val3
            Num_count1=Num_count1+val4
            if elem.islower():
                lower_val=lower_val+1
            if elem.isupper():
                uppper_val=uppper_val+1

        if pass_len > 5 :
            
            if pass_len < 16:
                
                if spec_count1 > 0:
                    
                    if Num_count1 > 0:
                        
                        if lower_val > 0:
                            
                            if uppper_val > 0:
                                
                                Password_Validation=True                          
                                
                            else:
                                print("\nPassword Error : \nMin one upper case need !!!")
                        else:
                            print("\nPassword Error : \nMin one lower case need !!!")
                    else:
                        print("\nPassword Error : \nMin one number needed !!!") 
                else:
                    print("\nPassword Error : \nMin one special character need !!!")
            else:
                print("\nPassword Error : \nLength must be less than 16 !!!")
        else:
            print("\nPassword Error : \nLength must be greater than 5 !!!")
                 

        # ********************* Store the Validated Data into CSV file ***************************

        if Email_Validation == False or Password_Validation ==False :
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("\n1.Do You Want to Continue Registration \n2.Quit")
            reg_validation=input("\n Press [ 1 ] / [ 2 ] : ")
            if reg_validation == '1':
                Registration()
            elif reg_validation == '2':
                print("\n\n    Thank You !!!")
            else:
                registration1()

        if Email_Validation == True and Password_Validation ==True :
            
            print("\n Registration Success !!! \n \n Thank You !!! \n")
            
            file='contacts.csv'
            df=pd.DataFrame( {'Email': [email] ,'Password': [password] } )
            df.to_csv(file,index=False,header=False,mode='a+')

       

    
    else:
        print("\nEmail Error    : Please Provide a Valid Email !!!")
        print("Password Error : Please Provide a Valid Password !!!")
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n1.Do You Want to Continue Registration \n2.Quit")
        reg_validation=input("\nPress [ 1 ] / [ 2 ] : ")
        if reg_validation == '1':
            Registration()
        elif reg_validation == '2':
            print("\n\n    Thank You !!!")
        else:
            registration1()
            
def retrive_pass():
    
    global forgot_email
    df3=pd.read_csv('contacts.csv')
    email_list=df3.iloc[:,0].tolist()
    password_list=df3.iloc[:,1].tolist()
    
    forgot_email_index=email_list.index(forgot_email)
    forgot_password=password_list[forgot_email_index]
    print("Your password is : " ,forgot_password)

def update_pass1():
    password_update_retry=input("\nPress [ 1 ] / [ 2 ] : ")
    if password_update_retry == '1':
        update_pass()
    elif password_update_retry == '2':
        print("\n \n  Thank you !!!")
    else:
        update_pass1()

def update_pass():
    global forgot_email
    
    spec=['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    Numbers=['0','1','2','3','4','5','6','7','8','9']

    Password_Validation5=False
    file='contacts.csv'
    df=pd.read_csv('contacts.csv')
    df4=df[df['Email']== forgot_email ].index.values
    df_val=0
    for dfs in df4:
        df_val=dfs
    change_password =input("\n Enter Your New Password : ")
    pass_len=len(change_password)

    spec_count1=0
    Num_count1=0
    lower_val=0
    uppper_val=0

    for elem in change_password:
        val3=spec.count(elem)
        val4=Numbers.count(elem)
        spec_count1=spec_count1+val3
        Num_count1=Num_count1+val4
        if elem.islower():
            lower_val=lower_val+1
        if elem.isupper():
            uppper_val=uppper_val+1

    if pass_len > 5 :
        
        if pass_len < 16:
            
            if spec_count1 > 0:
                
                if Num_count1 > 0:
                    
                    if lower_val > 0:
                        
                        if uppper_val > 0:
                            
                            Password_Validation5=True                          
                            
                        else:
                            print("\nPassword Error : \nMin One Upper Case Needed")
                    else:
                        print("\nPassword Error : \nMin ONe Lower Case Needed")
                else:
                    print("\nPassword Error : \nMin one Number needed") 
            else:
                print("\nPassword Error : \nMin one Special Character Needed")
        else:
            print("\nPassword Error : \nLength must be Less than 16 ")
    else:
        print("\nPassword Error : \nLength must be Greater than 5")
    
    if Password_Validation5 == True :
        df.loc[df_val,'Password'] = change_password  
        df.to_csv(file,index=False)
        print("\n Your New Password is :"+ change_password +"\n      Thank you !!!")
    elif Password_Validation5 == False:
        print("\n1.Change Password \n2.Quit")
        password_update_retry=input("\npress [ 1 ] / [ 2 ] : ")
        if password_update_retry == '1':
            update_pass()
        elif password_update_retry == '2':
            print("\n  Thank you !!!")
        else:
            update_pass1()

def forgot_pass1():
    retry1=input("\n Do You Want To Create a Account [ Y ] / [ N ] : ")
    if retry1 == 'Y' or retry1 == 'y':
        Registration()
    elif retry1 == 'N' or retry1 == 'n':
        print("\n Thank You!!!")        
    else :
        forgot_pass1()

def forgot_pass2():
        forgot_password_p1=input("\n Press [ 1 ] / [ 2 ] : ")
        if forgot_password_p1 == '1':
            retrive_pass()
        elif forgot_password_p1 == '2': 
            update_pass()
        else:
            forgot_pass2()
    
def forgot_pass():
    global forgot_email
    forgot_email=input("\n Enter Your Registered Email : ")
    df3=pd.read_csv('contacts.csv')
    email_list=df3.iloc[:,0].tolist()
    forgot_email_count=email_list.count(forgot_email)
    if forgot_email_count >0 :
        print("\n1. Retrive Password  \n2. Update Password")
        forgot_password_p1=input("\n Press [ 1 ] / [ 2 ] : ")
        if forgot_password_p1 == '1':
            retrive_pass()
        elif forgot_password_p1 == '2': 
            update_pass()
        else:
            forgot_pass2()
    elif forgot_email_count< 1 :
        create_acc=input("\n Your email is not registered !!!\n\n Do You Want To Create a Account [ Y ] / [ N ] : ")
        if create_acc == 'Y' or create_acc == 'y':
            Registration()
        elif create_acc == 'N' or create_acc == 'n':
            print("\n Thank You!!!")
        else:
            forgot_pass1()              
       
def check1():
    retry=input("\n\n Do you want to Login Again [Y] / [N] : ")
    if retry == "Y" or retry == "y":
        login()
    elif retry == "N" or retry == "n":
        print("\n  Thank you !!!!!!")
    else:
        check1()
        
def check2():
    retry=input("\n\n    Press [ 1 ] / [ 2 ] / [ 3 ] : ")
    if retry == '1':
        check1()
    elif retry == '2':
        Registration() 
    elif retry == '3':
        forgot_pass()    
    else:
        check2()

def login():
    i=1
    global email
    global password
    global email_col
    global password_col
    df2=pd.read_csv('contacts.csv')
    email_col=df2.iloc[:,0].tolist()
    password_col=df2.iloc[:,1].tolist()
    print("\n########################## Login System  ############################\n") 
    while i < 4:
        user_name1=input("\nEnter Email    : ")
        password1=input("Enter Password : ")
        
        for elem in email_col:
            if elem == user_name1:              
                email_index=email_col.index(user_name1)
                break
            elif elem != user_name1:
                email_index='user name is not matched'
                
        for elem1 in password_col:
            if elem1 == password1:
                password_index=password_col.index(password1)
                break
            elif elem1 != password1:
                password_index='password not matched'
        if email_index == password_index :
             print("\nLogin Successful!!! \n\n  Welocme !!!")  
             break
        else:
           print(f"\n***************** Attempt {i} Failed *****************\n")
            
        i=i+1

        if i == 4:
            retry=input("1.Do you want to Login Again \n2.Create a Account \n3.Forgot Password \n4.Quit\n\n    Press [ 1 ] / [ 2 ] / [ 3 ] / [ 4 ] : ")
            if retry == '1':
                check1()
            elif retry == '2':
                Registration()
            elif retry == '3':
                forgot_pass()
            elif retry == '4':
                print("\n\n   Thank You !!!")
            else:
                check2()
                          
def office():
    print("########################## Welcome to Office ##########################")
    print("\n1.Login \n2.Register")
    user_input=input("\n\nPress [ 1 ] / [ 2 ] : ")
    if user_input == '1':
        login()
    elif user_input == '2':
        Registration()
    else:
        office()

office()    


