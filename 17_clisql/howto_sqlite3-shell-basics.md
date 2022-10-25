# how-to :: sqlite3-shell-basics
---
## Overview
- ```bash
    sqlite3 ex1
    ``` 
    - creates a file called ex1 in the terminal

- ```sql
    create table tbl1(one text, two int);
    ```
  - tbl1 is the name of the table, one and two are column names, and the text/int are object type
- ```sql
    tbl1 values('hello!',10);
    ```
    - will add a row with column onw containing 'hello!' and column two containing 10

- We can use different output types to display tables, with .mode csv/markdown
- ```sql
    select * from tbl1;
    ```
  - Display the table in the shell (mardown mode depicted below)

|  one   | two |
|--------|-----|
| hello! | 3   |
| goof   | 403 |

- ```sql
    .mode box --wrap 30
    ``` 
    - displays a table in the shell
- ```sql
    select * from tbl1 where two>50; 
    ``` 
    - will only display the rows where their element in column "two" is greater than 50
- JSON appears to be a list of python dictionaries
### Estimated Time Cost: 0.5 hrs 

#### Contributors:  
Verit Li, pd8  
Justin Mohabir, pd8  
Brian Yang, pd8  
