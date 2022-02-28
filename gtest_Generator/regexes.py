class Find:
    #########################
    #                       #
    #  REGULAR EXPRESSIONS  #
    #                       #
    #########################  
           
    #### Regular Expression for finding the all Functions with Arguments 
    Functions = r"(^[a-zA-Z0-9_]+\s+[a-zA-Z0-9_ ]+\(.+\))|(^[a-zA-Z0-9_]+\s+[a-zA-Z0-9_ ]+\(\))" 

    #### Regular Expression for finding the all Rte Functions with Arguments 
    Rte = r"\= Rte_.+\)"

  
    #### Regular Expression for finding the all Functions with Arguments 
    Log = r" Log.+\)"

    #### Regular Expression for finding the all Rte Functions after editing with Arguments 
    Edit_Rte = r"Rte_.+\)"

    #### Regular Expression for finding the all  Arguments 
    Arguments = r"\(.+\)"

    #### Regular Expression for the RTE_MOCK
    Mock_RTE = r".*Rte.+"

    ############ Regular Expression for finding the all RTE data types for the Mock files 
    RTE_Mock_DT = r"[ \t\r\n\f][ ][a-zA-Z0-9_]+"

    ##### Regular Expression for finding the RTE function Names
    Rte_Func = r".+\("
    Func_edit = r".+[^(]"

    Get = r"= Get.+"
    Edit_Get = r"Get_.+\)"

    ##################################################################################
    #            FINDING THE FUNCTIONS INSIDE THE FUNCTIONS AND STORE IN LIST        #
    ##################################################################################   