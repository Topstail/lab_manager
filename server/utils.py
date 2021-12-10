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
    GET_SSD_LIST_CMD = '''lsblk | egrep -e "^sd|^nvme" | awk '{print $1,$4}''''
    HOSTNAME_CMD = '''hostname'''


    ssh = get_ssh_client(ip, port, username, password)

    host = Host()
    host.hostname = execute_command(ssh, HOSTNAME_CMD)
    host.cpu_name = execute_command(ssh, CPU_NAME_CMD)
    host.cpu_base_clock = execute_command(ssh, CPU_BASE_CLOCK_CMD)
    # print(execute_command(ssh, GET_SSD_LIST_CMD))
    # host.save()
    
    ssh.close()
    return host

