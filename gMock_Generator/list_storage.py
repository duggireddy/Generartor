# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      list_storage.py
#  \brief
#      
#

class List:

    #### FUNCTIONS ####
    List_Func = [] 
    List_Func_Arg = []


    #### RTE ####
    List_Rte = [] 
    List_Rte_Arg = [] 


    #### LOG_FUNCTIONS ####
    List_Log_Func = [] 


    #### FROM HEADER FILES RTE ####
    List_Rte_Mock = [] 
    List_Rte_Mock_DT = [] 
    List_Rte_Mock_Arg = []  
    List_Rte_Mock_Method_Arg_RTE = []  
    List_Rte_Mock_Method_Arg_DT = [] 
    List_Rte_Mock_Method_Arg_Func = []  
    
    



class prt:
    ###################################################
    #                                                 #
    #       FROM Finding_all_function.py              #
    #                                                 #
    ###################################################
    def List_print():
        print('\n')
        #### FUNCTIONS ####
        print('#### FUNCTIONS ####')
        print(List.List_Func )
        print('\n')

        print('#### FUNCTIONS ARGUMENTS ####')
        print(List.List_Func_Arg)
        print('\n')


        ##### RTE ####
        print('#### RTE FUNCTIONS ####')
        print(List.List_Rte)
        print('\n')


        #### LOG FUNCTIONS ####
        print('#### LOG FUNCTIONS ####')
        print(List.List_Log_Func)
        print('\n')

        ###################################################
        #                                                 #
        #       FROM Fetching_all_API_data.py             #
        #                                                 #
        ################################################### 

        print('#### API DATA ####')
        print(List.List_Rte_Mock )


        print('\n')
        print(List.List_Rte_Mock_DT)
        print('\n')
        print(List.List_Rte_Mock_Arg) ######[['void'], ['void'], ['void'], ['void'], ['*data']]#######
        print('\n')
        print(List.List_Rte_Mock_Method_Arg_RTE)
        print('\n')

        #### THIS IS USED FOR GENERATING MOCKS METHODS ####
        print(List.List_Rte_Mock_Method_Arg_DT)
        print('\n')
        print(List.List_Rte_Mock_Method_Arg_Func)



