#                             |----=== Sos1ska ===----|                                                                               #
# |----=== https://vk.com/nikitasos1ska <----> https://github.com/Sos1ska ===----                                                     #

# |----=== Code: CreaterNotificationForWindows ===----                                                #
#  ----=== Link Code: https://github.com/Sos1ska/CreaterNotificationForWindows ===----|               #

vbOKOnly = "vbOKOnly"
vbOKCancel = "vbOKCancel"
vbAbortRetryIgnore = "vbAbortRetryIgnore"
vbYesNoCancel = "vbYesNoCancel"
vbYesNo = "vbYesNo"
vbRetryCancel = "vbRetryCance"
vbCritical = "vbCritical"
vbQuestion = "vbQuestion"
vbExclamation = "vbExclamation"
vbInformation = "vbInformation"
vbDefaultButton1 = "vbDefaultButton1"
vbDefaultButton2 = "vbDefaultButton2"
vbDefaultButton3 = "vbDefaultButton3"
vbDefaultButton4 = "vbDefaultButton4"
vbApplicationModal = "vbApplicationModal"
vbSystemModal = "vbSystemModal"
vbMsgBoxHelpButton = "vbMsgBoxHelpButton"
vbMsgBoxSetForeground = "vbMsgBoxSetForeground"
vbMsgBoxRight = "vbMsgBoxRight"
vbMsgBoxRtlReading = "vbMsgBoxRtlReading"

from .Form import FORM_CREATE_VBS

class MainCode_CreaterNotificationForWindows():
    def Help(self):
        print('''
Argument: Text
    This argument passes text in any format to your msg
Argument: Title
    This argument passes the header in any format to your msg
Argument: ParametersMSG
    This argument passes the form msg, more on off. website https://docs.microsoft.com/ru-ru/office/vba/language/reference/user-interface-help/msgbox-function
                OR
    Open source file ListParametersMSG.py
Argument: Buffer 'Default False' 
    This argument creates a folder called Buffer, this folder will contain the source codes for running msg
    
    The True argument generates the source code to run and then removes it
''')
    def CreateNotification(self, Text, Title, ParametersMSG, Buffer = False):
        if Buffer == False:
            pass
        #elif Buffer == True:
        #    import os
        #    import random
        #    import subprocess
        #    dir = os.path.abspath(os.curdir)
        #    name_file = random.randint(0, 2147483600)
        #    try:
        #        os.mkdir(f'{dir}\\Buffer')
        #    except:
        #        pass
        #    file = open(f'{dir}\\Buffer\\{name_file}.vbs', 'w', encoding='UTF-16 LE')
        #    file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
        #    file.close()
        #    subprocess.call(f'cscript {dir}\\Buffer\\{name_file}.vbs')
        else:
            pass   
        import random
        import os
        import subprocess
        dir = os.path.abspath(os.curdir)
        name_file = random.randint(0, 2147483600)
        file = open(f'{dir}\\{name_file}.vbs', 'w', encoding='UTF-16 LE')
        file.write(FORM_CREATE_VBS(f'{Text}', f'{Title}', f'{ParametersMSG}'))
        file.close()
        subprocess.call(f'cscript {dir}\\{name_file}.vbs')
        os.remove(f'{dir}\\{name_file}.vbs')