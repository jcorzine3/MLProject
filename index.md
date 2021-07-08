## CS 4641 Project Proposal: Predicting NBA Player Performance Post-Injury

### Intro/Background:
In professional basketball, determining when an injured player should return to the team is often a difficult decision that involves conflicting interests. Team pressure may lead to a premature return to action by the player, putting them in a compromised position physically. On the other hand, the player may want more time for recovery than necessary in an attempt to nullify the risk of re-injury and secure their financial future. Across 3 seasons, 56.8% of players have at least 1 game-preventing injury (Lewis, 2018). This indicates the frequency of the dilemma between returning or resting.

### Problem Definition:
To lessen the divide between the conflicting interests of the team and the player, this project will formulate two models: one that predicts player performance post-injury and one that predicts whether or not a player will re-aggravate a previous injury. These predictive models would allow both the team and the player to make more educated decisions regarding the amount of treatment needed for certain injuries.

### Data Collection:
Two data sets were used for the models below: one with NBA injury data from 2010 to 2020 and one with attributes (height, weight, birth date, etc.) for all NBA players from 1950 to 2018. Both data sets contain information retrieved from basketball-reference.com and prosportstransactions.com, which seem to be the go-to sources for NBA statistics. Additionally, sample entries from both these data sets are shown below.

![Data 1](/docs/assets/DataCollection1.png)

![Data 2](/docs/assets/DataCollection2.png)

Creating a final conglomerate data set took a few steps. First, the player attribute data set was significantly reduced to include only desired player attributes from 2010 onwards. Then, this player attribute data was paired with each injury data entry to get entries such as the example entries shown below.

![Data 3](/docs/assets/DataCollection3.png)

The “injury type” column gives the numerical encoding of the injury the player sustained. In the entries above, “7” denotes a left knee injury. Additional data was ascertained from the original data sets, such as that seen in the “reinjured” and “times previously injured” columns. The “reinjured” column gives a Boolean output that represents whether or not the player sustained the same injury in the following year. Additionally, the “times previously injured” column gives the number of the times previously that the player sustained that injury. For example, Kemba Walker had 7 previous left knee injuries before sustaining another knee injury on March 27th, 2021.

### Methods:
The first step was to clean the data as described in the first section. We generated two neural networks (NNs). The first NN had 6 inputs: days missed due to injury, injury type, age, height, weight, and times previously reinjured. The output is a 0 or 1 for whether the player will be reinjured (1) or not (0). The 2 layers are fully connected. The first layer has 12 nodes and the second has 5 nodes. We chose the output layer to use a sigmoid activation function because our output is 0 or 1. The model uses cross entropy as our loss function for binary classification. The accuracy of this model based on the binary cross-entropy metric from Keras produced an average of 77.26 across 5 trials.

### Results/General Discussion:
As of right now, our neural network predicts re-injury within a year with an average accuracy of 77%, but we believe this can be improved upon in the future by treating each of the injury types separately, changing activation functions, and modifying the number of nodes per layer. Overall, this is a decent start to the project with regards to accuracy, but we would like to improve on this and also (time permitting) create a model that predicts change in performance after injury. 

![Data 4](/docs/assets/loss_over_epochs.png)

We experimented with another NN model that used linear regression to predict the number of days a player will be out based on an injury. However, the loss during the testing phase was larger and did not follow that from the training phase. Thus, we have excluded it from this report and plan on improving it for the final report. We believe that the injury types input is messing with the intended output.