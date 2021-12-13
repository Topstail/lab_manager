import paramiko
from paramiko.client import SSHClient
from .models import Host

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

def generate_host_data(ip, 
    port, 
    username, 
    password):


    HOSTNAME_CMD = '''hostname'''
    CPU_NAME_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f1'''
    CPU_BASE_CLOCK_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f2'''
    DISK_LIST_CMD = '''lsblk | egrep -e "^sd|^nvme" | awk '{print $1,$4}' '''
    OS_CMD = ''' grep -i "PRETTY_NAME" /etc/os-release | cut -d'"' -f2 '''
    BIOS_VERSION_CMD = ''' dmidecode -t bios | grep -i "version" | awk '{print $2}' '''
    MEMORY_CMD = ''' dmidecode -t memory | grep  Size: | grep -v "No Module Installed" | awk '{sum+=$2}END{print sum"GB"}' '''
    MEMORY_DETAIL_CMD = ''' dmidecode -t memory | grep -e "Size:" -e  "Speed:" | grep -v "No Module Installed" | grep  -v "Configured Memory Speed" | awk '{if(NR%2==1) printf $2 $3 " " ;else print $2 $3 }' '''

    ssh = get_ssh_client(ip, port, username, password)

    host = Host()
    host.hostname = execute_command(ssh, HOSTNAME_CMD)
    host.cpu_name = execute_command(ssh, CPU_NAME_CMD)
    host.cpu_base_clock = execute_command(ssh, CPU_BASE_CLOCK_CMD)
    host.disk = execute_command(ssh, DISK_LIST_CMD)
    host.ip = ip
    host.os = execute_command(ssh, OS_CMD)
    host.bios_version = execute_command(ssh, BIOS_VERSION_CMD)
    host.memory = execute_command(ssh, MEMORY_CMD)
    host.memory_detail = execute_command(ssh, MEMORY_DETAIL_CMD)
    
    ssh.close()
    return host

