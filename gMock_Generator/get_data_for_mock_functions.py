# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      get_data_for_mock_functions.py
#  \brief
#      
#

import os
import re
from regexes import Find
from temp_file_utilities import FILES
import itertools
from list_storage import List


def Mock_Rte_first(AG,var,j):
    if ' *' in AG:
       
        ##### FINDING POINTER ARGUMETS  AND NON-POINTER ARGUMETS ADDING IN TO LIST IN LIST  #####

        #### FINDING ALL POINTER ARGUMENTS ####
        regex_AG_var = r"[a-zA-Z0-9_]+ \*[a-zA-Z0-9_]+" #### THIS REGEX USED TO FIND THE POINTER ARGUMENTS #####

        Matched_AG_vars = re.finditer(regex_AG_var, AG, re.MULTILINE)
        for Matched_AG_var in Matched_AG_vars:
            Adding_Arg_var = Matched_AG_var.group().strip()


            ##############################
            #     USED IN MOCK CLASS     #
            ##############################
            #### FINDING ALL ARGUMENT DATATYPE IF ITS HAS POINTER JUST ADD THE  '*' AT END, WHICH IS USED FOR MOCK CLASS (uint8*) ####
            #### EXAMPLE ----> const Dt_RECORD_ASM *Get_PpAEB2ASM_DeAEB2ASM(uint8 *size, SubFunctionE subFunction)
            ####  USED HERE ------> MOCK_METHOD(uint8*, Rte_Read_CtCdIDC_PpCodingDataPH_SWC_DeCodingData_VALUE,());
            
            regex_AG_var_DT = r"^[a-zA-Z0-9_]+" ##### THIS REGEX IS USED TO FIND THE DATA TYPE OF THE ARGUMENT ####

            Matched_AG_vars_DT = re.finditer(regex_AG_var_DT, Adding_Arg_var, re.MULTILINE)
            for Matched_AG_var_DT in Matched_AG_vars_DT:
                Adding_Arg_var_DT = Matched_AG_var_DT.group().strip()
                List.List_Rte_Mock_Method_Arg_DT.append(Adding_Arg_var_DT+'*')##### Dt_RECORD_Coding* ####
                

            ###########################
            #     USED IN MOCK RTE    #
            ###########################
            #### FINDING ALL POINTER ARGUMENT AND REMOVING '*' IN THE STARTING AND CONVERT IT AS UPPER CASE  WHICH IS USED FOR MOCK CLASS  ####
            ######    EXAMPLE ---> MOCK_METHOD(uint8*,Get_PpParken2ASM_DeParken2ASM_SIZE,()); #####
            ##### USED THE UPPER size argument IN THE MOCK METHOD (_SIZE) #####


            regex_AG_var_Func = r"\*[a-zA-Z0-9_]+" #### THIS REGEX IS USED TO FIND THE ARGUMENT VARIABLE OR IDENTIFIER #### 
            Matched_AG_vars_Func = re.finditer(regex_AG_var_Func, Adding_Arg_var, re.MULTILINE)
            for Matched_AG_var_Func in Matched_AG_vars_Func:
                Adding_Arg_var_Func = Matched_AG_var_Func.group().strip()
                List.List_Rte_Mock_Method_Arg_Func.append(Adding_Arg_var_Func[1:].upper()) #### HERE WE ARE CHANGING TO UPPERCASE FOR THE RTE MOCK ####

            List.List_Rte_Mock_Method_Arg_RTE.append(var)  #### THIS RTE IS USED IN MOCK RTE INSIDE IF CALL HAS ARGUMENTS WITH THE POINTER ####
            
            regex_AG = r"\*[a-zA-Z0-9_]+"#### THIS REGEX IS USED TO FIND THE ARGUMENT VARIABLE OR IDENTIFIER #### 
            matches = re.finditer(regex_AG, AG, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                Adding_Arg = match.group()
                List.List_Rte_Mock_Arg[j].append(Adding_Arg)                


    else:
        
        ##########################################################################
        #     GENERATING ARGUMENTS  FOR INSIDE RTE MOCK @USED IN MOCK RTE        #
        ##########################################################################

        #### IF ITS (void) AND OTHER POINTER  IT WILL STORE HERE DIRECTLY ####

        List.List_Rte_Mock_Arg[j].append(AG)
      
      