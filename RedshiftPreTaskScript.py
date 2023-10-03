import re
import os
import pyuac
import ctypes

def get_envVar():
    variable_name = str
    for env_variable in os.environ:
        if env_variable.startswith("VARIABLE_NAME"):
            variable_name = env_variable
    return variable_name

var_name = get_envVar()

cwd = os.getcwd()
script_dit = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dit, 'doc.txt')

def __main__(*args):
    # Read the contents of the .txt file
    with open(path, 'r') as file:
        text = file.read()

    decreased_ip = None
    ip_count_dict = {}

    # Regex pattern to match IP addresses with counts
    pattern = r'(\d+\.\d+\.\d+\.\d+) : (\d+)'
    # Find all IP
    matches = re.findall(pattern, text)

    # Loop through the matches to find the first one with count > 0
    for ip, count_str in matches:
        count = int(count_str)
        if count > 0:
            count -= 1
            ip_count_dict[ip] = count
            decreased_ip = ip
            break  # Exit after the first match

    for ip, count in ip_count_dict.items():
        text = text.replace('{} : {}'.format(ip, count + 1), '{} : {}'.format(ip, count))
    # writing back to the file to keep count of available servers
    with open(path, 'w') as file:
        file.write(text)

    

    os.system("setx /M %s %s" % (var_name, decreased_ip))

    print(decreased_ip)
    return decreased_ip

    
if __name__ == "__main__":
    if not pyuac.IsUserAdmin():
        print('launching and admin...')
        pyuac.runAsAdmin()
    else:
        __main__(path)
        if __main__(path):
            print('Sucessfully switched IP')