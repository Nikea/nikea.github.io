#! /bin/bash
if [ ! -d ~/dev]
    then
        mkdir ~/dev
fi
cd ~/dev
https="https://github.com/"
ssh="git@github.com:"
prefix=$https
if ["$1" == "https"]
    then
        prefix=$https
fi
if ["$1" == "ssh"]
    then
        prefix=$ssh
fi
echo $prefix
## respositories to clone
declare -a repo_names=("NSLS2" "vistools" "KitchenSink" "NSLS-II.github.io")
## user names of developers
declare -a user_names=("ericdill" "tacaswell" "sameera2004" "giltis" "jammcc" "stuwilkins" "CJ-Wright" "dchabot" "sbillinge")
## remote names for the devs branches
declare -a alias=("dill" "caswell" "sameera" "iltis" "mcclintock" "wilkins" "wright" "chabot" "billinge")
suffix=".git"
## loop through the repositories
for repo in "${repo_names[@]}"
do
    echo removing "$repo" repository
    rm -rf "$repo"
    url="$prefix""NSLS-II/""$repo""$suffix"
##    echo echoing repo_names: $url
    git clone $url
    cd "$repo"
    git remote rename origin nsls2
    # loop through the user names
    for idx in "${!user_names[@]}"
    do
        url="$prefix""${user_names[idx]}""/""$repo""$suffix"
##        echo remote url: $url
        git remote add "${alias[idx]}" $url
	done
	git remote update
	cd ..
done
