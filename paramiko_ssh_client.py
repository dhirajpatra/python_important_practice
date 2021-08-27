from paramiko import SSHClient

client = SSHClient()
client.load_system_host_keys()
client.connect(
    '202.88.246.92',
    username='superuser',
    password='Techversant!2020',
    key_filename='/home/dhirajpatra/dev4.pem'
)
stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.readlines())
client.close()
