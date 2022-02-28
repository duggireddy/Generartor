# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#     get_function_names_from_src_under_test.py
#  \brief
#      
#

import os
import re
from regexes import Find
from temp_file_utilities import FILES
from get_func_proto_from_impl_template import Rte_data
from list_storage import List


files = os.listdir()
class Func:
    
    def Func(path,Gen_path):
        # CREATING THE FILES TO GENERATE THE DATA (PLZ FIND THE temp_file_utilities.py file for code )
        FILES.FILES_CLR(Gen_path)

        # current directory where the files are generated
        print('The Generated files in the path ', os.getcwd())
        
        files = os.listdir(path)
        for File_Name in files:

            print("\n")

            print("The file name is " + File_Name)  # file name

            Code = open(path+'/'+File_Name, 'r')  # reading the all files using the for loop

            test_str = Code.read()

            # Regex for the finding  the all function
            Matches_Find_functions = re.finditer(Find.Functions, test_str, re.MULTILINE)

            # Regex for the finding the all Rte call functions
            Matches_Find_Rte = re.finditer(Find.Rte, test_str, re.MULTILINE)
            

            # Regex for the finding  the all LogFunctions
            Matches_Find_Log = re.finditer(Find.Log, test_str, re.MULTILINE)

            # This is for the finding Get calls
            Matches_Find_Get = re.finditer(Find.Get, test_str, re.MULTILINE)


            # This is for the finding functions

            for Match_Func in Matches_Find_functions:
                List.List_Func.append(Match_Func.group().strip())

                with open(Gen_path+'/'+'Functions.txt', 'a') as f:
                    f.write(Match_Func.group() + '\n')

                # Finding Arguments in the Functions
                Arguments_in_function = re.finditer(Find.Arguments, Match_Func.group(), re.MULTILINE)

                for i in Arguments_in_function:
                    #### r"[^\(].+[^\)]" THIS REGEX IS USED TO SEPERATE THE ARGUMENTS FROM THE FUNCTION #### 
                    Rearranging_the_Arguments = re.finditer(r"[^\(].+[^\)]", i.group(), re.MULTILINE)
                    for Match_Func_Arg in Rearranging_the_Arguments:
                        List.List_Func_Arg.append(Match_Func_Arg.group().strip())
                        with open(Gen_path+'/'+'Function_arguments.txt', 'a') as file_1:
                            file_1.write(Match_Func_Arg.group() + '\n')


            # This is for the finding Rte calls
            
            for match in Matches_Find_Rte:
                Rte_adding = re.finditer(Find.Edit_Rte, match.group(), re.MULTILINE)
                for Rte_Func in Rte_adding:
                    Rte_Func_adding = re.finditer(Find.Rte_Func, Rte_Func.group(), re.MULTILINE)
                    for Rte_edit_fun in Rte_Func_adding:
                        Rte_Func_adding = re.finditer(Find.Func_edit, Rte_edit_fun.group(), re.MULTILINE)
                        for Match_Rte in Rte_Func_adding:
                            List.List_Rte.append(Match_Rte.group().strip())
                            with open(Gen_path+'/'+'Rte_Function_Names.txt', 'a') as file_2:
                                # Adding all RTE calls in the RTE file
                                file_2.write(Match_Rte.group().strip() + '\n')


            # This is for the finding Get calls
            
            for match in Matches_Find_Get:
                Rte_adding = re.finditer(Find.Edit_Get, match.group(), re.MULTILINE)
                for Rte_Func in Rte_adding:
                    Rte_Func_adding = re.finditer(Find.Rte_Func, Rte_Func.group(), re.MULTILINE)
                    for Rte_edit_fun in Rte_Func_adding:
                        Rte_Func_adding = re.finditer(Find.Func_edit, Rte_edit_fun.group(), re.MULTILINE)
                        for Match_Rte in Rte_Func_adding:
                            List.List_Rte.append(Match_Rte.group().strip())
                            with open(Gen_path+'/'+'Rte_Function_Names.txt', 'a') as file_2:
                                # Adding all RTE calls in the RTE file
                                file_2.write(Match_Rte.group().strip() + '\n')




        # This is for the finding the Log functions
            for Match_Log in Matches_Find_Log:
                List.List_Log_Func.append(Match_Log.group().strip())
                with open(Gen_path+'/'+'LogFunctions.txt', 'a') as file_3:
                    file_3.write(Match_Log.group().strip() + '\n')

                # close the file once
            Code.close()
