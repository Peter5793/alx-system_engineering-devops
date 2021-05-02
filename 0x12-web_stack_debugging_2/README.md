# Web Stack Debugging

## Task 1

Run the software as another user
Requirements:
 * Bash script that accepts one argument
 * Script should run the commnda ```whoami``` command under the user passed as argument
Example:
```
root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
```
