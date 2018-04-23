import pandas as pd
import numpy as np
from scipy.stats import norm

def split_data(data, percent_train):
    split_idx = int(data.shape[0] * percent_train)
    return data.iloc[0:split_idx, :].copy(), data.iloc[split_idx:, :].copy()

def get_py(groups):
    p_y = np.empty(len(groups.groups))

    for i, g in enumerate(groups.groups):
        p_y[i] = len(groups.get_group(g)) / len(groups.groups)
    return p_y

def get_models(groups):
    models = []
    for i, g in enumerate(groups.groups):
        curr_group = groups.get_group(g).copy()
        curr_group.drop(columns='class', inplace=True)
        curr_models = []
        for col in curr_group.columns:
            curr_models.append(norm.fit(curr_group[col]))
        models.append(curr_models)
    return models

def predict(test_data, groups, models):
    p_y = get_py(groups)
    
    predictions = np.empty(test_data.shape[0])

    for idx, row in enumerate(test_data.values.tolist()):
        curr_prediction = np.empty((len(groups.groups), len(row)))
        for i, g in enumerate(groups.groups):
            for j in range(len(row)):
                curr_prediction[i][j] = norm.logpdf(row[j], loc=models[i][j][0], scale=models[i][j][1])
        p_x_y = np.sum(curr_prediction, axis=1)
        predictions[idx] = np.argmax(p_x_y + np.log(p_y))
    return predictions

def score(predictions, test_data_labels):
    return (1 - (np.sum(1*(predictions != np.array(test_data_labels['class']).flatten())) / test_data.shape[0]))

if __name__ == "__main__":

	data = pd.read_csv('pima-indians-diabetes.data')
	train_data, test_data = split_data(data, .8)

	groups = train_data.groupby('class')
	test_data_labels = pd.DataFrame(test_data['class'])
	test_data.drop(columns='class', inplace=True)

	models = get_models(groups)
	predictions = predict(test_data, groups, models)
	print("Score: " + str(score(predictions, test_data_labels)))