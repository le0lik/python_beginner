class Matrix:
    def __init__(self, matrix_list):
        if not isinstance(matrix_list, list):
            raise ValueError("Not a matrix: arg is not a list")

        self.height = len(matrix_list)
        self.width = len(matrix_list[0])

        for line in matrix_list:
            if not isinstance(line, list):
                raise ValueError("Not a matrix: Row is not a list")
            if self.width != len(line):
                raise ValueError("Not a matrix: Rows have a different length")

        self.data = matrix_list.copy()

    def __str__(self):
        s = ""
        for line in self.data:
            s += str(line) + "\n"
            #s += "|"
            #for el in line:
            #    s += f" {el:5} "
            #s += "|\n"

        return s

    def __summ_vect(self, v1, v2):
        v_res = []
        for i in range(len(v1)):
            v_res.append(v1[i] + v2[i])
        return v_res

    def __add__(self, other):
        if self.width != other.width or self.height != other.height:
            raise ValueError("Matrixes have a different dimensions")
        res = []
        for i in range(len(self.data)):
            res.append(self.__summ_vect(self.data[i], other.data[i]))

        return Matrix(res)


m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[1, 1, 1], [1, 1, 1]])

print(m1)
print(m2)
print(m1 + m2)
