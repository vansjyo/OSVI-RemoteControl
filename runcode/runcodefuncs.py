import subprocess
from mysite.settings import pi_ip, pi_pwd


def kill_stop_clear():
    cmd = " sudo pkill motion"
    p = subprocess.Popen("sshpass -p "+pi_pwd+" ssh -p22 pi@" + pi_ip + cmd,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()
    cmd2 = " python3 /home/pi/runcode/stopit.py"
    p = subprocess.Popen("sshpass -p "+pi_pwd+" ssh -p22 pi@" + pi_ip + cmd2,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()
    cmd3 = "echo "+pi_pwd+" | sudo -S rm -rf ./runcode/data/videos"
    p = subprocess.Popen("sshpass -p "+pi_pwd+" ssh -p22 pi@" + pi_ip + cmd3,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.communicate()