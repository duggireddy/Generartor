

import re
from regexes import Find
from list_storage import List
from get_func_proto_from_impl_template import Rte_data
from list_storage import prt
from gtest_renderer import Unit_Test



    #####################################################################################################################################################################
    #            THIS FUNCTION IS USED TO THE ALL CALL IN SIDE THE FUNCTION AND STORE IN A LIST (List_EXPECT_CALL_Rte), THAT IS USED TO TO GENERATE THE EXCEPT CALL     # 
    #####################################################################################################################################################################

def Except_Calls(Func_test_str,index_fun):

    ##########################################################
    #            FINDING THE CALLS INSIDE THE FUNCTION       #
    ##########################################################

    # This is for the finding Rte calls IN THE EACHFUNCTION 
    if "= Rte_" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(Rte_.+)(\(.+)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(2).strip())
    
    # This is for the finding Get calls IN THE EACHFUNCTION 
    if "= Get_" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(Get_.+)(\(.+)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(2).strip())
    
    if "= pthr" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(pthr.+)(\(.+)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
                            



    # This is for the finding get calls IN THE EACHFUNCTION 

    # if "= getUpd" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

    #     Rte_adding = re.finditer(r"(= )(getUpd.+)\(\)|(= )(getUpd.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

    #     for Match_Rte in Rte_adding:
    #         List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(2).strip())
                            



    if "= Upda" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(Upda.+)\(\)|(= )(Upda.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
                            




    if "= Prs" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(Prs.+)\(\)|(= )(Prs.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
     

    if "= proce" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(proce.+)\(\)|(= )(proce.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
                            

    if "= checkR" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(checkR.+)\(\)|(= )(checkR.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(2).strip())
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
                            


    if "= DC_" in  Func_test_str:   #### TRY TO ADD THIS LINE CODE TO FIND WEATHER THE FUNCTION OR RTE OR CALLS IS THEIR OR NOT INT FUNCTION #####

        Rte_adding = re.finditer(r"(= )(DC_.+)\(\)|(= )(DC_.+)\(.+\)", Func_test_str, re.MULTILINE) #### THE REGEX IS USED TO FIND THE CALL NAME ####

        for Match_Rte in Rte_adding:
            List.List_EXPECT_CALL_Rte[index_fun].append(Match_Rte.group(4).strip())
        
                            









    #################################################################
        #       Add the code here for the remaining Calls           #
    #################################################################
    else: #### IFTHEIR IS NO RTE OR ANY CALLS JUST ADD THE Garbage ####
        Garbage = "THEIR IS NO RTE CALLS INSIDE THE FUNCTION"
        List.List_EXPECT_CALL_Rte[index_fun].append(Garbage)

