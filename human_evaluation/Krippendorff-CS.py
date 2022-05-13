import krippendorff
import numpy as np
import pandas as pd

# factual1 relevant1 fluent1 factual2 relevant2 fluent2 factual3 relevant3 fluent3
def convert_list(df, a, b):
    ans = []
    ans.extend(df[a].to_list())
    ans.extend(df[b].to_list())
    # ans.extend(df[c].to_list())
    return ans

def main():
    df_Long = pd.read_csv("./Long-CS.csv")
    df_Shankar = pd.read_csv("./Shankar-CS.csv")
    df_Tan = pd.read_csv("./JQ-CS.csv")

    factual_Long = convert_list(df_Long, "coverage2", "coverage3")
    factual_Shankar = convert_list(df_Shankar, "coverage2", "coverage3")
    factual_Tan = convert_list(df_Tan, "coverage2", "coverage3")
    factual = [factual_Long, factual_Shankar, factual_Tan]
    print("Krippendorff's alpha for ordinal metric, CS: ", krippendorff.alpha(reliability_data=factual,
                                                                          level_of_measurement="ordinal"))
    
    # re_Long = convert_list(df_Long, "relevant1", "relevant2", "relevant3")
    # re_Shankar = convert_list(df_Shankar, "relevant1", "relevant2", "relevant3")
    # re_Tan = convert_list(df_Tan, "relevant1", "relevant2", "relevant3")
    # re = [re_Long, re_Shankar, re_Tan]
    # print("Krippendorff's alpha for ordinal metric, Relevance: ", krippendorff.alpha(reliability_data=re,
    #                                                                       level_of_measurement="ordinal"))
    
    # fl_Long = convert_list(df_Long, "fluent1", "fluent2", "fluent3")
    # fl_Shankar = convert_list(df_Shankar, "fluent1", "fluent2", "fluent3")
    # fl_Tan = convert_list(df_Tan, "fluent1", "fluent2", "fluent3")
    # fl = [fl_Long, fl_Shankar, fl_Tan]
    # print("Krippendorff's alpha for ordinal metric, Fluency: ", krippendorff.alpha(reliability_data=fl, level_of_measurement="ordinal"))
    
    # Long = factual_Long
    # Long.extend(re_Long)
    # Long.extend(fl_Long)

    # Tan = factual_Tan
    # Tan.extend(re_Tan)
    # Tan.extend(fl_Tan)

    # Shankar = factual_Shankar
    # Shankar.extend(re_Shankar)
    # Shankar.extend(fl_Shankar)

    # print("Krippendorff's alpha for ordinal metric, Overall: ", krippendorff.alpha(reliability_data=[Long, Tan, Shankar],
    #                                                                     level_of_measurement="ordinal"))
if __name__ == '__main__':
    main()