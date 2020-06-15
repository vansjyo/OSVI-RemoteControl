import subprocess
import os
import mmap
from fabric import Connection
from mysite.settings import pi_ip, pi_pwd

class RunPyCode(object):
    
    def __init__(self, code=None):
        self.code = code
        if not os.path.exists('./runcode/running'):
            os.mkdir('./runcode/running')

    def _run_py_prog(self, cmd="./osvi/a.py"):
        p = subprocess.Popen("sshpass -p "+pi_pwd+" ssh -p22 pi@"+pi_ip+" python3 "+cmd,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        try:
            result = p.wait(timeout=20)
            a, b = p.communicate()
            self.stdout, self.stderr = a.decode("utf-8"), b.decode("utf-8")
            return result
        except:
            self.stdout, self.stderr = "Your output should be visible on the live stream, since programmatically " \
                                       "you have used an infinite loop, the execution will time out after 20 seconds", \
                                       "Execution Timed Out!, No infinite loops please"

    def run_py_code(self, code=None):
        filename = "./runcode/running/a.py"
        if not code:
            code = self.code
        with open(filename, "w") as f:
            f.write(code)
        c = Connection(host=pi_ip, user='pi', connect_kwargs={'password': pi_pwd}, connect_timeout = 10)
        c.put("./runcode/running/a.py",'./runcode/running/a.py')
        c.close()
        self.test_py_code(filename)
        return self.stderr, self.stdout

    def test_py_code(self, code=None):
        filename = "./runcode/running/a.py"
        flag = 0
        with open(filename, 'rb', 0) as file, \
                mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
            while True:
                if s.find(b'shutdown') != -1:
                    flag = 1
                    break
                if s.find(b'ifconfig') != -1:
                    flag = 1
                    break
                if s.find(b'reboot') != -1:
                    flag = 1
                    break
                if s.find(b'halt') != -1:
                    flag = 1
                    break
                if s.find(b'rm') != -1:
                    flag = 1
                    break
                if s.find(b'poweroff') != -1:
                    flag = 1
                    break
                else:
                    break
        if flag != 0:
            self.stdout = ''
            self.stderr = 'Malicious Code!'
        else:
            self._run_py_prog(filename)
