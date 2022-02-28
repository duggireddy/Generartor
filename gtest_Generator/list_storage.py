class List:

    #### FUNCTIONS ####
    List_Func = [] 
    List_Name_Func = [] 
    List_Str = []


    #### RTE ####
    List_G_Rte = [] 
    List_Rte_Arg = [] 



    #### FROM HEADER FILES RTE ####
    List_Rte_Mock = [] 
    List_Rte_Mock_DT = [] 
    List_Rte_Mock_Arg = []  
    List_Rte_Mock_Method_Arg_RTE = []  
    List_Rte_Mock_Method_Arg_DT = [] 
    List_Rte_Mock_Method_Arg_Func = []  


    #### EXPECT_CALL ####
    List_EXPECT_CALL_Rte = []
    List_EXPECT_CALL_DT = []
    List_EXPECT_CALL_Return_P_NP = []
    List_EXPECT_CALL_Rte_DT = []



    #### EXPECT_CALL ####
    List_Call_Arg = [] ###### STORING ARGUMENTS #####

    List_Call_Arg_Ptr = [] #### STORING CALL + VARIABLE ####

    List_Call_Arg_Var = []


    





class prt:
    ###################################################
    #                                                 #
    #       FROM Finding_all_function.py              #
    #                                                 #
    ###################################################
    def List_print():
        print('\n')


        print('\n')
        print(List.List_Rte_Mock_DT)
        print('\n')
        print(List.List_EXPECT_CALL_DT)

##########################################################################
#                                                                        #                                                              
#      CREATING THE FILES AND ERASE THE DATA INSIDE THE ALL FOLDERS      #
#                                                                        #                                                               
##########################################################################

class Del_All:
    def Files_Del_All():
        mydir = 'C:\HCP2_IDC\Mock_Methods'
        for f in os.listdir(mydir):
            os.remove(os.path.join(mydir, f))

