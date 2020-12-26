# Introduction
This project is python based tools to convert perforce repos to git repos. Then, the git repos can be used by `sourcegraph` for code search.

# Available Scripts
## `make clone_wxe_ap`
Clone `wxe_ap` perforce repo to git repo. The detailed info is defined at [config.wxe_ap.json](./config.wxe_ap.json) file.
## `make sync_all`
Sync all git repos. Refer to config files for the repo info.

# Serve Git Repos
## wxe_ap
```sh
cd /lan/cva/hsv-apfw/yuxiangw/src/git_repos/src_main_wxe/ap
sudo docker run --rm=true --publish 3440:3434 --volume /lan/cva/hsv-apfw/yuxiangw/src/git_repos/src_main_wxe/ap:/data/wxe_ap:ro sourcegraph/src-cli:latest serve-git data/wxe_ap
```
## wxe_ua
```sh
cd /lan/cva/hsv-apfw/yuxiangw/src/git_repos/src_main_wxe/ua
sudo docker run --rm=true --publish 3441:3434 --volume /lan/cva/hsv-apfw/yuxiangw/src/git_repos/src_main_wxe/ua:/data/wxe_ua:ro sourcegraph/src-cli:latest serve-git data/wxe_ua
```
## apollo_2_x
```sh
cd /lan/cva/hsv-apfw/yuxiangw/src/git_repos/firmware/apollo_2_x
sudo docker run --rm=true --publish 3442:3434 --volume /lan/cva/hsv-apfw/yuxiangw/src/git_repos/firmware/apollo_2_x:/data/apollo_2_x:ro sourcegraph/src-cli:latest serve-git data/apollo_2_x
```

# Detailed Commands
This projects based on `git-p4` command. Here are the based commands for `clone` and `sync`.
## clone
```sh
git p4 clone -v --destination wxe_ap //hsv/ap2/ap@all //hsv/mainwxe/ap@all
```
or
```sh
mkdir ap
git init
git p4 sync -v //hsv/ap2/ap@all //hsv/mainwxe/ap@all
git branch master refs/remotes/p4/master
git checkout -f
```
## sync force
```sh
git p4 sync -v //hsv/ap2/ua@all //hsv/ap_main/ua@all //hsv/mainwxe/ua@all
git checkout dev
git branch -f master refs/remotes/p4/master
git checkout master
```

