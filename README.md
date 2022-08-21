## Draft Proposal - Team 
By 

N.Varun Reddy

N.Vyshnavi
<br/>
## Advanced Data Driven Marketing for Optimizing Business's Marketing ROIs
Marketing is a great tool for most of the businesses for boosting sales. It is an important function in any business as production and distribution largely depend on marketing success. With the growth of technology and digital marketing, traditional marketing channels like direct telemarketing etc., are failing to capture business attention. One the major reason for this is the swift change in business operations as well as customer needs. Data driven campaign management in direct telemarketing can improve the performance. Advent of **Covid in 2020** is demanding more returns from marketing activities with limited or reduced budget across businesses. Data driven campaign management is the only option for business under these circumstances for Optimizing revenue generated from marketing campaigns.

<p align="center">
  <img src="https://user-images.githubusercontent.com/21233507/172528504-1756116b-121f-4993-a913-0247b98a392d.png"/>
</p>
<br/>
Figure showing the decline of marketing budgets (between 2019-2020) across major banks in Banking industry
<br/>
Source: https://emiboston.com/banks-cut-marketing-spend-in-2020-but-expect-to-ramp-up-investment-in-2021/

### Project Scope
Current project scope will be limited to Telemarketing. one of the traditional direct marketing strategies. Direct telemarketing enjoys certain major advantages over other marketing channels in terms of Ease of Targeting, Personalization and Measurability (which digital channels lack majorly). The act of telemarketing has four major categories Outbound Calls, Inbound Calls, Lead Generation and Sales. Current solution doesnt differentitate between these categories due to data limitations. 
**Direct marketing campaign data** of a **Portuguese banking institution** will be used for this project. Dataset captures the marketing campaigns which are run on phone where more than one contact to the same client is required  in order to access if back term deposit would be subscribed by the customer or not. 
<br/>
<p align="center">
  <img src="https://user-images.githubusercontent.com/21233507/172533550-290ceb26-a365-469c-b824-4bd2c402239e.png"/>
</p>
<br/>

### Solution Objective and Highlevel Architecture
High cost per call and requirement  of multiple touch points in customer acquisition journey results in high customer acquisition cost which in turn effects telemarketing's return on investments (ROIs). Building a Machine learning solution for proactively predicting the propensity of customer to subscribe for term deposit at each stage can help taking appropriate next best actions. Customer subscription propensity help in customer/call prioritization by eliminating the resource wastage the incurs due to reaching out to non-potential customers.

<p align="center">
  <img src="https://user-images.githubusercontent.com/21233507/172555357-45b61116-58f9-4f2d-8f4d-da5827ca5c7e.png"/>
</p>
<p align="center">
 Solution Architecture
</p>

<h4><u>Key Business Questions Answered</u></h4>

- What are the major factors driving subscriptions (subscriptions)?
- What is the probability of customer's conversion on targeting him through direct telemarketing?
- Who are the list of customers that can be proactively targeted for easy conversions?

### Data: Key Attributes and Summary
Independant Variable:
- age
- job : type of job
- marital : marital status
- education
- default: has credit in default?
- housing: has housing loan?
- loan: has personal loan?
- contact: contact communication type
- month: last contact month of year
- day_of_week: last contact day of the week
- duration: last contact duration, in seconds (numeric)
- campaign: number of contacts performed during this campaign and for this client
- pdays: number of days that passed by after the client was last contacted from a previous campaign
- previous: number of contacts performed before this campaign and for this client
- poutcome: outcome of the previous marketing campaign
- emp.var.rate: employment variation rate
- cons.price.idx: consumer price index
- cons.conf.idx: consumer confidence index
- euribor3m: euribor 3 month rate
- nr.employed: number of employees

Dependent Variable:
- y - has the client subscribed a term deposit? (binary: 'yes','no')

### Initial Exploratory Data Analysis
Data Summary:
<p align="center">
  <img src="https://user-images.githubusercontent.com/106714374/173241690-4aadf20b-f6ad-4bc0-bfd6-b6ad27c02ddd.png"/>
</p>

Key Variable Trends and Distributions:
<p align="center">
  <img src="https://user-images.githubusercontent.com/106714374/173241722-db18778a-8564-42c4-b626-944f9fc0dc21.png"/>
</p>

Variable Associations:
<p align="center">
  <img src="https://user-images.githubusercontent.com/106714374/173241738-4644d37a-461c-4fb2-b80d-71367d1a9bd9.png"/>
</p>

Key Observations on Distributions and Associations:
![image](https://user-images.githubusercontent.com/106714374/173241811-b4e7192a-d9c8-4c75-a590-acc027676a16.png)

Target Variable Class Ratio:
<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Class Ratio</td>
    <td>13.2% (Slightly Unbalanced)</td>
  </tr>
</table>

### Model Development and Evaluation
The current business problem at hand can be viewed as a classification problem with 2 classes. As the business would be interested in understanding/interpreting the results along with propensities ML models fit the requirement (DL models will not be used). Stack of following ML model would be test and evaluated on Precision, Recall and F1 score for final model selection. MAPE would not be used as model evaluation parameter due to presence of minor class imbalance in the data. Class balancing techniques like over sampling/undersampling will be tried out in case direct model development doesnt workout.

Model Stack:
- Logistic Regression
- Random Forest Classifier
- XGBoost
- SVM
- Decision Tree

Class Imbalance Addressal
- Oversampling
- Undersampling
Other advanced balancing techniques like SMOTE will be used incase above approached doesnt provided good model evaluation parameters

## Deployment

Streamlit application will be built with input as customer and call details and returns probabilty of customer purchasing the term plans.

## Work Distribution:

## N.Vyshnavi  
Exploratory Data Analysis

Logistic Regression

Random Forest Classifier

SVM

Decision Tree

## N.Varun
Building model XGBoost

Checking for class imbalance using over fitting and under fitting

Data visualization using streamlit

### Resources and References
- Data Source: https://archive.ics.uci.edu/ml/datasets/Bank+Marketing#
- Other References:
  - https://emiboston.com/banks-cut-marketing-spend-in-2020-but-expect-to-ramp-up-investment-in-2021/
  - https://emiboston.com/an-analysis-of-leading-u-s-banks-2018-marketing-spending/
  - https://www.business.qld.gov.au/running-business/marketing-sales/marketing-promotion/direct-marketing/using/benefits
