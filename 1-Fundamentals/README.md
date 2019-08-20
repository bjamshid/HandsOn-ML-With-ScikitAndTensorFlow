Example ML use-cases:

	- Segment customers and find the best marketing strategy for each group
	- Recommend products for each client based on what similar clients bought
	- Detect which transactions are likely to be fraudulent
	- Predict next year's revenue
	- More: kaggle.com/wiki/DataScienceUseCases

ML Definition:
	A computer program is said to learn from experience E with respect to some task T and some performance
	measure P, if its performance on T, as measured by P, imporves with Exprerience E. -T.M 1997

ML is great for:

	- Problems for which existing solutions require a lot of hand-tuning or long list of rules (ML can
	simplify code and perform better)
	- Complex problems for which there is no good solution at all using a traditional approach.
	- Fluctuating environment where an algorithm needs to adapt to new data.
	- Getting insight about complex problems and/or big data

Types of ML systems (can be combined):
	- Supervised/Unsupervised/Semisupervised/Reinforcement Learning

		- Supervised learining: training data includes the desired solutions(feature+label in data set)
		Examples: 
			- K-nearest neighbours
			- linear regression
			- logistic regression
			- SVMs
			- decision trees and random forests
			- neural networks

		- Unsupervised learning: training data is unlabeled.
		Examples:
			- clustering: k-means, hierarchical cluster analysis 'HCA', expectation maximazation
			- visualization and dimentionality reduction: principal component analysis, kernel PCA, locality-linear embedding 'LLE',
			t-distributed stochastic neighbour embedding 't-SNE'
			- association rule learning: Apriori, Eclat

		- Unsupervised learning: partially labeled trainig data, or combination of supervised & unsupervised algorithms(e.g.: photo hosting services)
		Examples:
			- deep belief networks 'DBNs' (based on stacked RBMs)

		- Reinforcement Learning: an agent observes the environment and select/perform the action and gets reward/penalty in return (results in learning a policy/strategy by agent)

	- Batch/Online Learining:

		- Batch: system is trained using all the available data (done offline - no learning in production)
		- Online: system is trained sequentially and can adapt to new data (learning rate)

	- Instance/Model based learning

		- Instance: system learns the examples by heart and generalizes to new input using a similarity measure
		- Model: model is built using examples and used to make predictions

