from process_dialation import predict_dialated_rf_n_loop_bound

# only inner loop for k = 2 to 4
dict2 = {0: 35, 1: 11, 2: 37, 3: 25, 4: 5, 5: 12, 7: 4, 9: 1, 10: 2, 11: 1, -1: 13}
dict3 = {0: 43, 1: 15, 2: 53, 3: 37, 4: 5, 5: 20, 9: 6, 12: 1, 13: 2, 14: 2, 15: 1, -1: 17}
dict4 = {0: 51, 1: 19, 2: 69, 3: 49, 4: 5, 5: 28, 11: 8, 15: 1, 16: 2, 17: 2, 18: 2, 19:1, -1: 21}
# Predict reuse profile for k = 5
predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 5)