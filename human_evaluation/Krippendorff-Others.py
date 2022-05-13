import krippendorff
import numpy as np
import pandas as pd

# factual1 relevant1 fluent1 factual2 relevant2 fluent2 factual3 relevant3 fluent3
def convert_list(df, a, b, c):
    ans = []
    ans.extend(df[a].to_list())
    ans.extend(df[b].to_list())
    ans.extend(df[c].to_list())
    return ans

def convert_to_list_CS(df, _, b, c):
    ans = []
    ans.extend([5]*150)
    ans.extend(df[b].to_list())
    ans.extend(df[c].to_list())
    return ans

def main():
    df_Long = pd.read_csv("./Long-Others.csv")
    df_Shankar = pd.read_csv("./Shankar-Others.csv")
    df_Tan = pd.read_csv("./JQ-Others.csv")

    factual_Long = convert_list(df_Long, "factual1", "factual2", "factual3")
    factual_Shankar = convert_list(df_Shankar, "factual1", "factual2", "factual3")
    factual_Tan = convert_list(df_Tan, "factual1", "factual2", "factual3")
    factual = [factual_Long, factual_Shankar, factual_Tan]
    print("Krippendorff's alpha for ordinal metric, Factual: ", krippendorff.alpha(reliability_data=factual,
                                                                          level_of_measurement="ordinal"))
    
    re_Long = convert_list(df_Long, "relevant1", "relevant2", "relevant3")
    re_Shankar = convert_list(df_Shankar, "relevant1", "relevant2", "relevant3")
    re_Tan = convert_list(df_Tan, "relevant1", "relevant2", "relevant3")
    re = [re_Long, re_Shankar, re_Tan]
    print("Krippendorff's alpha for ordinal metric, Relevance: ", krippendorff.alpha(reliability_data=re,
                                                                          level_of_measurement="ordinal"))
    
    fl_Long = convert_list(df_Long, "fluent1", "fluent2", "fluent3")
    fl_Shankar = convert_list(df_Shankar, "fluent1", "fluent2", "fluent3")
    fl_Tan = convert_list(df_Tan, "fluent1", "fluent2", "fluent3")
    fl = [fl_Long, fl_Shankar, fl_Tan]
    print("Krippendorff's alpha for ordinal metric, Fluency: ", krippendorff.alpha(reliability_data=fl, level_of_measurement="ordinal"))
    
    Long = factual_Long
    Long.extend(re_Long)
    Long.extend(fl_Long)
    df_cs_Long = pd.read_csv("./Long-CS.csv")
    cs_Long = convert_to_list_CS(df_cs_Long, '_', 'coverage2', 'coverage3')
    Long.extend(cs_Long)

    Tan = factual_Tan
    Tan.extend(re_Tan)
    Tan.extend(fl_Tan)
    df_cs_JQ = pd.read_csv("./JQ-CS.csv")
    cs_JQ = convert_to_list_CS(df_cs_JQ, '_', 'coverage2', 'coverage3')
    Tan.extend(cs_JQ)

    Shankar = factual_Shankar
    Shankar.extend(re_Shankar)
    Shankar.extend(fl_Shankar)
    df_cs_Shankar = pd.read_csv("./Shankar-CS.csv")
    cs_Shankar = convert_to_list_CS(df_cs_Shankar, '_', 'coverage2', 'coverage3')
    Shankar.extend(cs_Shankar)

    print("Krippendorff's alpha for ordinal metric, Overall: ", krippendorff.alpha(reliability_data=[Long, Tan, Shankar],
                                                                         level_of_measurement="ordinal"))
if __name__ == '__main__':
    main()

