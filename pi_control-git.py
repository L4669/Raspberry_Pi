#! /usr/bin/python


import paramiko
import subprocess
from subprocess import Popen, PIPE

MOVIE_PATH_LOCAL = "storage/downloads/upload/Movies/"
#MOVIE_PATH_LOCAL = "/home/euler/Downloads/Upload/"
MOVIE_PATH_SERVER = "/mnt/usb2/Movies/"
BytesPerMB = 1024 * 1024

host = "192.168.1.23"
port = 22
username = "****"
password = "****"

def sshutil(cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.readlines()
    ssh.close()
    return output
    

if __name__ == "__main__":
    print("\n")
    print("*******Pi Server Control******")
    print("===============================")
    print("Available operations:")
    print("1. Shutdown Server")
    print("2. File Transfer to Movie Server")
    print("3. Change file mode for plex")
    print("\n")

    opt = input("Enter operation no.: ")

    if int(opt) == 1:
        cmd = "echo ge0des!c | sudo -S shutdown -h now"
        sshutil(cmd)
    elif int(opt) == 2:
        res = subprocess.check_output(['du', '-BM', MOVIE_PATH_LOCAL])
        res2 = str(res)
        res3 = res2.split("\\")[0]
        movie_size = float(res3.strip("bM'"))
        print("Size of upload: ", movie_size, " MB")
        cmd_var = "df -BM " + MOVIE_PATH_SERVER
        res = sshutil(cmd_var)
        res2 = res[1].split()
        res3 = res2[3]
        disk_free = float(res3.strip("M"))
        print("Disk free space: ", disk_free, "MB")

        if movie_size >= disk_free:
            print("Server does not have sufficient disk space")
            exit()
        else:
            print("Initiating File Transfer ...")
            
            cmd = "sshpass -p " + password + " scp " + MOVIE_PATH_LOCAL + "*" +\
                " " + username + "@" + host + ":" + MOVIE_PATH_SERVER

            p = Popen(cmd, shell=True, stdout=subprocess.PIPE)
            p.wait()

    elif int(opt) == 3:
        cmd = "chmod 777 " + MOVIE_PATH_SERVER + "*"
        sshutil(cmd)
    else:
        print("No valid operation selected")

    
    

