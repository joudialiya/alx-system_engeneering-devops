Upload files to a remote device via sftp/ftp
1. First, you need to connect to the sftp/ftp server
```$ sftp username/password```
INFO: stfp has a shell like CLI that supports basic file manipulation in the remote server side like [cd, mkdir]
	cd: change dir
	mkdir: make dir
2. Naviate to the folder where you want the files to be uploded
3. Use the put command to uplode the files
```$ sftp put [path of the file in the local env]```
4. done
