xcopy() { $1 | xclip -selection clipboard; }
xcopyf() { cat $1 | xclip -selection clipboard; }
xpaste() { xclip -selection clipboard -o; }
