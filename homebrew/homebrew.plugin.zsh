function brewup() {
	echo "***BREW UPDATE***"
	brew update
	echo "***BREW UPGRADE***"
	brew upgrade
	echo "***BREW CLEANUP***"
	brew cleanup
	brew autoremove
	echo "***BREW DOCTOR***"
	brew doctor
}
