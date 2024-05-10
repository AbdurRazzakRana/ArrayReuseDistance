from predict_n_list import generate_n_list
from predict_n_list import generate_dynamic_rd_count_list

def process_cluster_data(common_rds, dict1, dict2, dict3):
     common_rds_count= []
     unique_rds = []
     unique_rds_count = []
     
     # prepare reuse distnce counts for the common reuse distnses
     list1_common_rd_counts = []
     list1_unique_rds = []
     list1_unique_rd_counts = []
     for key, value in dict1.items():
          if key in common_rds:
               list1_common_rd_counts.append(value)
          else:
               list1_unique_rds.append(key)
               list1_unique_rd_counts.append(value)

     common_rds_count.append(list1_common_rd_counts)
     unique_rds.append(list1_unique_rds)
     unique_rds_count.append(list1_unique_rd_counts)


     list2_common_rd_counts = []
     list2_unique_rds = []
     list2_unique_rd_counts = []
     for key, value in dict2.items():
          if key in common_rds:
               list2_common_rd_counts.append(value)
          else:
               list2_unique_rds.append(key)
               list2_unique_rd_counts.append(value)

     common_rds_count.append(list2_common_rd_counts)
     unique_rds.append(list2_unique_rds)
     unique_rds_count.append(list2_unique_rd_counts)

     list3_common_rd_counts = []
     list3_unique_rds = []
     list3_unique_rd_counts = []
     for key, value in dict3.items():
          if key in common_rds:
               list3_common_rd_counts.append(value)
          else:
               list3_unique_rds.append(key)
               list3_unique_rd_counts.append(value)

     common_rds_count.append(list3_common_rd_counts)
     unique_rds.append(list3_unique_rds)
     unique_rds_count.append(list3_unique_rd_counts)

     return common_rds_count, unique_rds, unique_rds_count

def gen_rf_from_output_data(common_rds, dict1, common_rds_count_predicted, unique_rds_predicted, unique_rds_count_predicted):
     ans_dict={}
     i=0
     j=0
     # -1 reuse distance will be last
     for key, value in dict1.items():
          if key in common_rds and key != -1:
               ans_dict[key] = common_rds_count_predicted[i]
               i+=1
     if unique_rds_predicted:
          for index, val in enumerate(unique_rds_predicted):
               ans_dict[val] = unique_rds_count_predicted[index]
     
     ans_dict[-1] = common_rds_count_predicted[i]
     return ans_dict

def predict_dialated_rf_n_loop_bound(dict1, dict2, dict3, n):
     common_rds = set(dict1.keys()) & set(dict2.keys()) & set(dict3.keys())

     common_rds_count, unique_rds, unique_rds_count = process_cluster_data(common_rds, dict1, dict2, dict3)
     common_rds_count_predicted = generate_n_list(common_rds_count, n)
     # Only calculte unique ids if they have
     rd_not_changing = all(not sublist for sublist in unique_rds)
     if not rd_not_changing:
          unique_rds_predicted = generate_n_list(unique_rds, n)
     if not rd_not_changing:
          unique_rds_count_predicted = generate_dynamic_rd_count_list(unique_rds_count, n)
     # print(unique_rds_count_predicted)

     if not rd_not_changing:
          rf = gen_rf_from_output_data(common_rds, dict1, common_rds_count_predicted, unique_rds_predicted, unique_rds_count_predicted)

     else:
          rf = gen_rf_from_output_data(common_rds, dict1, common_rds_count_predicted, [], [])

     return rf
# print(rd_list)