## CS 4641 Project Proposal: Predicting NBA Player Performance Post-Injury

### Intro/Background:
In professional basketball, determining when an injured player should return to the team is often a difficult decision that involves conflicting interests. Team pressure may lead to a premature return to action by the player, putting them in a compromised position physically. On the other hand, the player may want more time for recovery than necessary in an attempt to nullify the risk of re-injury and secure their financial future. Across 3 seasons, 56.8% of players have at least 1 game-preventing injury (Lewis, 2018). This indicates the frequency of the dilemma between returning or resting.

### Problem Definition:
To lessen the divide between the conflicting interests of the team and the player, this project will formulate a model that predicts whether or not a player will re-aggravate a previous injury. This predictive model will allow both the team and the player to make more educated decisions regarding the amount of treatment needed for certain injuries.

### Data Collection:
Two sets of data were obtained: one with NBA injury data from 2010 to 2020 and one with attributes (height, weight, birth date, etc.) for all NBA players from 1950 to 2018. Both data sets contain information retrieved from basketball-reference.com and prosportstransactions.com, which seem to be the go-to sources for NBA statistics. Additionally, sample entries from both these data sets are shown below.


![Data 1](/docs/assets/DataCollection1.png)

![Data 2](/docs/assets/DataCollection2.png)

Creating a final conglomerate data set took a few steps. First, the player attribute data set was significantly reduced to include only desired player attributes from 2010 onwards. Then, this player attribute data was paired with each injury data entry to get entries such as the example entries shown below.

![Data 3](/docs/assets/DataCollection3.png)

The “injury type” column gives the numerical encoding of the injury the player sustained. In the entries above, “7” denotes a left knee injury. Additional data was ascertained from the original data sets, such as that seen in the “reinjured” and “times previously injured” columns. The “reinjured” column gives a Boolean output that represents whether or not the player sustained the same injury in the following year. Additionally, the “times previously injured” column gives the number of the times previously that the player sustained that injury. For example, Kemba Walker had 7 previous left knee injuries before sustaining another knee injury on March 27th, 2021.

### Methods:
The first step was to clean the data as described in the first section. Next, we used principal component analysis to reduce the number of features in our dataset. This reduced the overall size of our data so as to make the learning process for the models more efficient, and more importantly, PCA captures features (dimensions) of the data set that are highly correlated, which eliminates noise created by less relevant features. Additionally, we performed a parametric study comparing the level of dimensional reduction performed on the data to the accuracy of the resultant  neural network.

For the first set of neural networks, we varied the dimensionality of the input data from 6 to 1 and trained 6 different neural networks, each using a data set of different dimension. The first neural network of this set will be described subsequently, but it should be noted that, except for the dimension of the input data, all other features described are consistent across all 6 neural networks in this set. The first NN had 6 inputs: days missed due to injury, injury type, age, height, weight, and times previously reinjured. The output is a 0 or 1 for whether the player will be reinjured (1) or not (0) within a year of the current injury. The 2 layers are fully connected. The first layer has 12 nodes and the second has 5 nodes. We chose the output layer to use a sigmoid activation function because our output is 0 or 1, and the model uses cross entropy as our loss function for binary classification. The accuracy of this model is based on the binary cross-entropy metric from Keras.

For our last neural network, we tried to predict the number of days a player would miss due to injury. This model had 5 inputs: past days missed due to injury, injury type, age, height, and weight. The output is the number of days the player misses due to injury. For the model’s structure, the first layer has 25 nodes and the second has 10 nodes. The output layer uses a linear activation function, and the model uses MSE as our loss function. 

As an additional regression model that did not use Neural Networks, we also used Support Vector Classifiers to classify the data. We used a radial basis function as a kernel for the SVM and set the regularization parameter  to 0.1. Though our data is not relatively big, we shrunk the amount of injured entries to match the number of non-injured entries to best serve the model (N = 340).

### Results/General Discussion:
In our parametric study of dimensional reduction, we consider optimal neural network training to be training that takes a minimal number of epochs to reach minimal loss.  As can be seen from the six graphs below, training the neural network was closest to optimal when the dimension of the data set was reduced to either 2 or 3 dimensions. This matches expectation since PCA using 3 components gives explained variance ratios of approximately 0.622, 0.356, and 0.014 for the 3 respective selected components, meaning in layman’s terms that these selected components explained about 99.2% of the variance in the data set. Since the third component only explains 1.4% of the variance in the data, it makes sense that the reduction of the data to 2 dimensions also leads to good performance when training the neural network.

![Data 4](/docs/assets/epochs6-5.png)
![Data 4](/docs/assets/epochs4-3.png)
![Data 4](/docs/assets/epochs2-1.png)

The first NN produced an average of 77.26% accuracy across 5 trials. Even after changing the number of nodes, trying different activation functions in the layers, and changing the number of epochs, the accuracy usually remained around 77%. The leftmost graph in the figure above shows the loss over epochs for all 6 inputs mentioned in the Methods section. 

The other graphs in the figure above apply PCA to reduce the number of features for the same NN. For example, the graph in the top right reduces the number of inputs from 6 to 5. Even after applying PCA and testing models with reduced features, the accuracy for the models still remained around the same (77%). It may be possible that all of the models are converging to a simple rule. The model however is an improvement from randomly guessing.

The second NN model uses linear regression to predict the number of days a player will be out based on an injury. The loss during the testing phase was large and did not follow that from the training phase. We believe that the problem with the model comes from attempting to predict an output based on unrelated inputs. We determined that the type and severity of the injury are the main determining factors of how many days needed to recover. Our model does not represent those inputs as well. The loss versus epochs graph for this model is shown below.

![Data 5](/docs/assets/loss_over_epochs2.png)

For the SVM, the accuracy reached up to 88% correctness for labeling both injured and non-injured players. Here are the labels for all data points:

![Data 6](/docs/assets/svm.png)

Even with evenly distributed non-reinjured and reinjured data points, the model leaned towards classifying players as not likely to be re-injured, which in  general the majority of players were. The model may be better served by training on a greater amount of reinjured entries so that it can more correctly identify them, as we currently have entries in the hundreds. Obviously our sample size is limited by the number of NBA injuries that happen, which is a relatively small number, so we could expand to other basketball leagues, in order to have a more complete model where reinjury is more aptly predicted.  


### References:
Lewis, M. (2018). It’s a Hard-Knock Life: Game Load, Fatigue, and Injury Risk in the National Basketball Association. Journal of Athletic Training, 53(5), 503–509. https://doi.org/10.4085/1062-6050-243-17
