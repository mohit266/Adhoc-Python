import os

for i in range(50):
    os.system("docker run -itd --name web"+i" -p 120"+i":80 Mohitweb")
