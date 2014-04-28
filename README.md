github-sync-fork-script
=======================

Python script to sync your github fork to its parent repository.

## Installation

* Download the script [here](https://github.com/imagentleman/github-sync-fork-script/archive/master.zip).
* Put the script gsync.py on your path. In Windows you would probably place it on the root of your python folder (which in most cases is already in the path), somewhere like `C:\Python27`. That way the script would be callable from any folder.

## Usage

* Clone your repo and cd into its folder.
* Run gsync.py
* Cake

The Script has some basic error handling. It will catch if the repo is not a fork (in that case there won't be anything to sync), if you are not in the folder of a git repo, etc.

## How does it work?

The script basically follows the github syncing instructions [page](https://help.github.com/articles/syncing-a-fork), but saving you the need to search for the parent repo's git url (which the script gets automatically from github) and typing the 100+ characters of the 4+ needed git commands.
