# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"1110.0","system":"med"},{"code":"1421.0","system":"med"},{"code":"1488.0","system":"med"},{"code":"16096.0","system":"med"},{"code":"28472.0","system":"med"},{"code":"31272.0","system":"med"},{"code":"33570.0","system":"med"},{"code":"34294.0","system":"med"},{"code":"3773.0","system":"med"},{"code":"57103.0","system":"med"},{"code":"57629.0","system":"med"},{"code":"61171.0","system":"med"},{"code":"63149.0","system":"med"},{"code":"71740.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('pilonidal-cystsinus-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["pilonidal-cystsinus-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["pilonidal-cystsinus-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["pilonidal-cystsinus-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
