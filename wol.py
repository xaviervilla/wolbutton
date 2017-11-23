import paramiko

# Set your ssh server ip or dns, port, username, and password.
# keep the quotes, just remove the <>
server = '<server ip/dns>' # use your raspberry pi's ip or dns. Ex. '172.217.5.110' or 'google.com'
port = '<port>' # default '22'
username = '<username>'
password = '<password>'

# Your command_to_run should be your script on your raspberry pi that wakes your computer.
# Ex: 'bash wol.sh'
command_to_run = '<command_to_run>'

# Do not edit the following.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, port, username, password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command_to_run)
