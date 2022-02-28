# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      get_data_for_mock_class.py
#  \brief
#      
#

import os
import re
from regexes import Find
from temp_file_utilities import FILES
import itertools
from list_storage import List


#### Head ( *   Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn(void)) IS COMPLETE LINE THAT PASS TO FUNCTION TO FIND THE DATA TYPE OF THE CALL ####

def Mock_Class_First(Head):
    
    #### r" [^[^*].+\)|^[a-zA-Z0-9_].+" REGEX IS USED TO SELECT THE EXCACT CALL (DATATYPE FUNCTION(ARGUMENTS))  #####

    Arguments_in_RTE_function = re.finditer(r" [^[^*].+\)|^[a-zA-Z0-9_].+", Head, re.MULTILINE)

    for i in Arguments_in_RTE_function:
        RT = i.group().strip()

        List.List_Rte_Mock.append(i.group().strip())
        test_str =RT
        ##### test_str (Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn(void)) #### 
        ###############################################################################
        #        GENERATING  RTE DATA TYPE  FOR MOCK CLASS @USED IN MOCK CLASS        #
        ###############################################################################

        regex_H_RTE = r"(.+)\("  #### regex_H_RTE IS USED TO SEPERATE THE CALL NAME FROM THE CALL #### 
        matches = re.finditer(regex_H_RTE, test_str, re.MULTILINE)
        Array = []
        for matchNum, match in enumerate(matches, start=1):
                                                
            for groupNum in range(0, len(match.groups())):

                #### SEPERATING THE DATA TYPE AND RTE ####
                #### Dt_RECORD_EthDAFIn* ####

                groupNum = groupNum + 1
                store = "{group}".format(group = match.group(groupNum))
                Array = store 

                ##### FINDING POINTER DATA TYPE TYPE AND NON-POINTER DT ADDING IN TO LIST #####

                if ' *' in Array: ##### IF THE CALL IS POINTER TYPE IT WILL ENTER TO THE IF LOOP OTHERWISE ELSE #### 
                    RTE_Mock_DT = r"(.+) [a-zA-Z0-9_*]+$" ##### THIS REGEX IS USED TO GROUPING THE DATA TYPE FROM THE CALL #### 
                    matches_find_API_DT = re.finditer(RTE_Mock_DT, Array, re.MULTILINE)
                    for matchNum, match in enumerate(matches_find_API_DT, start=1):

                        for groupNum in range(0, len(match.groups())):
                            groupNum = groupNum + 1
                            DT = match.group(groupNum)
                            DT = DT +'*'  #### IF ITS POINTER DATA TYPE ADD THE "*" TO THAT ##### 
                            List.List_Rte_Mock_DT.append(DT.strip())
                else:
                    RTE_Mock_DT = r"(.+) [a-zA-Z0-9_*]+$" ##### THIS REGEX IS USED TO GROUPING THE DATA TYPE FROM THE CALL #### 
                    matches_find_API_DT = re.finditer(RTE_Mock_DT, Array, re.MULTILINE)
                    for matchNum, match in enumerate(matches_find_API_DT, start=1):

                        for groupNum in range(0, len(match.groups())):
                            groupNum = groupNum + 1
                            DT = match.group(groupNum)
                            List.List_Rte_Mock_DT.append(DT.strip())

