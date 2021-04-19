import pandas as pd 
import datetime


class Preprocess(): 
    """
    Preprocesses bank records into a single df sorted by date to be returned as a csv. 
    """

    def filter_account(self, account):
        """ 
        Input: 
            A CSV file of a bank account. 
        Returns: 
            A dataframe of the bank account filtered down to most important columns, plus a Transactions column.  
            Sorted by date, descending.
        """
        account = account[['Date', 'Description', 'Debit', 'Credit']]
        account = account.fillna(0)
        account['Transactions'] = account['Debit'] + account['Credit']
        
        return account[['Date', 'Description', 'Transactions']]

    def filter_credit(self, credit):
        """
        Filters the credit card dataframe won to the desired columns: Date, Transaction, and Description.
        
        Input: 
            credit: A Pandas Dataframe that should be created from an imported CSV file of a credit card
                    transaction history.  
        Returns: 
            A dataframe of the credit card's transaction history that has been filtered down to columns 
            labeled as Date, Transaction, and Description.

        """
        # Filter the credit card dataframe down to the desired columns
        credit = credit.iloc[:, [0, 1, 4]]
        credit = credit.rename(columns={0:"Date",1:"Transactions",4:"Description"})
        credit = credit[['Date','Description','Transactions']]
        credit['Date']=pd.to_datetime(credit.Date, format='%m/%d/%Y') 
        
        return credit
    
    def unify(self, checkings, savings, credit): 
        """
        Unifies checkings, savings, and credit card dataframes into one dataframe sorted by date.
        
        Input: 
            checkings: Pandas Dataframe of checking account
            savings: Pandas Dataframe of savings account 
            credit: Pandas Dataframe of credit card transcactions.  
            
        Returns: 
            A single dataframe made up of all three input dataframes, and sorted by date.  
        """
        # Filter checkings and savings dataframes down to the desired columns
        checkings = self.filter_account(checkings)
        savings = self.filter_account(savings)

        # Combine checkings and savings into one dataframe
        bank_accounts = pd.concat([checkings, savings]) # ignore_index = True 
        bank_accounts['Date'] = pd.to_datetime(bank_accounts.Date, format = '%m/%d/%Y') # Convert to Date-Time format

        # Filter the credit card dataframe down to the desired columns
        credit = self.filter_credit(credit)   

        # Combine checkings, savings, and credit card dataframes into one dataframe
        report = pd.concat([bank_accounts, credit])
        report = report.sort_values(['Date'], ascending = False)
        
        return report   
    

    def create_report(self, checkings, savings, credit): 
        """
        Creates a sorted dataframe of all monthly transactions and saves it as a CSV file.  

        Input: 
            CSV files from Checkings, Savings, and Credit Card Accounts. 
        Returns:
            A dataframe of all transactions, sorted by date in ascending order.  
        """      
        report = self.unify(checkings, savings, credit)
        
        # Determine filename based on date
        first_day = input("Please enter the starting date for the report in YYYY-MM-DD format: ")
        first_day_complete = datetime.datetime.strptime(first_day[:10], '%Y-%m-%d')

        today = datetime.date.today()
        filename = "expense-report-" + str(today.month) + str(today.year) + ".csv"

        # Filter report down to this month's history of transactions
        report = report.loc[(report['Date'] >= pd.Timestamp(first_day_complete)) & (report['Date'] <= pd.Timestamp(today))]
        report = report.sort_values(['Date'], ascending = True)

        print("Monthly Expense report compiled!  Here's what we have so far: ")
        print(report)

        report.to_csv('expense-reports/' + filename)
        print("Report saved to file!")

        return report


