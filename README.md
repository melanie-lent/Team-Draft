# Pokemon Team Drafter

For strategy in playing Pokemon GO. Generates a balanced team of 6 pokemon and their ideal movesets and IVs, uses simulated annealing.

Sample data is based on the PvPoke dataset

## Analyzing results

Pokemon in a team will be displayed with abbreviated forms of their ideal moveset and IV values (in order being *attack*, *defense*, and *stamina*.)

For example, if you see ```Mismagius H+SB/DP 5/8/13``` in your results, the program suggests that you use a Mismagius with Hex as their quick attack, and Shadow Ball or Dark Pulse as a charge attack, with their attack value as 5, defense value as 8, and stamina value as 13.

A team's utility score represents the likelihood they will win in a battle. For a utility value > 500, they're more likely to win. For utility < 500, less likely to win. The higher the utility, the better.

## To use

Run ```python3 teamDraft.py filename``` in a terminal where ```filename``` is the name of the tournament data file. Do not include a directory or other prefix.

Current built-in options are ```h.matrix.p``` and ```l.matrix.p```.

For example, run ```python3 teamDraft.py l.matrix.p``` inside your Team Draft directory.