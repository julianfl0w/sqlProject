SELECT AVG(Amount) AS MeanAmount,
       STDEV(Amount) AS StdDevAmount
FROM [master].[dbo].[Transactions];
