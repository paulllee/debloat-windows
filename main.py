# Program: Debloat Windows 11 - Specific to HP Devices but Works on All Windows Devices
# Author: Paul Lee (https://github.com/paulllee)
# Date: July 10th, 2022

import os, ctypes, sys

def run(command):
    fullCommand = 'powershell.exe "{}"'.format(command)
    print("\nrunning:", fullCommand)
    return os.system(fullCommand)

def uninstall(applicationName):
    return run('winget uninstall \'{}\''.format(applicationName))

isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
if (not isAdmin):
    print('Please run terminal as administrator to start the script.')
    sys.exit()

print('Welcome to Debloating Windows!')

apps = [
    'Netflix', 
    'Amazon Alexa',
    'McAfee® Personal Security',
    'HP Impreza Pen',
    'Dropbox promotion',
    'Disney+',
    'HP_Documentation',
    'MSC',
    'Cortana',
    'Microsoft News',
    'MSN Weather',
    'Xbox',
    'Get Help',
    'Microsoft Tips',
    'Paint 3D',
    'Office',
    'Microsoft Solitaire Collection',
    'Microsoft Sticky Notes',
    'Mixed Reality Portal',
    'OneNote for Windows 10',
    'Microsoft OneDrive',
    'OneDrive',
    'Paint',
    'Microsoft People',
    'Power Automate',
    'Print 3D',
    'Skype',
    'Microsoft To Do',
    'Windows Clock',
    'Windows Calculator',
    'Feedback Hub',
    'Windows Maps',
    'Xbox TCUI',
    'Xbox Console Companion',
    'Xbox Game Bar Plugin',
    'Xbox Game Bar',
    'Xbox Identity Provider',
    'Xbox Game Speech Window',
    'Your Phone',
    'Windows Media Player',
    'Movies & TV',
    'Microsoft Teams',
    'Microsoft Office 365 - en-us',
    'Mail and Calendar',
    'ExpressVPN',
    'EzTiltPen',
    'OMEN Gaming Hub',
    'News',
    'Logi Bolt',
    'Groove Music',
    'Phone Link',
    'Microsoft 365 - en-us',
    'Microsoft OneNote - en-us',
    'Concepts',
    'WebAdvisor by McAfee'
]

isFinish = False
while not isFinish:
    print('\nThis is the list of apps that we will uninstall:')

    for num, name in enumerate(apps):
        print('{}. {}'.format(num + 1, name))

    userInput = input('\nType in the number next to the app you want to keep (type "finish" to continue): ').lower()
    
    if userInput == 'finish':
        isFinish = True
    else:
        try:
            apps.pop(int(userInput) - 1)
        except:
            print('Invalid number.')

for name in apps:
    uninstall(name)

if 'Xbox Game Bar' in apps:
    print("Fixing no Xbox Game Bar pop up.")
    run('REG ADD \'HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR\' /v AppCaptureEnabled /t REG_DWORD /d 0 /f')

if 'OneDrive' and 'Microsoft OneDrive' in apps:
    print('Changing OneDrive paths to local paths. Move files if there are any after reboot.')
    
    # My Pictures
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'{0DDD015D-B06C-45D5-8C4C-F59713854639}\' -Value \'%USERPROFILE%\\Pictures\' -Force')
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'{3B193882-D3AD-4EAB-965A-69829D1FB59F}\' -Value \'%USERPROFILE%\\Pictures\\Saved Pictures\' -Force')
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'{69D2CF90-FC33-4FB7-9A0C-EBB0F0FCB43C}\' -Value \'%USERPROFILE%\\Pictures\\Slide Shows\' -Force')
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'{B7BEDE81-DF94-4682-A7D8-57A52620B86F}\' -Value \'%USERPROFILE%\\Pictures\\Screenshots\' -Force')
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'My Pictures\' -Value \'%USERPROFILE%\\Pictures\' -Force')

    # Documents
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'{F42EE2D3-909F-4907-8871-4C22FC0BF756}\' -Value \'%USERPROFILE%\\Documents\' -Force')
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'Personal\' -Value \'%USERPROFILE%\\Documents\' -Force')

    # Desktop
    run('Set-ItemProperty -Path \'HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders\' -Name \'Desktop\' -Value \'%USERPROFILE%\\Desktop\' -Force')