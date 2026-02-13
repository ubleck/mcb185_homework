cd ~/Code/MCB185/data/
gunzip -c dictionary.gz | grep -E "^[zonica]*r[zonica]*$" | grep -vE "^.{0,3}$"