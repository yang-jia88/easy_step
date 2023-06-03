import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV


train_data = pd.read_csv("train.csv")
print(train_data.shape)
# train_data.head(3)
test_data = pd.read_csv("test.csv")
# print(train_data.shape)

# women = train_data.loc[train_data.Sex == 'female']["Survived"]
# rate_women = sum(women)/len(women)

# print("% of women who survived:", rate_women)


y = train_data["Survived"]

# train_data['Age'].isna().sum()
# train_data = train_data.fillna(train_data.median())

features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

model = RandomForestClassifier(n_estimators=71, max_depth=3, random_state=1,max_features=1)
model.fit(X, y)
predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('fourth.csv', index=False)



# param_test1= {'n_estimators':range(10,201,10)}

# gsearch1= GridSearchCV(estimator = RandomForestClassifier(min_samples_split=100,

# min_samples_leaf=20,max_depth=8,max_features='sqrt' ,random_state=10),

# param_grid =param_test1, scoring='roc_auc',cv=5)

# gsearch1.fit(X,y)

# print(gsearch1.best_params_, gsearch1.best_score_)

# param_test1 = {"n_estimators":range(1,101,10)}
# gsearch1 = GridSearchCV(estimator=RandomForestClassifier(),param_grid=param_test1,
#                         scoring='roc_auc',cv=10)
# gsearch1.fit(X,y)

# # print(gsearch1.grid_scores_)
# print(gsearch1.best_params_)
# print("best accuracy:%f" % gsearch1.best_score_)

# param_test2 = {"max_features":range(1,11,1)}
# gsearch1 = GridSearchCV(estimator=RandomForestClassifier(n_estimators=71,
#                         random_state=1),
#                         param_grid = param_test2,scoring='roc_auc',cv=10)
# gsearch1.fit(X,y)
# # print(gsearch1.grid_scores_)
# print(gsearch1.best_params_)
# print('best accuracy:%f' % gsearch1.best_score_)