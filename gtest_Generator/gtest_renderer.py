import os
import re
from list_storage import List
from list_storage import prt
import jinja2
from jinja2 import FileSystemLoader

###################################################
#           LISTS ASSIGNING TO  JINJA             #
###################################################


List1 = List.List_Func
List2 = List.List_EXPECT_CALL_Rte
List3 = List.List_EXPECT_CALL_Rte_DT
List4 = List.List_EXPECT_CALL_Return_P_NP
List5 = List.List_Name_Func
List6 = List.List_Call_Arg_Ptr
List7 = List.List_Call_Arg
List8 = List.List_Call_Arg_Var

class Unit_Test:

    def G_Test(template_dir,path_Gen_file,File_Name ):

        file_loader = FileSystemLoader(template_dir) #### HERE DEFINE THE PATH OF JINJA TEMPLATE ####
        env = jinja2.Environment(loader=file_loader)
                 
        with open(path_Gen_file+'/'+File_Name, 'w') as f:
            pass
        template = env.get_template("gtest_template.jinja2")
        output = template.render(fun_list = List1, Rte_list = List2,Data_Types = List3, pt = List4,Function_Name = List5, Call_Arg_Ptr = List6, Call_Arg = List7, Arg_Var = List8)
        print (output) 
        with open(path_Gen_file+'/'+File_Name, 'a') as f:
            f.write(output)







