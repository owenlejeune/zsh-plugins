alias fix-audio="pavucontrol"

function open() {
	DIR="."
	if [[ $# -gt 0 ]];
	then
		DIR="$1"
	fi
	gio open $DIR
}

function trash() {
	gio trash $@
}
