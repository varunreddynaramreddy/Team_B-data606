#### Highlevel Final Model Architecture
![image](https://user-images.githubusercontent.com/106714374/185816412-e96de9ac-35c4-46a9-96b2-4777d17555a6.png)

#### Model Stack Used
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- AdaBoost
- SVM

#### Model Results Analysis
##### With Class Balancing vs Without Class Balancing:
- Class balancing with oversampling provided significant improvement across all model validation metrics
-   F1 Score showed an improvement of over 15% (In Train set)
- Recall showed a increase of 21% (in train set) percent port class balancing 
- Improvement is observed consistently across models as well as test and train sets

##### Test vs Train (for Models with Class Balancing):
- Average F1 Score on train dataset is ~69% while for test data is 46%
- A significant difference in test and train performance is observed suggesting a slight overfit across models

##### Model (Algo) vs Model (Algo):
- Though Xgboost and Random Forest models have exceptional train performance but are failing drastically in test performance
- Adaboost classifier shows consistent performance across train and test sets in comparison with other models
- Adaboost has been selected as file model for production
![image](https://user-images.githubusercontent.com/106714374/185816872-b299f9bd-defb-4535-9c01-0f6c5672f5fb.png)


#### Cross Model Results Comparsion
![image](https://user-images.githubusercontent.com/106714374/185816680-2b257ad6-b45f-47a0-b1e3-0f416f718dbe.png)

#### Adaboost Model Validation Metrics (Finalized Model)
##### Key Model Validation Parameters
![image](https://user-images.githubusercontent.com/106714374/185816750-1b1a47cb-5bbb-44db-8024-4272c74111ee.png)
##### ROC Curve
![image](https://user-images.githubusercontent.com/106714374/185816710-c04d1bc2-9b54-4887-90c9-2da69c973038.png)
##### Feature Importance
![image](https://user-images.githubusercontent.com/106714374/185816734-94d509a1-ae65-467a-a97e-ceea78d51eed.png)

#### Modeling Summary
- Data used modeling showed the presence of class imbalance and mostly every model showed improved F1 score port treating for class imbalance
- F1 Score has been used as primary metric for model selection while other metrics like precision, recall etc., are using as supporting metrics
- Tree based and linear model stack has been tested on the data. It is observed that tree based models (RF, XGBoost etc.,) showed better performance in comparison with linear models (logistic regression etc.,)
- All model parameters have been selected using grid search along with k-fold cross validation
- Average F1 Score on train dataset is ~69% while for test data is 46%

Though Xgboost and Random Forest models have exceptional train performance but are failing drastically in test performance. Adaboost classifier showed consistent performance across train and test sets in comparison with other models
Adaboost has been selected as file model for production
