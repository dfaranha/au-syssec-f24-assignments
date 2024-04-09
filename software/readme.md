# Attacking and defending software

## Your Task(s)

In this task, you will study and reproduce a working local or remote exploit against a piece of vulnerable software. By observing how exploits work you will get a better understanding of how vulnerabilities affect software security in practice.

1. Find an interesting software vulnerability that can be exploited locally or remotely (for example in a CVE database) against a relevant software package. A classic and interesting starting point is the heap overflow against the WU-FTPD server, version 2.6.1, linked [here](https://static.lwn.net/2001/1129/a/wuftpdheapbug.php3). Some other suggestions are: Stagefright, Shellshock, KRACK, Dirty COW, Spectre, Meltdown, SGAxe, Log4shell. The list is long, so I am sure there is something for everybody to play with. :)
2. Find a working exploit for that vulnerability. In most cases, a proof-of-concept exploit is part of the disclosure process and remain publicly available after the software is fixed.
3. Assemble an execution environment to run the vulnerable software (VM) and execute the exploit.
4. Document in detail how the exploit works and the behavior observed in the system and over the network (for example, using a network sniffer such as Wireshark).

## Logistics:

Submit a short report (up to 7 pages, 12-point font, double-column format) detailing your observations, with due date on 29/04/2024. In your report, document the threat model in which the vulnerability can be exploited, the security properties that were violated and explain how the vulnerability was fixed.
The work is in groups of at most 3 students and should be submitted within Brightspace. For the larger groups, please consider that you have more hands and attempt to be more ambitious in terms of scope and target.
