import os
import re
from regexes import Find
from list_storage import List
from get_func_proto_from_impl_template import Rte_data
from list_storage import prt
from get_function_body import Fun_St_Ed
from gtest_renderer import Unit_Test



######################################################################################################################
#      THE Fun_Name_Gen FUNCTION IS USED TO GENERATE THE ALL RUNNABLES (FUNCTIONS ) WHICH ARE IN THE .C FILES        #
######################################################################################################################

############ PASSING THE C FILE PATH ###########

def Fun_Name_Gen(Path_Main_file):
    
    files = os.listdir(Path_Main_file)
    ##########################################################################################################
    #            THIS IS USED TO FIND THE ALL FUNCTIONS IN A FILE AND STORED IN  FunctionInFunc.txt          #
    ##########################################################################################################
    for File_Name in files:

        print("The file name is " + File_Name)  #### PRINTING THE FILE NAME FOR REFERENCE ####

        Code = open(Path_Main_file+'/'+File_Name, 'r')  #### READING THE ALL FILES USING THE FOR LOOP TO GENERATE THE FUNCTION NAMES ######

        test_str = Code.read()


        Matches_Find_functions = re.finditer(Find.Functions, test_str, re.MULTILINE)     ######  THIS REGEX IS USED TO FIND THE ALL FUNCTIONS ####

        for Match_Func in Matches_Find_functions:

            List.List_Func.append(Match_Func.group().strip())  ###### WE ARE STORING THE FUNCTION WITH DATA TYPE AND ARGUMENTS #####

            matches = re.finditer(r"([a-zA-Z0-9_ ]+) ([a-zA-Z0-9_ ]+)(\()", Match_Func.group().strip(), re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):

                List.List_Name_Func.append(match.group(2).strip()) ##### HERE WE ARE STORING THE RUNNABLE NAMES ##### 


