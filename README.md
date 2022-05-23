#Baumis Repomanager

My little helper to maintain my own repository. 


# Installation

`git clone https://github.com/bauminao/repomanager.git`

# Setup and Initialisation

Clone the Repos you want to have inside your repo wihtin farming
Just take the Repo-Link from [AUR](https://aur.archlinux.org) and do a `git clone <RepoLink>` inside farming directory. 

There are two lists:
* ignore 
* locked

To activate them copy the template files to real files. 

## ignored

packages are not taken into account at all. Nothing is done on these directories. 

## locked

Once a package is created, a tag with the name of the REPO is set on the package repo. 
If locked:
  * No updates are pulled, 
  * no new compilation is done 
  * If you force to re-compile the commit with the tag of "REPO" is taken into account.

# Create packages 

# Add to Repo 

# Update packages automatically

# Replace packages in Repo 

