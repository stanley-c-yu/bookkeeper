# Bookkeeper 

Bookkeeper is a simple command line application that compiles a monthly report 
regarding all transactions that have been made to your checkings and savings account, as
well as all transactions made with a single credit card.  

It works by accepting three csv files, one for each of your accounts, and then intelligently 
combines the three into a single dataframe that is sorted by date.  The dataframe is then 
saved as a csv file for later reference.  

Note that the folders, 'bank-records' and 'expense-reports' will need to be re-created locally
first in order for this application to actually work.  


## Usage 

Just run either 'python run.py' or 'python3 run.py' and respond to the prompts accordingly.

```sh
$ python3 run.py 
```

Once the report is created, a simple barplot will be displayed. 

```sh
Money in bank            : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 5733.00
Money owed to credit card: ▇▇▇ 441.67
Money adjusted for credit: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 5291.33
```