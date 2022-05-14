############################################################################################################################################ Calculate Month diff 
## Month : Purchase Month
## MonthStarted : First Purchase month per Customer
## Using function datetime.dt.to_period()

retail['MonthPassed'] = retail['Month'].dt.to_period('M').astype(int) - \
                        retail['MonthStarted'].dt.to_period('M').astype(int)


###################################################################################################################################### Create 30 minute time interval

order_by_hour_half = retail.set_index('InvoiceDate') \
                     .groupby(lambda x : str(x.hour) + ':' + '00' if x.minute < 30 \
                                    else str(x.hour) + ':' + '30') \
                     .count()['CustomerID']
order_by_hour_half
