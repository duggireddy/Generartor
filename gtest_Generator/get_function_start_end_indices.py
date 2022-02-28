import os
import re
from regexes import Find
from list_storage import List
from get_func_proto_from_impl_template import Rte_data
from list_storage import prt
from gtest_renderer import Unit_Test

    #####################################################################################################################################################################
    #            THIS FUNCTION IS USED TO FIND THE STARTING AND ENDING INDEX OF FUNCTION AND BY USING THAT INDEX WE ARE STORING THE EACH FUNCTION IN THE FILE           # 
    #                                  AND LATER WE WILL FIND THE CALLS IN SIDE THE FUNCTION                                                                            #
    #####################################################################################################################################################################

def Fun_sto(i,test_str_line,File_Names):
    count =0
    for j in range(i,len(test_str_line)): # FINDING THE LAST LINE OF THE FUNCTION  AND ALSO THIS LOOP IS USED TO FIND THE WHOLE FUNCTION 
        if "{" in test_str_line[j] :
            count = count+1
        if "}" in test_str_line[j]:
            count = count-1
            if count == 0:
                end_ind = j
                break   #### AFTER FINDING THE LAST "}" WRT TO FUNCTION EXIT FROM THE LOOP AND START TO MATCH THE NEW FUNCTION 

    #############################################################################################
    #            STORING THE EACH FUNCTION FROM STARTING("{") TO ENDING "}" USING INDEX         #
    #############################################################################################

    end_ind = end_ind+1  
    for sto in range(i,end_ind): 
        with open(File_Names, 'a') as f:
            f.write(test_str_line[sto] + '\n')
            
