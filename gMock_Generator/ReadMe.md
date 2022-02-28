# How can one run the "gmock_main_generator.py" ? 

- Open cmd window from the folder \swc\tools\Common\gMock_Generator

- Adapt the paths in the "gmock_generator_config.json" as follows : 

| Key                      | Example Value                                                            | Description|
| :---                     |          :---                                                            |    :----:  |
| gmock_srcs               | "C:/Projects/HCP2/idc/swc/src/ASMH"                                      |  Sources under test for which we need to generate the gMock files |
| gmock_swc_func_proto_src | "C:/Projects/HCP2/idc/Header"                                            |  Path to the implementation template of the IDC from which the RTE function prototypes are being read out|
| gmock_jinja_template     | "C:/Projects/HCP2/idc/swc/tools/Common/gMock_Generator/Jinja2_Templates" |  Jinja templates that are rendered to generate the gMock files |
| gmock_output             | "C:/Projects/HCP2/idc/Mock_Methods"                                      |  gMock methods        |

- Make sure that you are using the Python-3. Note : This script has not been tested using Python-2.
- Execute the command : ```python gmock_main_generator.py``` to generate the gMock files for GoogleTest.