import os
import re
from regexes import Find
from list_storage import List
from get_func_proto_from_impl_template import Rte_data
from list_storage import prt
from get_function_start_end_indices import Fun_sto
from find_function_calls import Except_Calls

# Global variable for storing intermediate files 
gtest_intermediates_path = 'Intermediates'

class Fun_St_Ed:

    def Find_str_End(Path_Main_file):

        files = os.listdir(Path_Main_file)

        for File_Name in files:

            print("The file name is " + File_Name)  # file name

            Code = open(Path_Main_file+'/'+File_Name, 'r')  # reading the all files using the for loop

            test_str_line = Code.readlines()
            Length_List_Func = len(List.List_Func)
            for E_line_func in List.List_Func:   ### READING EACH FUNCTION ### 
                index_fun = List.List_Func.index(E_line_func)
                List.List_EXPECT_CALL_Rte.append([])

                for i in range(len(test_str_line)):
                    if E_line_func in test_str_line[i]:  # CHECKING EACH FUNCTION THAT IS IN THE LIST WITH DATA IN FILE AND IF ITS START FROM THE INDEX AND ENTER IN TO THE LOOP TO FIND THE FUNCTION STARTING AND ENDING 


                        #############################################################################################################################
                        #              THIS FUNCTION IS USED TO FIND THE STARTING AND ENDING INDEX OF THE FUNCTION WHICH IS INSIDE OF THE FILE      #
                        #                  AND STORED IN Trail_Functions.txt                                                                        #
                        # ########################################################################################################################### 
                         
                        ###### i = INDEX, WHEN THE FUNCTION IS MACHES TO TEXT INSIDE THE FILE THEN THE INDEX i PASSED TO FUNCTION TO STORE THE WHOLE FUNCTION ######
                        ###### test_str_line = PASSING THE SAME FUNCTION DATA FILE FOR SEPERATE THE WHOLE FUNCTION AND  STORING THE EACH FUNCTION FROM STARTING("{") TO ENDING "}" USING INDEX #### 

                        Fun_sto(i,test_str_line,(os.path.join(gtest_intermediates_path,"Trail_Functions.txt")))
                                
                        Func_Code = open((os.path.join(gtest_intermediates_path,"Trail_Functions.txt")), 'r')  # READING THE FUNCTION INSTANTLY FROM THE Trail_Functions.txt FILE 
                        next(Func_Code)  #### READING THE FILE FROM THE SECOND LINE ####
                        Func_test_str = Func_Code.read()                        

                        #####################################################################################################################
                        #            FINDING THE FUNCTIONS INSIDE THE FUNCTIONS AND STORE THE CALLS THAT ARE INSIDE THE ALL FUNCTIONS       #
                        #####################################################################################################################

                        Fun_In_Fun_Regex = r"[a-zA-Z0-9_]+\(.+\)|[a-zA-Z0-9_]+\(\)" #### THIS REGEX USED TO FIND THE FUNCTION THAT INSIDE THE RUNNABLES 
                        Edit_Fun_In_Fun_Regex = r"([a-zA-Z0-9_]+)\(" #### THIS REGEX IS USED TO SEPERATE FUNCTION NAME #### 

                        Regex_F_In_F = r"([a-zA-Z0-9_]+)\(.+\)|([a-zA-Z0-9_]+)\(\)" #### THIS REGEX IS USED TO FIND THE 

                        matches = re.finditer(Regex_F_In_F, Func_test_str, re.MULTILINE)

                        for F_F_match in matches:
                                                    
                            #### THIS LOGIC IS USED TO RUN THE MATCHED GROUP ONE BY ONE ####
                            if F_F_match.group(1)== None:
                                Fun_Fun_cmp = F_F_match.group(2)
                                pass
                            else:
                                Fun_Fun_cmp = F_F_match.group(1)
                                pass

                            for cmp_func in List.List_Func: #### READING EACH FUNCTION FROM THE FUNCTION LIST ####

                                if  Fun_Fun_cmp in cmp_func:   ##### IF THE FUNCTION IN THE FUNCTION IS IN THE FUNCTION LIST ####
                                    
                                    COMP_dup_func = cmp_func                                          

                                    files_for_cmp = os.listdir(Path_Main_file)

                                    ##########################################################################################################
                                    #            HERE WE ARE USING THE RECURSSION, FECTHING THE ALL CALL RELATED TO THE FUN(FUN(FUN ...ETC)  #
                                    ########################################################################################################## 
                                    
                                    def Fun_In_Fun_In_Fun(n):
                                        
                                        for File_Name in files_for_cmp:

                                            Code_for_cmp = open(Path_Main_file+'/'+File_Name, 'r')  # reading the all files using the for loop

                                            test_str = Code_for_cmp.readlines()

                                            for test_str_each_line in test_str:
                                                
                                                #### HERE THE n IS FUNCTION NAME ####

                                                if n in test_str_each_line: ##### if the function in the file or line ##### 
                                                    index_cmp_fun = test_str.index(test_str_each_line)
                            
                                                    #####################################################################################################################################################################
                                                    #            THIS FUNCTION IS USED TO FIND THE STARTING AND ENDING INDEX OF FUNCTION AND BY USING THAT INDEX WE ARE STORING THE EACH FUNCTION IN THE FILE           # 
                                                    #                                  AND LATER WE WILL FIND THE CALLS IN SIDE THE FUNCTION                                                                            #
                                                    #####################################################################################################################################################################

                                                    Fun_sto(index_cmp_fun,test_str,(os.path.join(gtest_intermediates_path,"Trail_Functions_In_Function.txt")))

                                                    #############   CODE TO FIND ALL FUNC AND RTE AND LATER SEPERATE  #############
        
                                                    Func_In_Fun_Code = open((os.path.join(gtest_intermediates_path,"Trail_Functions_In_Function.txt")), 'r')  # READING THE FUNCTION INSTANTLY FROM THE Trail_Functions.txt FILE 
                                                    next(Func_In_Fun_Code)  #### READING THE FILE FROM THE SECOND LINE ####
                                                    Func_In_Fun_test_str = Func_In_Fun_Code.read()
                                            
                                                    #### NOTE : DONT FORGET THE INDEX REGARDING SAVING LIST(List.List_EXPECT_CALL_Rte[index_fun]) ####

                                                    ##################################################################################
                                                    #            THIS FUNCTION WILL STORE THE CALL THOSE ARE INSIDE THE RUNNABLES    #
                                                    ##################################################################################
                                                    Except_Calls(Func_In_Fun_test_str,index_fun)
                                                    
                                                    #################################################################################################
                                                    #            FINDING FUN(FUN(FUN))  IF ITS THEIR CALL THE FUNCTION " def Fun_In_Fun_In_Fun"     #
                                                    #################################################################################################

                                                    matches = re.finditer(Fun_In_Fun_Regex, Func_In_Fun_test_str, re.MULTILINE)

                                                    for match in matches:

                                                        matches = re.finditer(Edit_Fun_In_Fun_Regex, match.group(), re.MULTILINE)

                                                        for matchNum, match in enumerate(matches, start=1):
                                                            
                                                            for groupNum in range(0, len(match.groups())):
                                                                groupNum = groupNum + 1                                                            
                                                                for cmp_func_In_fun in List.List_Func:

                                                                    if match.group(groupNum) in cmp_func_In_fun:   ##### IF THE FUNCTION IN THE FUNCTION IS IN THE FUNCTION LIST ####
                                                                        C = cmp_func_In_fun                                                                            
                                                                        with open((os.path.join(gtest_intermediates_path,"Trail_Functions_In_Function.txt")), 'w') as Function_arguments:
                                                                            pass
                                                                        Fun_In_Fun_In_Fun(C) ##### passing the function 
                                                                    else:
                                                                        pass 

                                                    ##### HERE WE ARE CLEARING THE DATA IN FILE FOR THE NEXT FUNCTION ####                                                        
                                                    with open((os.path.join(gtest_intermediates_path,"Trail_Functions_In_Function.txt")), 'w') as Function_arguments:
                                                        pass

                                    #### HERE WE ARE CALLING FUNCTION AND ASSIGN THE FUNCTION NAME WHICH IS INSIDE OF THE FUNCTION #####            
                                    Fun_In_Fun_In_Fun(COMP_dup_func)


                        ##################################################################################
                        #            THIS FUNCTION WILL STORE THE CALL THOSE ARE INSIDE THE RUNNABLES    #
                        ##################################################################################
                    
                        Except_Calls(Func_test_str,index_fun)

                        ##################################################################################
                        #            FOR EVERY FUNCTION WE SHOULD CLEAR THE Trail_Functions.TXT FILE     #
                        ##################################################################################

                        with open((os.path.join(gtest_intermediates_path,"Trail_Functions.txt")), 'w') as Function_arguments:
                            pass