# 2025.12.28 - On The Fourth Day Of Coding...

My solution -> *[2025_12_28_on_the_fourth_day_of_coding](2025_12_28_on_the_fourth_day_of_coding.py)*

## **_Task condition:_**

*_On the fourth day of coding my team lead sent to me... Four dining elves,_*

*_Three security rules, two pointers, and a nasty bug in a production tree!_*

Mr. Frost looks exhausted. "We have a situation in the cafeteria. Four elves - Jingle, Sparkle, Tinsel, and Holly - are sitting around a circular table trying to eat lunch. There are four forks on the table, one between each pair of elves. Each elf needs TWO forks to eat (the one on their left AND the one on their right)."

He pulls up a log on his screen. "The problem is, they keep trying to grab forks that other elves are already using. Every time an elf attempts to pick up a fork that's currently held by someone else, it causes a 'contention' - they have to wait, complain, and it slows everything down."

"I need you to analyze this log and count how many contentions occurred during lunch. Help me figure out how bad the problem really is."

**Input**: logs of actions separated by newline. Each log contains name of the elf, action (pick or release) and an id of a fork, all separated by comma.

**Example**: `Jingle,pick,3`

**Output**: Total number of contentions (attempts to pick up a fork that's already held by another elf).

**Order of elves and forks around the table:**

*_`Jingle - Fork_1 - Sparkle - Fork_2 - Tinsel - Fork_3 - Holly - Fork_4 - (back to) Jingle`_*

**_NOTES:_**

- Data for this task is located in given file - *[hyperskill-dataset-119029174.txt](hyperskill-dataset-119029174.txt)*.
- You will need to submit only the right answer as plain text.
- You can write and run code in IDE of your choice.

#

<br />