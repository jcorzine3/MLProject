# Feature Extraction with PCA
import numpy
from pandas import read_csv
from sklearn.decomposition import PCA
# load data


def pca(n_components):
    fieldnames = ['name', 'injury date', 'return date', 'days missed', 'injury type', 'age', 'height', 'weight',
                  'times previously injured', 'reinjured']
    dataframe = read_csv("combined_data.csv", names=fieldnames)
    array = dataframe.values
    # 6 features: days missed, injury type, age, height, weight, times previously injured
    X = array[1:, 3:9]
    Y = array[1:, 9:]   # boolean output: reinjuried within a year

    # feature extraction
    pca = PCA(n_components)
    fit = pca.fit(X)
    transformed_fit = pca.fit_transform(X)
    # summarize components
    print(transformed_fit.shape)
    print("Explained Variance: %s" % fit.explained_variance_ratio_)
    print("Singular Values: %s" % fit.singular_values_)
    print(fit.components_)

    return transformed_fit
