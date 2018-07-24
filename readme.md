# actor_contribution_analysis
Using Multivariate Linear Regression（MLR）to evaluate the contribution of actors towards film boxoffice and rating.

## main code
* AHP_analysis.py

analyze whether the factors are consistent with the result
(To be honest, AHP is too dependent on human identification, so I think it may lack of convincing)

* mongo_data_extract.py

operate mongodb to extract some data

* txt_to_libsvm.py

turn the txt file to libsvm

* linear_models.py

linear models I use to see whether it work or not

* traing_model.py	

train the model to fit the data

* Ltp_NameRecognition.py

use pyltp to extract actor's name in the reviews in order to compute one of the factors
