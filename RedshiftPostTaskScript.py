import re
import os



def get_envVar():
    for env_variable in os.environ:
        if env_variable.startswith("REDSHIFT_LICENSE"):
            variable_name = env_variable
    return variable_name

var_name = get_envVar()

cwd = os.getcwd()
script_dit = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dit, 'doc.txt')

license_var = os.environ.get(var_name)

def __main__(*args):

    with open(path, 'r') as file:
        text = file.read()

    ip_count_dict = {}
    
    # Regex pattern to match IP
    pattern = r'(\d+\.\d+\.\d+\.\d+) : (\d+)'
    matches = re.findall(pattern, text)
    
    # Loops through and increases count by 1    
    for ip, count_str in matches:
        count = int(count_str)
        if ip == license_var:
            count += 1
        ip_count_dict[ip] = count
    
    # Replace the IP address-count pairs
    for ip, count in ip_count_dict.items():
        text = text.replace('{} : {}'.format(ip, count - 1), '{} : {}'.format(ip, count))
    # import scrldoup
    # Write the updated text back to the .txt file
    with open(path, 'w') as file:
        file.write(text)
    os.system("setx /M /D %s" % var_name)

# Call the function to increase the count of the specified IP address in doc.txt
if __name__ == "__main__":
    __main__()