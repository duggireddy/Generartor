
import os
import re
import json
import sys
from regexes import Find
from list_storage import List
from get_func_proto_from_impl_template import Rte_data
from list_storage import prt
from get_function_body import Fun_St_Ed
from gtest_renderer import Unit_Test
from function_names import Fun_Name_Gen
sys.setrecursionlimit(100000)


def print_start_message():
    print("*"*70)
    print("*"*70)
    print("Intelligent Data Collector SWC gtest Generator start")
    print("*"*70)
    print("*"*70)

def print_end_message():
    print("*"*70)
    print("*"*70)
    print("Intelligent Data Collector SWC gtest Generator end")
    print("*"*70)
    print("*"*70)

def path(config):
    path.gtest_srcs = config["gtest_srcs"] ### Path to the source files under test ###    
    path.gtest_swc_func_proto_src = config["gtest_swc_func_proto_src"]  ### Path to the IDC implementation template from which the function prototypes are read out###
    path.gtest_jinja_template = config["gtest_jinja_template"] ### Path to the jinja templates used for rendering ###
    path.gtest_output = config["gtest_output"]  ### gMock generator output path ###     

def main():
    print_start_message()
    
    f = open('gmock_generator_config.json')
    config = json.load(f)
    
    path(config) #SetPaths 

    Fun_Name_Gen(path.gtest_srcs) # THIS FUNCTION  IS USED TO FIND THE ALL FUNCTIONS IN A FILE AND STORED IN  FunctionInFunc.txt          #

    Fun_St_Ed.Find_str_End(path.gtest_srcs) # THIS IS USED TO GENERATE THE CALL INSIDE THE FUNCTIONS AND FUNCTION IN FUNCTIONS AND ETC.....  

    Rte_data.Rte_Data_Gen(path.gtest_swc_func_proto_src)    # THIS IS USED TO GENERATE FUNCTIONS NAMES, DATA TYPES , ARGUMENTS  FOR MOCK RTE(check the code in Fetching_all_API_data.py)

    Unit_Test.G_Test(path.gtest_jinja_template,path.gtest_output, "gtest.cpp") # THIS IS USED TO GENERATE THE UNIT TEST CASES     

    print_end_message()



if __name__ == "__main__":
    main()

