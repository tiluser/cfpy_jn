'''
    Program     : AppSpecBuildDefs.py
    Author      : Joseph M. O'Connor
    Purpose     : Builds the primitives defined in AppSpec.py and any high-level
                  definitions defined in the APPSPEC vocabulary. 
'''

from CreoleForth import cfb1

cfb1.buildPrimitive("TEST", cfb1.Modules.AppSpec.doTest, "AppSpec.doTest", "APPSPEC", "COMPINPF","( -- ) Testing definition - put whatever you want here")
# cfb1.buildPrimitive("TEST2", cfb1.Modules.AppSpec.doTest2, "AppSpec.doTest2", "APPSPEC", "COMPINPF","( -- ) Yet another testing def")