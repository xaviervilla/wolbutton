import paramiko

# Set your ssh server ip or dns, port, username, and password.
# Keep the quotes, just remove the <>.
server = '172.217.5.110' # use your PC that you want to sleep's ip or dns. Ex. '172.217.5.110' or 'google.com'
port = '22' # default '22'
username = 'username'
password = 'password'
command_to_run = "echo 'YOUR LINUX PASSWORD' | sudo -S pm-suspend" # In linux this suspends your PC.

# Do not edit the following.
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, port, username, password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command_to_run)
