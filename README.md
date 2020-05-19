#Problem Statement

A Machine is composed of some Parts. Multiple Machines can share a Part. Each Part has a Price. Price of a Machine is the summation of prices of the Parts. Given valid information about some Machines, identify the Machine(s) with highest price.

Extra Info

No Extra Information.

Input Format

First Line contains two integers M and P where M is the number of Machines and P is the number of Parts.

Next line has M numbers of space separated integers each of which indicates the number of Parts in each Machine.

Next each of P numbers of lines indicates a part. Each Part line has some space separated integers where the First integer X indicates how many Machines are associated with current Part, next X integers (in the same line) are the indices of the Machines of which the current Part is associated with and last integer is the price of the current Part



For Example, Let is take the below Input

4 6

3 4 5 3

2 1 3 700

2 2 3 140

4 1 2 3 4 90

2 2 3 270

2 2 4 300

3 1 3 4 150



First line of the input says, that we have 4 machines and 6 parts in total.

Second line says that 1st machine has 3 parts, 2nd machine has 4 parts, 3rd machine has 5 parts and lastly 4th machine has 3 parts.

Next 6 lines represent parts.



3rd line says that 1st part is associated with 2 machines, i,e 1st and 3rd machine and its price is 700.

4th line says that 2nd part is associated with 2 machines, i,e 2nd and 3rd machine and its price is 140.

5th line says that 3rd part is associated with 4 machines, i,e 1st, 2nd, 3rd and 4th machine and its price is 90.

6th line says that 4th part is associated with 2 machines, i,e 2nd and 3rd machine and its price is 270.

7th line says that 5th part is associated with 2 machines, i,e 2nd and 4th machine and its price is 300.

8th line says that 6th part is associated with 3 machines, i,e 1st, 3rd and 4th machine and its price is 150.

Output Format

Integer N which represents the machine number (from 1 to M) having highest price.

For the input given above, the output would be 3. That is the 3rd machine has highest price (1350 in this case)

Constraints

M and P both have inclusive range from 1 to 100

Price of any part can be up to 1000

There can be multiple instance of any part within a machine.



Time Limit5s.Each test case should pass in 5s.

Sample Input

4 6

3 4 5 3 

2 1 3 700 

2 2 3 140 

4 1 2 3 4 90 

2 2 3 270 

2 2 4 300 

3 1 3 4 150

Sample Output

3