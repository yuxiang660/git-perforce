# Introduction
The `requirements` folder is about softwares dependencies for ["Using Perforce repositories with Sourcegraph"](https://docs.sourcegraph.com/admin/repo/perforce).

# Git P4
[git-p4.py](./git-p4.py) is modified based on origianl [git-p4.py](https://git.wiki.kernel.org/index.php/GitP4#Adding_git-p4_to_an_existing_install) to perform `git fast-import` with `force` option.
```python
self.importProcess = subprocess.Popen(["git", "fast-import", "--force"],
                                              stdin=subprocess.PIPE,
                                              stdout=subprocess.PIPE,
                                              stderr=subprocess.PIPE)
```

# Docker
To install docker with rpm packages for `Red Hat Enterprise Linux Workstation release 7.6 (Maipo)`, you can follow following steps.
* enter [docker installer](./docker) folder
``` sh
sudo yum install containerd.io-1.2.0-3.el7.x86_64.rpm
sudo yum install docker-ce-17.03.0.ce-1.el7.centos.x86_64.rpm docker-ce-selinux-17.03.0.ce-1.el7.centos.noarch.rpm
```
* start docker daemon
```sh
sudo systemctl start docker
```
or
```sh
sudo service docker start
```
* test docker
```sh
sudo docker run hello-world
```
