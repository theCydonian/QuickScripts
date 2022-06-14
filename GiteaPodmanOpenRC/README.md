# GiteaPodmanOpenRC

These are the two init scripts I use to start, stop and manage my Gitea server 
using OpenRC and Podman.

If you want to use them, clone this repo, and move both files to `/etc/init.d/`

I found [this](https://blog.while-true-do.io/podman-setup-gitea/) tutorial to 
be useful, but it uses SystemD and not OpenRC. Using my init scripts, you can 
follow the tutorial but using OpenRC.
