#!/usr/bin/python3

import sys 

if len(sys.argv) != 2:
    print(f'Usage {sys.argv[0]} <sddl_string>')
    sys.exit()


# All the different service ACL permissions
_permissions = {
    'CC': 'SERVICE_QUERY_CONFIG',
    'LC': 'SERVICE_QUERY_STATUS',
    'SW': 'SERVICE_ENUMERATE_DEPENDENTS',
    'LO': 'SERVICE_INTERROGATE',
    'RC': 'READ_CONTROL',
    'RP': 'SERVICE_START',
    'DT': 'SERVICE_PAUSE_CONTINUE',
    'CR': 'SERVICE_USER_DEFINED_CONTROL',
    'WD': 'WRITE_DAC',
    'WO': 'WRITE_OWNER',
    'WP': 'SERVICE_STOP',
    'DC': 'SERVICE_CHANGE_CONFIG',
    'SD': 'DELETE'
    }

# All the different ACL trustees 
_trustees = {
    'AA': 'Access Control Assistance Operators are',
    'AC': 'All Application running in an app package context are',
    'AN': 'Anonymous Logins are',
    'AO': 'Account Operatros are',
    'AP': 'Protected Users are',
    'AU': 'Authinticated Users are',
    'BA': 'Built-in Administrators are',
    'BG': 'Built-in Guests are',
    'BO': 'Backup Operators are',
    'BU': 'Built-in Users are',
    'CA': 'Certificate Publishers are',
    'CD': 'Users Who Can Connect to Certification Authorities Using DCOM are',
    'CG': 'The Creator Group is',
    'CN': 'Cloneable Domain Controllers are',
    'CO': 'The Creator Owner is',
    'CY': 'Cypto Operators are',
    'DA': 'Domain Administrators are',
    'DC': 'Domain Computers are',
    'DD': 'Domain Controllers are',
    'DG': 'Domain Guests are',
    'DU': 'Domain Users are',
    'EA': 'Enterprise Administrators are',
    'ED': 'Enterprise Domain Controllers are',
    'EK': 'Enterprise Key Admins are',
    'ER': 'Event Log Readers are',
    'ES': 'Endpoint Servers are',
    'HA': 'Hyper-V Administrators are',
    'HI': 'The High Integrety Level group is',
    'IS': 'Anonymous Internet Users are',
    'IU': 'Interactively Logged-on Users are',
    'KA': 'Domain Key Admins are',
    'LA': 'The Local Administrator is',
    'LG': 'Local Guests are',
    'LS': 'The Local Service Account is',
    'LU': 'Perfromance Log Users are',
    'LW': 'The Low Integrity Level group is',
    'ME': 'The Medium Integrity group is',
    'MP': 'The Medium Plus Integrity group is',
    'MU': 'Performance Monitor Users are',
    'NO': 'Network Configuration Operators are',
    'NS': 'The Network Service Account is',
    'NU': 'Network Logon Users are',
    'OW': 'The Owner Rights is',
    'PA': 'Group Policy Administrators are',
    'PO': 'Printer Operators are',
    'PS': 'Principal Self is',
    'PU': 'Power Users are',
    'RA': 'The RDS Remote Access Server group is',
    'RC': 'Restricted Code is',
    'RD': 'Terminal Server Users are',
    'RE': 'The Replicator is',
    'RM': 'The RMS service is',
    'RO': 'Enterprise Read-Only Domain Controllers are',
    'RS': 'The RAS Servers Group is',
    'RU': 'Pre Windows Server 2000 Applications are',
    'SA': 'Schema Administrators are',
    'SI': 'The System Integrity Level group is',
    'SO': 'Server Operators are',
    'SS': 'The Authintication Service Asserted group is',
    'SU': 'The Service Login User is',
    'SY': 'The Local System is',
    'UD': 'User-Mode Driver is',
    'WD': 'Everyone are',
    'WR': 'Write Restricted Code is'
    }

sddl = sys.argv[1]

# Check if the strings begins with 'D:' for DACL
if not sddl.startswith('D:'):
    print('\nThis is not a DACL string, it should start with "D:"')
    sys.exit()

# Identify any SACL in the input and remove them. We mainly care about the DACL portion
if 'S:' in sddl:
    sacl = sddl[sddl.find('S:'):]
    sddl = sddl[:sddl.find('S:')]
    
    print(f'\nPlease note that SACL\'s are not supported and thus "{sacl}"')
    print('has not been accounted for.')

# Split the DACL string into seperate, even entries.
entries = sddl.split(')(')
entries[0] = entries[0][3:]            # Clean up the first entry
entries[-1] = entries[-1][:-1]         # Clean up the last entry


for entry in entries:
    action = entry[0]
    if action == 'A':
        action = 'Allowed'
    else:
        action = 'Denied'

    trustee = entry.find(';;;') 
    
    perms = entry[3:trustee]
    perms = [perms[i:i + 2] for i in range(0, len(perms), 2)] # Split the permissions into sets of two characters

    trustee = entry[entry.rfind(';')+1:]
    
    if trustee.startswith('S-1-'):                    # Check if SID is in the Entry
        print(f'\n{trustee} is {action}:')
        for perm in perms:
            print(f'\t{_permissions[perm]}')
    else:
        print(f'\n{_trustees[trustee]} {action}:')
        for perm in perms:
            print(f'\t{_permissions[perm]}')

