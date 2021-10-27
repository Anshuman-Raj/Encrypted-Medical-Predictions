import numpy as np
import pandas as pd
import itertools

data = pd.read_csv("data.csv")
data['obese'] = (data.Index >= 4).astype('str')
data.drop('Index', axis=1, inplace=True)

df = pd.read_csv("heart.csv")
df.dropna(inplace=True)


def gini_index(col):
    probability = col.value_counts() / col.shape[0]
    gini = 1 - np.sum(probability ** 2)
    return gini


def entropy_value(col):
    probability = col.value_counts() / col.shape[0]
    # Adding 0.000000001 to probability so that
    # in case of probability 0, log doesn't throw error
    entropy = np.sum(-probability * np.log2(probability + 1e-9))
    return entropy


def variance(column):
    if len(column) == 1:
        return 0
    else:
        return column.var()


def information_gain(dependent_variable, split_element, func=gini_index):
    split_terms = sum(split_element)
    non_split_terms = split_element.shape[0] - split_terms

    if split_terms == 0 or non_split_terms == 0:
        info_gain = 0

    else:
        if dependent_variable.dtypes != 'O':
            info_gain = variance(dependent_variable) - (
                    split_terms / (split_terms + non_split_terms) * variance(dependent_variable[split_element])) - (
                                non_split_terms / (split_terms + non_split_terms) * variance(
                            dependent_variable[-split_element]))
        else:
            info_gain = func(dependent_variable) - split_terms / (split_terms + non_split_terms) * func(
                dependent_variable[split_element]) - non_split_terms / (split_terms + non_split_terms) * func(
                dependent_variable[-split_element])

    return info_gain


def cat_opts(dependent_variable):
    dependent_variable = dependent_variable.unique()

    opts = []
    for inps in range(0, len(dependent_variable) + 1):
        for sbset in itertools.combinations(dependent_variable, inps):
            sbset = list(sbset)
            opts.append(sbset)

    return opts[1:-1]


def max_info_gain(independent_variable, dependent_variable, func=gini_index):
    split_value = []
    info_gain = []

    is_num = True if independent_variable.dtypes != 'O' else False

    # Getting the options depending on type of the variable
    if is_num:
        options = independent_variable.sort_values().unique()[1:]
    else:
        options = cat_opts(independent_variable)

    # Calculate info_gain for all values
    for val in options:
        split_element = independent_variable < val if is_num else independent_variable.isin(val)
        val_info_gain = information_gain(dependent_variable, split_element, func)
        # appending information gains to list
        info_gain.append(val_info_gain)
        split_value.append(val)

    # Check if there are more than 1 results if not, return False
    if len(info_gain) == 0:
        return None, None, None, False

    else:
        # Get results with highest IG
        best_info_gain = max(info_gain)
        info_gain_index = info_gain.index(best_info_gain)
        best_split = split_value[info_gain_index]
        return best_info_gain, best_split, is_num, True


def get_split(col, dataframe):
    split_values = dataframe.drop(col, axis=1).apply(max_info_gain, dependent_variable=dataframe[col])
    if sum(split_values.loc[3, :]) == 0:
        return None, None, None, None

    else:
        # the terms that can be used to split dataframe
        split_values = split_values.loc[:, split_values.loc[3, :]]

        # Finding split terms
        split_var = max(split_values)
        split_value = split_values[split_var][1]
        info_gain = split_values[split_var][0]
        is_num = split_values[split_var][2]

    return split_var, split_value, info_gain, is_num


def set_split(variable, value, dataframe, is_num):
    if is_num:
        data_l = dataframe[dataframe[variable] < value]
        data_r = dataframe[(dataframe[variable] < value) == False]

    else:
        data_l = dataframe[dataframe[variable].isin(value)]
        data_r = dataframe[(dataframe[variable].isin(value)) == False]

    return data_l, data_r


def predictions(dataframe, is_target):
    # for predicting the results
    if is_target:
        prediction = dataframe.value_counts().idxmax()
    else:
        prediction = dataframe.mean()

    return prediction


def train(dataframe, dependent_variable, target_name, max_depth=None, min_samples_split=None,
          min_information_gain=1e-20, counter=0,
          max_cat=20):
    # Checking max_cat when it's first iteration
    if counter == 0:
        types = dataframe.dtypes
        check_columns = types[types == "object"].index
        for column in check_columns:
            var_length = len(dataframe[column].value_counts())
            if var_length > max_cat:
                raise ValueError("There are too many categories")

    # if max depth is within limits
    if max_depth is None:
        depth_condition = True

    else:
        if counter < max_depth:
            depth_condition = True

        else:
            depth_condition = False

    # if minimum sample split is valid
    if min_samples_split is None:
        sample_condition = True

    else:
        if dataframe.shape[0] > min_samples_split:
            sample_condition = True

        else:
            sample_condition = False

    # if max depth is minimum sample conditions are met
    if depth_condition & sample_condition:

        variable, value, info_gain, variable_type = get_split(dependent_variable, dataframe)

        # If information gained is sufficient
        if info_gain is not None and info_gain >= min_information_gain:

            counter += 1

            left_dataframe, right_dataframe = set_split(variable, value, dataframe, variable_type)

            # root is done now moving to sub trees
            split_type = "<=" if variable_type else "in"
            check_condition = "{} {}  {}".format(variable, split_type, value)
            # check_condition for appending split terms
            subtree = {check_condition: []}

            # Using head recursion to find the split values for different variables
            yes_node = train(left_dataframe, dependent_variable, target_name, max_depth, min_samples_split,
                             min_information_gain, counter)

            no_node = train(right_dataframe, dependent_variable, target_name, max_depth, min_samples_split,
                            min_information_gain, counter)

            if yes_node == no_node:
                subtree = yes_node

            else:
                subtree[check_condition].append(yes_node)
                subtree[check_condition].append(no_node)

        # If information gain is not sufficient
        else:
            pred = predictions(dataframe[dependent_variable], target_name)
            return pred

    # if max depth exceeds
    else:
        pred = predictions(dataframe[dependent_variable], target_name)
        return pred
    # returning the subtree of split values
    return subtree


max_depth = 25
min_samples_split = 20
min_information_gain = 1e-15

decisions = train(df, 'target', True, max_depth, min_samples_split, min_information_gain)

print(decisions)

### Training part is complete here
### Now predicting part will come into action

##Prediction making function


def classifier(observations, hash_map_set):
    # using the dictionary of split terms
    # predictions on the data will be made
    chcek_condition = list(hash_map_set.keys())[0]

    if chcek_condition.split()[1] == '<=':

        if observations[chcek_condition.split()[0]] <= float(chcek_condition.split()[2]):
            answer = hash_map_set[chcek_condition][0]
        else:
            answer = hash_map_set[chcek_condition][1]

    else:

        if observations[chcek_condition.split()[0]] in (chcek_condition.split()[2]):
            answer = hash_map_set[chcek_condition][0]
        else:
            answer = hash_map_set[chcek_condition][1]

    # If the answer is constant
    if not isinstance(answer, dict):
        return answer
    else:
        residual_tree = answer
        return classifier(observations, answer)


print(classifier(df.iloc[212,:13],decisions))
print(df.iloc[212,:])