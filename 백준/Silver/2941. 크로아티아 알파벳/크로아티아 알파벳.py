import re

croatia = input()
output_croatia = re.sub(r"=", "", croatia)
output_croatia = re.sub(r"-", "", output_croatia)
# print(output_croatia)
croatia_list = list(map(str, output_croatia))
croatia_origin_list = list(map(str, croatia))
# print(croatia_list)

except_num = 0

for i in range(len(croatia_list) - 1):
    sample_list = croatia_list[i : (i + 2)]
    # print(sample_list)
    # if "d" in sample_list:
    #     if "z" in sample_list:
    #         if sample_list.index("d") == (sample_list.index("z") - 1):
    #             except_num += 1
    #     else:
    #         except_num += 0

    if "l" in sample_list:
        if "j" in sample_list:
            if sample_list.index("l") == (sample_list.index("j") - 1):
                except_num += 1
        else:
            except_num += 0

    elif "n" in sample_list:
        if "j" in sample_list:
            if sample_list.index("n") == (sample_list.index("j") - 1):
                except_num += 1
        else:
            except_num += 0

    else:
        except_num += 0

# print(except_num)

for i in range(len(croatia_origin_list) - 2):
    sample_list = croatia_origin_list[i : (i + 3)]
    # print(sample_list)
    if "d" in sample_list:
        if "z" in sample_list:
            if "=" in sample_list:
                if sample_list.index("d") == (sample_list.index("z") - 1):
                    if sample_list.index("z") == (sample_list.index("=") - 1):
                        except_num += 1
    else:
        except_num += 0

# print(except_num)

# print(len(croatia_list))
print(len(croatia_list) - except_num)
