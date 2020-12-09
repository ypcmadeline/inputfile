import csv
import numpy as np
import constPara

class inputFile:

    def __init__(self, varyParameter, constParameter):
        self.vary_name = []
        self.range_list = []
        self.sweep = []
        for i in range(len(varyParameter)):
            self.vary_name.append(varyParameter[i].getName)

        self.const_name = []
        self.const_value = []
        for i in range(len(constParameter)):
            self.const_name.append(constParameter[i].getName())
            self.const_value.append(constParameter[i].getValue())
        self.write_list = []
        self.file_list = []
        self.csv = "sample.csv"
        # self.f = open(self.csv, 'w+', newline='')

        for i in range(len(varyParameter)):
            tlist = []
            for j in range(len(varyParameter[i].range)):
                num = varyParameter[i].range[j].split(",")
                if varyParameter[i].sweep[j]:
                    # if first range sweep
                    tlist = tlist + list(np.linspace(int(num[0]), int(num[1]), int(num[2]))) \
                           + list(np.linspace(int(num[1]), int(num[0]), int(num[2])))
                else:
                    tlist = tlist + list(np.linspace(int(num[0]), int(num[1]), int(num[2])))
            self.write_list.append(tlist)
        # self.writeHead()
        self.recurse(len(varyParameter), len(varyParameter))
        # self.f.close()

    def writeHead(self):
        name_list = self.vary_name + self.const_name
        self.f.csv_write = csv.writer(self.f)
        self.f.csv_write.writerow(name_list)
        self.f.flush()

    def recurse(self, n, t):
        if n <= 0:
            return
        for i in range(len(self.write_list[n - 1])):
            if i == 0:
                if len(self.file_list) != t:
                    self.file_list.append(self.write_list[n - 1][i])
            # else:
            self.file_list[t - n] = self.write_list[n - 1][i]
            if len(self.file_list) == t and n == 1:
                # self.f.csv_write = csv.writer(self.f)
                # self.f.csv_write.writerow(self.file_list + self.const_value)
                # self.f.flush()
                print(self.file_list + self.const_value)
            self.recurse(n - 1, t)
