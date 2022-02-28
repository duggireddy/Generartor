# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      get_func_proto_from_impl_template.py
#  \brief
#      
#

import os
import re
from regexes import Find
from temp_file_utilities import FILES
import itertools
from list_storage import List
from get_data_for_mock_functions import Mock_Rte_first
from get_data_for_mock_class import Mock_Class_First


#### INPUT = ALL CALLS INSIDE THE FILE  (Rte_Function_Names.txt) #####

#### FUNCTION = THIS FUNCTION FETCH THE RELATED DATA FROM THE HEADER FILES AND  RETURN ALL DATA TYPES, ARGUMENTS FOR MOCK RTE & MOCK CLASS ####

#### OUTPUT =  CALLS, CALLS DATA TYPE, ARGUMENTS AND IT'S DATA TYPE    ####


class Rte_data:
    
    #### reading the Calls from the Rte_Function_Names.txt to find the Arguments and Return types from the header file ####
    #### path_header = PATH WHERE THE HEADER FILES(API FILES ) ARE LOCATED ####
    #### path_Gen_file = PATH WHERE TEMPORARY FILES AND ACUTAL MOCK_FILES THAT SHOULD GENERATE ####

    def Rte_Data_Gen(path_header,path_Gen_file):

        j=0
        All_Rte_Func = open(path_Gen_file +'/' +'Rte_Function_Names.txt')   
        List_Rte = All_Rte_Func.readlines()  ##### STORING ALL CALLS IN LIST FORMATE AND READING ONE BY ONE CALL TO FIND WHERE IT IS DEFINED IN THE HEADER FILE ####
        
        for i in List_Rte: 

            var = i.strip()  #### EACH CALL ASSIGN TO THE VARIABLE(var) ####
            print(var)
            New_files = os.listdir(path_header)

            for File_Name in New_files:  #### READING EACH HEADER FILE TO FIND THE CALLS INSIDE IT ####

                Code = open(path_header+'/'+File_Name, 'r')  
                test_str = Code.read()
                Matched_API = re.finditer(rf".+{var}.+", test_str, re.MULTILINE) 
                
                for Match_API in Matched_API:
                    Head = Match_API.group()  #### STORING THE ENTIRE MATCH HEADER API IN THE Head VARIABLE ####
                    print(Head)  ##### *   Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn(void) #####

                    Arguments_in_RTE_function = re.finditer(r"\(.+\)", Head, re.MULTILINE) ##### r"\(.+\)" REGEX IS USED TO FIND THE ARGUMETS WITH "( )" ######
                    for i in Arguments_in_RTE_function:
                        Arguments_in_RTE_function = re.finditer(r"[^\(].+[^\)]", i.group(), re.MULTILINE) ###### r"[^\(].+[^\)]" THIS REGEX IS USED TO FIND THE ARGUMENTS BETWENN "( )" ######
                        for i in Arguments_in_RTE_function:

                            AG = i.group() #### STORING THE ALL ARGUMENTS THAT INSIDE THE RTE CALL ####
                            # print(AG)      ##### Dt_RECORD_Coding *data ####

                            ###### create a list with nested lists   ######
                            ###### HERE WE USED NESTED LISTS BECAUSE FOR EVERY CALL WE HAVE TO STORE THE ARGUMENTS SEPERATELY ######
                            ###### FOR EVERY CALL IT CREATE ONE LIST TO STORE THE ALL ARGUMENTS RETURN TYPE #####

                            List.List_Rte_Mock_Arg.append([])

                            # NOTE : PLEASE CHECK BOTH FUNCTIONS( Mock_Rte_first AND Mock_Class_First ) FOR REQUIRED DATA #

                            ########################################################################################################################
                            #### HERE WE ARE PASSING ARGUMETS(AG), CALL(VAR) AND LIST INDEX(J), THE OUT PUT IS ARGUMENT DATA TYPE ARGUMETS NAME #### 
                            ########################################################################################################################
                            Mock_Rte_first(AG,var,j) 

                            j =j+1

                    ######################################################################################################
                    #### Head = Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn(void) ###################
                    #### HERE WE ARE PASSING MATCH HEADER TO FUNCTION  AND GET REQUIRED DATA TO GENERATE THE MOCK RTE ####
                    ######################################################################################################
                    Mock_Class_First(Head)
            print("###############################################################################")

