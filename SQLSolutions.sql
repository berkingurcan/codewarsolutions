--// 8 and 7 Kyu problems

/*You work at a book store. It's the end of the month, and you need to find out the 5 bestselling books at your store. Use a select statement to list names, authors, and number of copies sold of the 5 books which were sold most.

books table schema

name
author
copies_sold
NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

*/

SELECT name, author, copies_sold
FROM books
ORDER BY copies_sold DESC
LIMIT 5

/*Given the following table 'decimals':

** decimals table schema **

id
number1
number2
Return a table with two columns (root, log) where the values in root are the square root of those provided in number1 and the values in log are changed to a base 10 logarithm from those in number2.*/

select sqrt(number1) as root, log(number2) as log
from decimals


/*In your application, there is a section for adults only. You need to get a list of names and ages of users from the users table, who are 18 years old or older.

users table schema

name
age
NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.*/

SELECT name, age
FROM users
WHERE age > 17

/*For this challenge you need to create a simple SUM statement that will sum all the ages.

people table schema
id
name
age
select table schema
age_sum (sum of ages)
NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

NOTE2: You need to use ALIAS for creating age_sum*/

SELECT sum(age) as age_sum FROM people

/*Very simple, given a number, find its opposite.

Examples:

1: -1
14: -14
-34: 34*/

SELECT -1*number AS res
FROM opposite

/*You will need to create SELECT statement in conjunction with LIKE.

Please list people which have first_name with at least 6 character long

names table schema
id
first_name
last_name
results table schema
first_name
last_name*/

SELECT first_name, last_name
FROM names
WHERE first_name LIKE '______%'

/*For this challenge you need to create a simple MIN / MAX statement that will return the Minimum and Maximum ages out of all the people.

people table schema
id
name
age
select table schema
age_min (minimum of ages)
age_max (maximum of ages)
NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.*/

select min(age) as age_min, max(age) as age_max from people

/*Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59*/

select h*3600000 + m*60000 + s*1000 as res from past

/*Messi goals function
Messi is a soccer player with goals in three leagues:

LaLiga
Copa del Rey
Champions
Complete the function to return his total number of goals in all three leagues.

Note: the input will always be valid.

For example:

5, 10, 2  -->  17*/

Select la_liga_goals + copa_del_rey_goals + champions_league_goals as res
FROM goals
-- you will be given a table, goals, with columns la_liga_goals, copa_del_rey_goals, and champions_league_goals. Return a table with a column, res.

