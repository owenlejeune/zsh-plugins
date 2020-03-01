alias gadd="git add"
alias gadda="gadd -A"
alias gstatus="git status"
alias gdiff="git diff"
alias glog="git log"
alias glast="glog -p -1"
alias gcheckout="git checkout"
alias gcheckoutb="gcheckout -b"
alias gcheckoutf="gcheckout --"
alias gpull="git pull origin"
alias gpullm="gpull master"
alias grebase="git rebase"
alias gcommit="git commit"
alias gcommitm="git commit -m"
alias gamend="gcommit --amend"
alias gbranch="git branch"
alias rnmbranch="gbranch -m"
alias gpushb="git push origin"

function gpush() {
	BRANCH=""
	if [[ $# -eq 0 ]];
	then
		BRANCH="$(git rev-parse --abbrev-ref HEAD)"
	else
		BRANCH="$1"
	fi
	git push origin $BRANCH
}
