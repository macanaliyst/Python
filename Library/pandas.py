############################################################################################################################################ Calculate Month diff pandas
## Month : Purchase Month
## MonthStarted : First Purchase month per Customer
## Using function datetime.dt.to_period()

retail['MonthPassed'] = retail['Month'].dt.to_period('M').astype(int) - \
                        retail['MonthStarted'].dt.to_period('M').astype(int)
