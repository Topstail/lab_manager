import paramiko
from paramiko.client import SSHClient
from .models import Host
from concurrent.futures import ThreadPoolExecutor

def get_ssh_client(remote_ip, 
    remote_port, 
    remote_username, 
    remote_password):

    sshclient = paramiko.SSHClient()
    sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    sshclient.connect(hostname=remote_ip, port=remote_port, username=remote_username,password=remote_password)
    return sshclient

def execute_command(sshclient:SSHClient, cmd):
    stdin, stdout, stderr = sshclient.exec_command(cmd)
    stdout.channel.set_combine_stderr(True)
    output = stdout.read().decode("utf-8")
    return output.strip()
    
def close_ssh_client(sshclient:SSHClient):
    sshclient.close()

def generate_host_data(host:Host, ip, 
    port, 
    username, 
    password):


    HOSTNAME_CMD = '''hostname'''
    CPU_NAME_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f1 | sed 's/\$//g' '''
    CPU_BASE_CLOCK_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f2'''
    DISK_LIST_CMD = '''lsblk | egrep -e "^sd|^nvme" | awk '{print $1,$4}' '''
    OS_CMD = ''' grep -i "PRETTY_NAME" /etc/os-release | cut -d'"' -f2 '''
    BIOS_VERSION_CMD = ''' dmidecode -t bios | grep -i "version" | awk '{print $2}' '''
    MEMORY_CMD = ''' dmidecode -t memory | grep -P -A5 "Memory\s+Device" | grep Size | grep -v Range  | grep -v "No" | awk '{if($3=="MB" && ($2/1024)%1==0) sum+=$2/1024;else if($3=="GB")sum+=$2}END{print sum"GB"}' '''
    MEMORY_DETAIL_CMD = '''  dmidecode -t memory | grep -P -A16 "Memory\s+Device" | grep -v Range | grep -e "Size" -e "Speed" |  awk '{if(NR%2==1)printf $2 $3 "\t";else print $2 $3}' '''

    ssh = get_ssh_client(ip, port, username, password)

    host.ip = ip
    host.port = port
    host.username = username
    host.password = password
    cmd_dict = {'hostname':HOSTNAME_CMD, 
                'cpu_name':CPU_NAME_CMD,
                'cpu_base_clock':CPU_BASE_CLOCK_CMD,
                'disk':DISK_LIST_CMD,
                'os':OS_CMD,
                'bios_version':BIOS_VERSION_CMD,
                'memory':MEMORY_CMD,
                'memory_detail':MEMORY_DETAIL_CMD}
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {name: executor.submit(
            execute_command, ssh, command) for name, command in cmd_dict.items()}
        host.hostname = futures['hostname'].result()
        host.cpu_name = futures['cpu_name'].result()
        host.cpu_base_clock = futures['cpu_base_clock'].result()
        host.disk = futures['disk'].result()
        host.os = futures['os'].result()
        host.bios_version = futures['bios_version'].result()
        host.memory = futures['memory'].result()
        host.memory_detail = futures['memory_detail'].result()

    ssh.close()
    return host

