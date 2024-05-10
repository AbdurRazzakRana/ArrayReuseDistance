from predict_n_list import generate_n_list

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

def predict_dialated_rf_n_loop_bound(dict1, dict2, dict3, n):
     common_rds = set(dict1.keys()) & set(dict2.keys()) & set(dict3.keys())

     common_rds_count, unique_rds, unique_rds_count = process_cluster_data(common_rds, dict1, dict2, dict3)
     


     print(common_rds_count)
     print(unique_rds)
     print(unique_rds_count)


# rd_list = generate_n_list(list1, list2, list3, n)
# print(rd_list)