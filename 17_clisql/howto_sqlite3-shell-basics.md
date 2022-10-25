# how-to :: sqlite3-shell-basics
---
## Overview
Allows organization of relational databases

### Estimated Time Cost: 0.5 hrs 

### Prerequisites:

- How to open a terminal
- have sqlite3 installed

1. start the sqlite3 program with the terminal command `sqlite3`
	1. you can create a new database at the same time instead if you do `sqlite3 <DATABASE_NAME>`
	1. you can reopen a database or create one at a specfic location with the command `.open <ADDRESS_TO_DATABASE>`
1. to create a new table use the format:
	1. `create table <TABLE_NAME>(<FIELD_NAME_0> <DATA_TYPE_0>, <FIELD_NAME_1> <DATA_TYPE_1>, ...);`
	1. or 
		```
		CREATE TABLE <TABLE_NAME> (
			<FIELD_NAME_0> <DATA_TYPE_0>, 
			<FIELD_NAME_1> <DATA_TYPE_1>,  
			...
		);
		```
1. to view all the contents of a table, use the command:
	```
	select * from <TABLE_NAME>;
	```
1. you can change the format you output the table in with `.mode <OUTPUT_FORMAT>`
	> output formats include: ascii, box, csv, column, html, insert, json, line, list, markdown, quote, table, tabs, and tcl
	
	1. csv example:
		```
		hello!,10
		goodbye,20
		```
	2. html example:
		```
		<TR><TD>hello!</TD> 
		<TD>10</TD> 
		</TR> 
		<TR><TD>goodbye</TD> 
		<TD>20</TD> 
		</TR> 
		```
	3. box example:
		```
		┌─────────┬─────┐
		│   one   │ two │
		├─────────┼─────┤
		│ hello!  │ 10  │
		│ goodbye │ 20  │
		└─────────┴─────┘
		```

1. to see a list of tables in the database use the command `.tables`

			

### Resources
* [sqlite official documentation](https://www.sqlite.org/cli.html)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Verit Li, pd8  
Justin Mohabir, pd8  
Brian Yang, pd8  
