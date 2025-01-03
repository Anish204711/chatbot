
def split_list_with_overlap(input_list, num_parts, overlap):
    # Calculate the length of each part without the overlap
    part_length = (len(input_list) - overlap * (num_parts - 1)) // num_parts
    result = []
    
    # Generate each part with overlap
    for i in range(num_parts):
        start_index = i * (part_length - overlap)
        end_index = start_index + part_length + overlap
        result.append(input_list[start_index:end_index])
    
    return result



def data_prep():
    with open("data/data.txt", "r", encoding="utf-8") as file:
        text = file.read()


    text=text.replace(",", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace(".", "").replace(":", "").replace('"', '')
    text=text.replace("'", "").replace("(", "").replace(")", "").replace("?", "").replace("!", "")
    word_list = text.split()
    
    word_list = text.split()
    word_list=split_list_with_overlap(word_list,200,20)

    return word_list








