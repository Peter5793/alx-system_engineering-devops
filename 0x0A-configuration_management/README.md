# Configuration Management
## Installing puppet-lint

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
### 1. Task
#### Create a file
* File path is ```/tmp/holberton```
* File permission is 0744 
* File Owner ```www-data```
* File group ```www-data```
* File contains ```I Love Puppet``` 

#### Install a package
Using Puppet install ```puppet-lint```

Requirements:
* Install ```puppet-lint```
* Version must be ```2.1.1```

Example

```
root@d391259bf577:/# puppet apply 1-install_a_package.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.10 seconds
Notice: /Stage[main]/Main/Package[puppet-lint]/ensure: created
Notice: Finished catalog run in 2.83 seconds
root@d391259bf577:/# gem list

*** LOCAL GEMS ***

puppet-lint (2.1.1)
root@d391259bf577:/#
```
#### Execute Command
Create a manafest that kills a process named ```killmenow```
Requirements:
     * Must use the ```exec``` Puppet resource
     * Must use pkill

Example

Terminal #0 starting my process

```
root@d391259bf577:/# cat killmenow
#!/bin/bash
while [[ true ]]
do
    sleep 2
    done

root@d391259bf577:/# ./killmenow
```
Terminal #1 Executing my manifest

```
root@d391259bf577:/# puppet apply 2-execute_a_command.pp
Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
Notice: Finished catalog run in 0.10 seconds
root@d391259bf577:/#
```

Terminal #0 - Process has been terminated

```
root@d391259bf577:/# ./killmenow
Terminated
root@d391259bf577:/#
```