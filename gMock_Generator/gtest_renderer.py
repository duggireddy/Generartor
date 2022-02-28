# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      gtest_renderer.py
#  \brief
#      
#

import os
import re
from regexes import Find
from temp_file_utilities import FILES
from get_func_proto_from_impl_template import Rte_data
from list_storage import List
from list_storage import prt
from get_function_names_from_src_under_test import Func
import jinja2
from jinja2 import FileSystemLoader


###################################################
#                                                 #
#           LISTS ASSIGNING TO  JINJA             #
#                                                 #
###################################################


List1 =List.List_Rte_Mock_DT 
List2 = List.List_Rte
List3 = List.List_Rte_Mock
List4 = List.List_Rte_Mock_Method_Arg_DT
List5 = List.List_Rte_Mock_Method_Arg_RTE
List6 = List.List_Rte_Mock_Method_Arg_Func
List7 = List.List_Rte_Mock_Arg




class Mock_jinja:
    def Temp_jinja(Path_Jinja_Item,path_Gen_file, Jinja_file_name, Jinja_C_file ):
        
        template_dir = Path_Jinja_Item #### HERE DEFINE THE PATH OF JINJA TEMPLATE ####
        file_loader = FileSystemLoader(template_dir)
        env = jinja2.Environment(loader=file_loader)
        template = env.get_template(Jinja_file_name)
        len_list = range(len(List1))
        output = template.render(RTN = List1, RTE = List2 , Rte_Mock = List3, DT = List4, ARG_FUNC = List5 ,ARG_RTE = List6,Rte_Mock_Arg = List7 )
        print (output) 
        with open(path_Gen_file +'/'+ Jinja_C_file, 'a') as f:
            f.write(output)



   
