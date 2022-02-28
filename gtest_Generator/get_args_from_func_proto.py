
import os
import re
from regexes import Find
from list_storage import List
from list_storage import prt
from gtest_renderer import Unit_Test

    ######################################################################################################################
    #            THIS FUNCTION IS USED TO FIND THE ALL ARGUMETS THAT RELATED TO THE CALLS, FOR THE EXCEPT CALL           #
    ######################################################################################################################

def Call_Arguments(test_str,index_RTE_List):

    regex_For_Rte = r"(([A-Za-z0-9_]+)(\())" #### THIS REGEX IS USED TO SEPERATE THE CALL NAME FOR EXCEPT_CALL ####

    matches_Rte = re.finditer(regex_For_Rte, test_str, re.MULTILINE)

    for match_Rte in matches_Rte:    

        RTE_Mock_DT1 = r"(\()(.+)(\))"  #### THIS REGEX IS USED TO PICK THE DATA(ARGUMENTS) BETWEEN THE "( ARGUMENTS )" #####

        Args = re.finditer(RTE_Mock_DT1, test_str.strip(), re.MULTILINE)

        ##### regex_Calls_Arguments THIS REGEX IS USED TO FIND THE ALL TYPES OF ARGUMENTS  #####

        regex_Calls_Arguments = r"([a-zA-Z0-9_]+ \*[a-zA-Z0-9_]+)|([a-zA-Z0-9_]+ [a-zA-Z0-9_]+ \*[a-zA-Z0-9_]+)|[a-zA-Z0-9_]+ [a-zA-Z0-9_]+"

        for All_Args in Args:

            matches_Args = re.finditer(regex_Calls_Arguments, All_Args.group(2), re.MULTILINE)

            for match in matches_Args:

                if '*' in match.group():
                    ##### COLLECTING THE ARGUMENTS AND REMOVING THE "*" FROM ARGUMENTS WHICH IS USED IN UNIT TEST FOR PASSING VALUES ####


                    List.List_Call_Arg[index_RTE_List].append(match.group().replace("*", ""))
                    
                    regex_Ptr_Arg = r"\*([a-zA-Z0-9_]+)"   ###### REGEX IS USED TO SEPERATE THE ARGUMENT POINTER VARIABLE FROM THE ARGUMENT ######  

                    matches_Ptr_Arg = re.finditer(regex_Ptr_Arg, match.group(), re.MULTILINE)

                    for matches in matches_Ptr_Arg:

                        
                        ####### THIS IS USED TO GENERATE CALL WITH ARG VARIABLE FOR EXCEPT_CALL #####
                        List.List_Call_Arg_Ptr[index_RTE_List].append(match_Rte.group(2) +"_"+ matches.group(1).strip().upper())

                        ####### THIS IS USED TO GENERATE POINTER VARIABLE FOR EXCEPT_CALL #####
                        List.List_Call_Arg_Var[index_RTE_List].append(matches.group(1).strip())

                else:

                    List.List_Call_Arg[index_RTE_List].append(match.group().strip())


