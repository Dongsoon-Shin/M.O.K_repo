Berthier, with your help the computer have been identified.
You have requested a memory dump and before starting your analysis you want to take a look at the antivirus logs. 
Unfortunately you forget to write down the workstation hostname.
But it’s not a problem to get it back since you have a memory dump.

The validation flag is the workstation hostname

file source -> https://www.root-me.org/en/Challenges/Forensic/Command-Control-level-2

my solution 

we can see a bzip file after downloading file from above.
check this fact with linux command 'file' and decompress it with bzip2 decompress option 'bzip -d'
after that, A dmp file is appeared. 

using strings ch2.dmp | grep computer, you can find hostname.

COMPUTERNAME=WIN-ETSA91RKCFP

Written by blueksg0307@gmail.com



