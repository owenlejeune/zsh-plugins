alias allowanywhere="sudo spctl --master-disable"
alias resetaudio="sudo killall coreadiod"

function screensaver() {
  open -a ScreenSaverEngine.app
}

function finder() {
  DIR="."
  if [[ $# -gt 0 ]];
  then
    DIR="$1"
  fi
  open $DIR
}

function quick-look() {
  (( $# > 0 )) && qlmanage -p $* &>/dev/null &
}

function man-preview() {
  man -t "$@" | open -f -a Preview
}

function open-preview() {
  "$@" | open -f -a Preview
}

# Spotify control function
source ${ZSH}/plugins/osx/spotify

# Show/hide hidden filed in the Finder
alias showfiles="defaults write com.apple.finder AppleShowAllFiles -bool true && killall Finder"
alias hidefiles="defaults write com.apple.finder AppleShowAllFiles -bool false && killall Finder"

# Remove .DS_Store files recursively in a directory, default .
function rmdsstore() {
  find "${@:-.}" -type f -name .DS_Store -delete
}
