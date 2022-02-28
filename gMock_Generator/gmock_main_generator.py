# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      gmock_main_generator​.py
#  \brief
#      Main function for the gMock Generator
#


###################################################
#                                                 #
#           Import Library                        #
#                                                 #
###################################################
import os
import re
import json
from regexes import Find
from temp_file_utilities import FILES
from temp_file_utilities import Del_All
from temp_file_utilities import Del
from get_func_proto_from_impl_template import Rte_data
from list_storage import List
from list_storage import prt
from get_function_names_from_src_under_test import Func
from gtest_renderer import Mock_jinja

def print_start_message():
    print("*"*70)
    print("*"*70)
    print("Intelligent Data Collector SWC gMock Generator start")
    print("*"*70)
    print("*"*70)

def print_end_message():
    print("*"*70)
    print("*"*70)
    print("Intelligent Data Collector SWC gMock Generator end")
    print("*"*70)
    print("*"*70)

def path(config):
    path.gmock_srcs = config["gmock_srcs"] ### Path to the source files under test ###    
    path.gmock_swc_func_proto_src = config["gmock_swc_func_proto_src"]  ### Path to the IDC implementation template from which the function prototypes are read out###
    path.gmock_jinja_template = config["gmock_jinja_template"] ### Path to the jinja templates used for rendering ###
    path.gmock_output = config["gmock_output"]  ### gMock generator output path ###

def main():
    print_start_message()
    
    f = open('gmock_generator_config.json')
    config = json.load(f)
    
    path(config) #SetPaths 

    Del_All.Files_Del_All(path.gmock_output) # Clear all files from directory

    Func.Func(path.gmock_srcs, path.gmock_output) #Generate RTE calls, function names, log functions etc.

    Rte_data.Rte_Data_Gen(path.gmock_swc_func_proto_src,path.gmock_output) #Generate function names, datatypes, function arguments and mocking RTE, Get, etc. functions

    # Render JINJA templates for mock files
    Mock_jinja.Temp_jinja(path.gmock_jinja_template,path.gmock_output,"gmock_class_template.jinja2", 'Mock_Class.h')
    Mock_jinja.Temp_jinja(path.gmock_jinja_template,path.gmock_output, "gmock_function_template.jinja2", 'Mock_function.h')

    Del.Files_Del(path.gmock_output) #Clean-up all unnecesary files

    print_end_message()


if __name__ == "__main__":
    main()