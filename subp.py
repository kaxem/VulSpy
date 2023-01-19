import subprocess

urlInput = input("url\n")

# you need to change subfiners's path when you bua=ild docker container!
subprocess.call(["subfinder", "-d" ,f"{urlInput}", "-all","-silent", "-o", "/Users/kaaxeem/desktop/nucInput.txt" ])

## 1.go to nuclei installed folder in container
## 2. execute nuclei
## Attributes: -list: taking input from a url list from nucImput.txt
## then saving out put to a path with json format
subprocess.call(["nuclei","-l", "/Users/kaaxeem/desktop/nucInput.txt", "-silent" ])