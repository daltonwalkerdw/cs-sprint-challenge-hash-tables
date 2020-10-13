
def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {weight: index for index, weight in enumerate(weights)}

    for index, weight in enumerate(weights):
        difference = limit - weight
        if difference in weight_dict:
            if index > weight_dict[difference]:
                print("curr_indexinx", index, weight_dict[difference])
                return(index, weight_dict[difference])
            else:
                return (weight_dict[difference], index)



