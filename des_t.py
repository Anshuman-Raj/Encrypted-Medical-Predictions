from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from sklearn.tree import export_text, _tree

df = pd.read_csv('heart.csv')
x_train, x_test, y_train, y_test = train_test_split(df.iloc[1:, :13], df.iloc[1:, 13], test_size=0.2, random_state=12)
classifier = DecisionTreeClassifier(max_depth=9)
classifier.fit(x_train, y_train)
pred = classifier.predict(x_test)
feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
                 'ca', 'thal']

decision_tree = export_text(classifier, feature_names=feature_names)
print(decision_tree)
# print(pred[2:8])
print(accuracy_score(y_test, pred))


def tree_to_code(tree, feature_names=feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    print("def predict(conditions, result):")
    # print("\tconditions_ckecklist = []\n\tresults_list = []")

    def recursion(node, depth,i=[0],j=[0]):
        indent = "\t" * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            # print("\tconditions_checklist.append({} - {})".format(name, np.round(threshold, 2)))
            print("{}if conditions[{}] <= 0:".format(indent, max(j)))
            j.append(max(j)+1)
            i,j = recursion(tree_.children_left[node], depth + 1, i, j)
            print("{}else:  # condition is false".format(indent))
            i,j = recursion(tree_.children_right[node], depth + 1, i, j)
        else:
            print("{}return result[{}].index(max(result[{}]))".format(indent, max(i), max(i)))
            i.append(max(i)+1)
            # print("\tresults_list.append({})".format(tree_.value[node][0]))
        return i, j
    recursion(0, 1)


tree_to_code(classifier)
