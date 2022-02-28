import os
import re
from regexes import Find
import itertools
from list_storage import List
from get_args_from_func_proto import Call_Arguments

#######################################################################################
#      THIS FUNCTION IS USED TO GENERATE  DATA TYPES , ARGUMENTS WRT TO CALLS         #
#######################################################################################

class Rte_data:
    
    def Rte_Data_Gen(path):
        j=0

        for List_of_List in List.List_EXPECT_CALL_Rte: #### LIST[LIST] CALLS WE ARE READING TO FIND THE ALL RETURN TYPE AND ETC ####

            index_RTE_List = List.List_EXPECT_CALL_Rte.index(List_of_List)  #### THIS INDEX WE ARE USING TO STORE THE ALL DATA WRT TO THE LIST ####


            ###############################################################################
            #            HERE WE ARE CREATING NESTED LIST WRT TO THE EACH RUNNABLE        #
            ###############################################################################

            List.List_EXPECT_CALL_Return_P_NP.append([])  #### STORING POINTER AND NON POINTER RETURN TYPE ####

            List.List_EXPECT_CALL_Rte_DT.append([])   #### STORING CALLS DATA TYPE ####

            List.List_Call_Arg.append([])   #### STORING THE ARGUMENTS #####

            List.List_Call_Arg_Ptr.append([])   #### STORING THE pointer ARGUMENTS VARIABLE WITH CALL #####

            List.List_Call_Arg_Var.append([])  ##### STORING THE POINTER ARGUMENT ####
            

            for List_EXPECT_CALL in List_of_List: #### FROM HERE WE STARTED THE READING CALL [list] ONE BY ONE WHICH IS IN THE LIST[list] ####

                var = List_EXPECT_CALL.strip()  ##### Storing in a variable and pass to regex for finding in API ####

                ##### IF ITS NOT A CALL THEN SKIP THAT PART #####

                if 'THEIR IS NO RTE CALLS INSIDE THE FUNCTION' == var:
                    List.List_EXPECT_CALL_Return_P_NP[index_RTE_List].append('N_A_T')  ##### "N_A_T" = NO ARGUMENT TYPE FOR THE CALL #### 
                    List.List_EXPECT_CALL_Rte_DT[index_RTE_List].append("N_DT_IN_FILE_CALL")  #### "N_DT_IN_FILE_CALL" = NO DATA TYPE FOR THE CALL ####

                else:
                
                    New_files = os.listdir(path)

                    for File_Name in New_files: #### READING THE FILES TO CHECK THE HEADER FOR THE CALLS ####
                        
                        Code = open(path+'/'+File_Name, 'r')  # reading the all files using the for loop
                        test_str = Code.read()

                        
                        if var in test_str:
                        
                            Matched_API = re.finditer(rf"\*.+{var}.+|.+{var}.+", test_str, re.MULTILINE) ##### THIS REGEX IS USED TO MATCH THE EXACT API LINE, THE CONTAIN THE CALL #####

                            #### IF WE FING THE MATCH DATA EXIT FROM THE LOOP #### 

                            for Match_API in Matched_API:

                                Head = Match_API.group()
                                                                                                                    
                                if List_EXPECT_CALL in Head:
                                
                                    Arguments_in_RTE_function = re.finditer(r" [^[^*].+\)|^[a-zA-Z0-9_].+", Head, re.MULTILINE)
                                    
                                    for i in Arguments_in_RTE_function:

                                        #### HERE WE ARE TAKING CALL WITH DATA TYPE AND ARGUMENTS ####
                                        ### Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn(void) ####

                                        Exact_Head = i.group().strip()
                                        List.List_Rte_Mock.append(i.group().strip())
                                        test_str = Exact_Head

                                        regex_H_RTE = r"(.+)\(" ###### THIS REGEX IS USED TO FIND THE CALLS NAME, WHICH IS INTHE HEADER FILE #### 
                                        matches = re.finditer(regex_H_RTE, test_str, re.MULTILINE)
                                        Array = []
                                        for matchNum, match in enumerate(matches, start=1):

                                            #### DEFERATING DATA TYPE AND RTE FROM THE HEADER ####
                                            
                                            for groupNum in range(0, len(match.groups())):
                                                groupNum = groupNum + 1
                                                store = "{group}".format(group = match.group(groupNum))
                                                Array = store 
                                                ################################################################################################
                                                #           FINDING POINTER DATA  TYPE TYPE AND NON-POINTER DATATYPE AND ADDING TO LIST        #
                                                ################################################################################################

                                                ##### FINDING POINTER DATA  TYPE TYPE AND NON-POINTER DATATYPE AND ADDING TO LIST #####
                                                ##### WEATHER THE CALL SHOULD RETURN THE POINTER TYPE OR NOT, ITS IT CONTAIN " * " THEN WE ARE ADDING "&" TO THE LIST WRT TO THAT CALL ##### 
                                                ### Dt_RECORD_EthDAFIn *Rte_IRead_RCtCdIDCMain_PpEthDAFIn_DeEthDAFIn ####

                                                if ' *' in test_str:
                                                    List.List_EXPECT_CALL_Return_P_NP[index_RTE_List].append('&')

                                                else:
                                                    List.List_EXPECT_CALL_Return_P_NP[index_RTE_List].append('N_A_T')

                                                ###################################################
                                                #           FINDING ARGUMENTS INSIDE THE CALL     #
                                                ###################################################

                                                Call_Arguments(test_str,index_RTE_List)

                                                ###################################################
                                                #           FINDING DATA TYPES FOR THE CALLL      #
                                                ###################################################

                                                ##### THIS IS FOR COLLECTING THE DATA TYPES RELATED TO THE CALLS ####

                                                RTE_Mock_DT2 = r"(.+) ([a-zA-Z0-9_*]+$)" #### THIS REGEX IS USED TO FIND THE DATA TYPES THAT RELATED TO THE CALLS #####
                                                matches_find_API_DT = re.finditer(RTE_Mock_DT2, Array, re.MULTILINE)
                                                for match in matches_find_API_DT:
                                                    DT = match.group(1)
                                                    List.List_Rte_Mock_DT.append(DT.strip())

                                                    List.List_EXPECT_CALL_Rte_DT[index_RTE_List].append(DT.strip())

                                else:
                                    List.List_EXPECT_CALL_Rte_DT[index_RTE_List].append("N_DT_IN_FILE_CALL")  
                                    List.List_EXPECT_CALL_Return_P_NP[index_RTE_List].append('N_RTN_IN_FILE_CALLL') 
                                