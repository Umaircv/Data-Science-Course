
# Steps:

1. Gathering Data
-  Assessing the data (EDA)
-  Cleaning the Data
-  Dealing with missing values
-  Correcting errors in the data
2. Outliers removal
-  Visualization
-  Shapiro-wilk test
-  IQR method
-  Z-score (Assignment)
-  Droping duplicates.
3. Transforming the data
4. Normaliza the data (Data Normalization)
-  Min-Max normalization/scalling
-  Standard scalar
-  Log transformation
-  Winsorization
-  Z-score normalization
-  Decimal Scaling
5. Feature Engineering
- Organizing data
-  Columns creation
-  Renaming
-  Renaming jis ki sense
6. Saving the data to be used
7. Machine Learning
- (X,y)
- train_test split
- model
- model.fit(x_train,y_train)
- y_predict=model.pridict(X_test)
- accuracy_score(y_test,y_pred)
- from sklearn.metrics import precision_score, recall_score, f1_score
- precision_score(y_test, y_pred)
- confusion matrix
- cm=sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap='Blues')
