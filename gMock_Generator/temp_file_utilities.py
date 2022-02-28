# *******************************************************************************
#   Copyright (C) 2014 TTTech Automotive GmbH. All rights reserved              *
#   Schoenbrunnerstrasse 7, A-1040 Wien, Austria. office\tttech-automotive.com  *
# ******************************************************************************/
#
#  \file
#      temp_file_utilities.py
#  \brief
#      
#

import os

##########################################################################
#                                                                        #                                                              
#      CREATING THE FILES AND ERASE THE DATA INSIDE THE ALL FOLDERS      #
#                                                                        #                                                               
##########################################################################

#### CLEARING ALL FILES IN SIDE THE FOLDER BEFORE GENERATING THE MOCK CLASS, MOCK RTE ####
class Del_All:
    def Files_Del_All(path_Gen_file):
        mydir = path_Gen_file
        for f in os.listdir(mydir):
            os.remove(os.path.join(mydir, f))


##### CREATING FILES AND CLEAR THE DATA IN SIDE THE FILE TO STORE THE DATA WHICH IS REQUIRED TO GENERATE ####
class FILES:
    def FILES_CLR(path_Gen_file):
        ## Note: Initialy ERASE the data inside the all folders
        with open(path_Gen_file +'/'+'Function_arguments.txt', 'w') as Function_arguments:
            pass
        with open(path_Gen_file + '/' +'Functions.txt', 'w') as Functions:
            pass
        with open(path_Gen_file + '/' +'LogFunctions.txt', 'w') as LogFunctions:
            pass
        with open(path_Gen_file + '/' +'Rte_Function_Names.txt', 'w') as Rte_Function_Names:
            pass
        with open(path_Gen_file + '/' +'Mock_Classes.h', 'w') as Mock_Classes:
            pass


##############################################################
#      DELETING THE FILES EXCEPT MOCK AND MOCK_CLASSES       #                                                               
##############################################################


class Del:
    def Files_Del(path_Gen_file):
        mydir = path_Gen_file
        for f in os.listdir(mydir):
            if not f.endswith(".txt"):
                continue
            os.remove(os.path.join(mydir, f))
