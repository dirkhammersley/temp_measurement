import paramiko

server = "192.168.0.106"
username = "pi"
password = "raspberry"
cmd_to_execute = "touch test.txt"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(server, username=username, password=password)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)