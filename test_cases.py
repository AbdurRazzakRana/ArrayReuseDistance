from process_dialation import predict_dialated_rf_n_loop_bound

# only inner loop for k = 2 to 4
# dict2 = {0: 35, 1: 11, 2: 37, 3: 25, 4: 5, 5: 12, 7: 4, 9: 1, 10: 2, 11: 1, -1: 13}
# dict3 = {0: 43, 1: 15, 2: 53, 3: 37, 4: 5, 5: 20, 9: 6, 12: 1, 13: 2, 14: 2, 15: 1, -1: 17}
# dict4 = {0: 51, 1: 19, 2: 69, 3: 49, 4: 5, 5: 28, 11: 8, 15: 1, 16: 2, 17: 2, 18: 2, 19:1, -1: 21}

# Predict reuse profile for k = 5
# print(dict2)
# print(dict3)
# print(dict4)
# print("Predicting for k = 5")
# predicted_rf = predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 4)
# print(predicted_rf)
# print("Actual for k = 5")

print("----->CASE 1")
code = '''
    for(k=0;k<5;k++) {
        A[0][k] = alpha * A[0][k];
        B[0][k] = alpha;
    }
}'''
print(code)
# print("Mem Trace:  ['retval', 'alpha', 'k', '[2', 'k', 'alpha', 'k', 'arrayidx1', 'k', 'arrayidx4', 'alpha', 'k', 'arrayidx1', 'k', 'k', ']', 'k']")
print()
dict2 = {0:5, 1:9, 2:5, -1:7}
dict3 = {0:7, 1:13, 2:8, -1:9}
dict4 = {0:9, 1:17, 2:11, -1:11}
print("Predicted for k = 5")
predicted_rf = predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 4)
print(predicted_rf)
print()
print("Actual for k = 5")
actual_rf = {0: 11, 1: 21, 2: 14, -1: 13}
print(actual_rf)
print()

if predicted_rf == actual_rf:
 print("\n----->TEST CASE PASSED\n")
else:
 print("\n----->TEST CASE FAILED\n")


print("\n----->CASE 2\n")
code = '''
    for(k=0;k<300;k++) {
        A[0][k] = alpha * A[0][k];
        B[0][k] = alpha;
    }
}'''
print(code)
print("Predicted for k = 300")
predicted_rf = predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 299)
print(predicted_rf)
print("Actual for k = 300")
actual_rf = {0: 601, 1: 1201, 2: 899, -1: 603}
print(actual_rf)
if predicted_rf == actual_rf:
 print("\n----->TEST CASE PASSED\n")
else:
 print("\n----->TEST CASE FAILED\n")



print("\n----->CASE 2\n")
code = '''
    for(k=0;k<300;k++) {
        A[0][k] = alpha * A[0][k];
        B[0][k] = alpha;
    }
}'''
print(code)
print("Predicted for k = 300")
predicted_rf = predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 299)
print(predicted_rf)
print("Actual for k = 300")
actual_rf = {0: 601, 1: 1201, 2: 899, -1: 603}
print(actual_rf)
if predicted_rf == actual_rf:
 print("\n----->TEST CASE PASSED\n")
else:
 print("\n----->TEST CASE FAILED\n")


print("\n----->CASE 3\n")
code = '''
    for(j=0;j<2;j++){
        for(k=0;k<300;k++) {
            A[0][k] = alpha * A[0][k];
            B[j][k] = alpha;
        }
    }
}'''
print(code)
print("Predicted for j = 2, k = 300")
dict2 = {0:15, 1:17, 2:7, 3:9, 4:2, 6:2, -1:10} # j = 2, k = 2
dict3 = {0:19, 1:25, 2:9, 3:13, 4:4, 8:3, -1:13} # j = 2, k = 3
dict4 = {0:23, 1:33, 2:11, 3:17, 4:6, 10:4, -1:16} # j = 2, k = 4
predicted_rf = predict_dialated_rf_n_loop_bound(dict2, dict3, dict4, 299)
print(predicted_rf)
print("Actual for j = 2, k = 300")
actual_rf = {0:1207, 1:2401, 2:603, 3:1201, 4:598, 602:300, -1:904} # j = 2, k = 300
print(actual_rf)
if predicted_rf == actual_rf:
 print("\n----->TEST CASE PASSED\n")
else:
 print("\n----->TEST CASE FAILED\n")