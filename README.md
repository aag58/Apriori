# Apriori

Command to execute:
---------------------------
 py apriori.py data.txt
 
 
 
 sample Output:
 ----------------------
Enter min support in %: 50
Enter min confidence in %: 50
-----------------------------------------------------------
Frequent Item Set:
-----------------------------------------------------------
pen
cheese
milk
juice
pen cheese
cheese milk
cheese juice
milk juice
cheese milk juice
-----------------------------------------------------------
Associations with confidence greater than 0.5
-----------------------------------------------------------
['pen']-->['cheese']
['cheese']-->['pen']
['milk']-->['cheese']
['cheese']-->['milk']
['cheese']-->['juice']
['juice']-->['cheese']
['milk']-->['juice']
['juice']-->['milk']
['milk', 'juice']-->['cheese']
['cheese', 'juice']-->['milk']
['cheese', 'milk']-->['juice']
['milk']-->['cheese', 'juice']
['cheese']-->['milk', 'juice']
['juice']-->['cheese', 'milk']


