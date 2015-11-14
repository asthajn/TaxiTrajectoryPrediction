import csv
import readValidate
from validation import Validation

try:
    f = open('../preprocessed_data/probabilities.txt', 'rb')
    h = open('../preprocessed_data/hops.txt', 'rb')
except IOError:
	print "No probabilities to validate "
    f.close()
    return
else:
    prob = pickle.load(f)
    hops = pickle.load(h)
    f.close()
    h.close()

shouldBeResult = readValidate.read("../data/validate.csv")

results = Validation()
results.validation(shouldBeResult,prob,hops)