#!/usr/bin/python
# coding=utf-8

from __future__ import print_function
from subprocess import check_output, call
import urllib2
import json
import sys

if __name__ == '__main__':
    """Run a bunch of boilerplate commands to sync your local clone to its
       parent github repo.

    """
    print("Starting sync...", "\n")

    CURRENT_REPO_CMD = ['git', 'config', '--get', 'remote.origin.url']
    ADD_REMOTE_CMD = ['git', 'remote', 'add', 'upstream']
    CHECK_REMOTES_CMD = ['git', 'remote', '-v']
    FETCH_UPSTREAM_CMD = ['git', 'fetch', 'upstream']
    CHECKOUT_MASTER_CMD = ['git', 'checkout', 'master']
    MERGE_UPSTREAM_CMD = ['git', 'merge', 'upstream/master']

    try:
        repo_url = check_output(CURRENT_REPO_CMD)
        print("Getting repo's url...")
        print("Syncing repo:", repo_url)

        url_segments = repo_url.split("github.com/")
        path = url_segments[1]
        user, repo = path.split("/")

        print("Checking the fork's parent url...", "\n")
        url = "https://api.github.com/repos/{}/{}".format(user, repo)
        req = urllib2.urlopen(url)
        res = json.load(req)
        parent_url = res['parent']['git_url']

        print("Will add remote to parent repo:", parent_url, "\n")
        ADD_REMOTE_CMD.append(parent_url)
        print(ADD_REMOTE_CMD)
        call(ADD_REMOTE_CMD)
        print("")

        print("Checking remotes...", "\n")
        call(CHECK_REMOTES_CMD)
        print("")

        print("Fetching upstream...", "\n")
        call(FETCH_UPSTREAM_CMD)
        print("")

        print("Merging upstream and master", "\n")
        check_output(CHECKOUT_MASTER_CMD)
        call(MERGE_UPSTREAM_CMD)
        print("Syncing done.")

    except Exception as e:
        e_type = sys.exc_info()[0].__name__
        print("The following error happened:", e, "\n")

        if (e_type == 'CalledProcessError' and
            hasattr(e, 'cmd') and
            e.cmd == CURRENT_REPO_CMD):
            print("Are you sure you are on the git repo folder?", "\n")
        elif (e_type == 'IndexError' and
            e.message == 'list index out of range'):
            print("Sorry, couldn't get the user and repo names from the Git config.", "\n")
        elif (e_type == 'KeyError' and
            e.message == 'parent'):
            print("Are you sure the repo is a fork?")
        elif (e_type == 'CalledProcessError' and
            (e.cmd == MERGE_UPSTREAM_CMD or e.cmd == CHECKOUT_MASTER_CMD)):
            print("Didn't merge. Reason:", e.output)
        print("Game Over.")
