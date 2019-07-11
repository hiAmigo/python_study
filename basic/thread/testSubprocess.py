import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print(r)
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))

p = subprocess.Popen('ls', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = p.communicate('/home')
print(out)
