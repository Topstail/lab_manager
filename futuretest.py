# from concurrent.futures import ThreadPoolExecutor
# from paramiko import SSHClient
# import paramiko
# import time


# def get_ssh_client(remote_ip,
#                    remote_port,
#                    remote_username,
#                    remote_password):

#     sshclient = paramiko.SSHClient()
#     sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     sshclient.connect(hostname=remote_ip, port=remote_port,
#                       username=remote_username, password=remote_password)
#     return sshclient


# def execute_command(sshclient: SSHClient, cmd):
#     stdin, stdout, stderr = sshclient.exec_command(cmd)
#     stdout.channel.set_combine_stderr(True)
#     output = stdout.read().decode("utf-8")
#     return output.strip()


# def cmd(i):
#     return i+1


# ssh = get_ssh_client('10.238.152.107', 22, 'root', 'intel@123')
# HOSTNAME_CMD = '''hostname'''
# CPU_NAME_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f1 | sed 's/\$//g' '''
# CPU_BASE_CLOCK_CMD = '''lscpu | grep "^Model name" | cut -d: -f2 | cut -d@ -f2'''
# DISK_LIST_CMD = '''lsblk | egrep -e "^sd|^nvme" | awk '{print $1,$4}' '''
# OS_CMD = ''' grep -i "PRETTY_NAME" /etc/os-release | cut -d'"' -f2 '''
# BIOS_VERSION_CMD = ''' dmidecode -t bios | grep -i "version" | awk '{print $2}' '''
# MEMORY_CMD = ''' dmidecode -t memory | grep  Size: | grep -v "No Module Installed" | grep -v "MB" | grep -v "Unknown" | awk '{sum+=$2}END{print sum"GB"}' '''
# MEMORY_DETAIL_CMD = ''' dmidecode -t memory | grep -e "Size" -e "Speed" | grep -v "Configured Memory" | awk '{if(NR%2==1)printf $2 $3 " ";else print $2 $3}' '''
# cmd_dict = {'hostname': HOSTNAME_CMD,
#             'cpu_name': CPU_NAME_CMD,
#             'cpu_base_clock': CPU_BASE_CLOCK_CMD,
#             'disk': DISK_LIST_CMD,
#             'os': OS_CMD,
#             'bios_version': BIOS_VERSION_CMD,
#             'memory': MEMORY_CMD,
#             'memory_detail': MEMORY_DETAIL_CMD}

# # startTime = time.time()
# # result_list = [execute_command(ssh, cmd) for k, cmd in cmd_dict.items()]
# # exe_complete_time = time.time()
# # for result in result_list:
# #     print(result)
# # endTime = time.time()
# # # startTime:1639979375.5930543
# # # exe_complete_time:1639979376.1835997
# # # endTime:1639979376.183857

# startTime = time.time()
# result_dict = {}
# with ThreadPoolExecutor(max_workers=5) as executor:

#     futures = {name: executor.submit(
#         execute_command, ssh, command) for name, command in cmd_dict.items()}
#     for k, v in futures.items():
#         print("%s:-->%s" % (k, v.result()))
#     # futures = [executor.submit(execute_command, ssh, command) for k, command in cmd_dict.items()]
#     # exe_complete_time = time.time()
#     # for future in futures:
#     #     print(future.result())

# endTime = time.time()
# print('startTime:%s' % startTime)
# # print('exe_complete_time:%s' % exe_complete_time)
# print('endTime:%s' % endTime)
# # startTime:1639980095.1641066
# # endTime:1639980095.760198
