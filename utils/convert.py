def convert_file():
    file = open("cnab_files/CNAB.txt", "r")
    file_read = file.readlines()
    new_file = []
    for data in file_read: 
        new_data = {}
        new_data["type"] = data[0]
        new_data["date"] = f"{data[1:5]}-{data[5:7]}-{data[7:9]}"
        new_data["value"] = int(data[9:19])/100.00
        new_data["cpf"] = data[19:30]
        new_data["card"] = data[30:42]
        new_data["hour"] = f"{data[1:5]}-{data[5:7]}-{data[7:9]} {data[43:44]}:{data[44:46]}:{data[46:48]}"
        new_data["owner"] = data[48:62].strip()
        new_data["store_name"] = data[62:81].strip()
        new_file.append(new_data)

    file.close()
    return new_file
