# Introduction
This project is python based tools to convert perforce repos to git repos. Then, the git repos can be used by `sourcegraph` for code search.

# Available Scripts
## `make clone_wxe_ap`
Clone `wxe_ap` perforce repo to git repo. The detailed info is defined at [config.wxe_ap.json](./config.wxe_ap.json) file.
## `make sync_all`
Sync all git repos. Refer to config files for the repo info.
