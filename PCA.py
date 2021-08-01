# Feature Extraction with PCA
import numpy
from pandas import read_csv
from sklearn.decomposition import PCA
# load data

fieldnames = ['name','injury date','return date','days missed','injury type','age', 'height', 'weight',
                'times previously injured', 'reinjured']
dataframe = read_csv("combined_data.csv", names=fieldnames)
array = dataframe.values
X = array[1:,3:9] # 6 features: days missed, injury type, age, height, weight, times previously injured
Y = array[1:,9]   # boolean output: reinjuried within a year
# feature extraction
pca = PCA(n_components=5)
fit = pca.fit(X)
transformed_fit =pca.fit_transform(X)
# summarize components
print("Explained Variance: %s" % fit.explained_variance_ratio_)
print("Singular Values: %s" % fit.singular_values_)
print(fit.components_)