# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows  
        self.cols = cols  
        self.matrix = [[None for j in range(cols)] for i in range(rows)]  

        for i in range(rows):
            for j in range(cols):
                self.set_value(i, j, 1)

    def set_value(self, row, col, value):
        if row < 0 or col < 0:
            raise ValueError("Row and column indices must be non-negative")

        while row >= self.rows:
            self.matrix.append([1 for j in range(self.cols)])
            self.rows += 1
        while col >= self.cols:
            for i in range(self.rows):
                self.matrix[i].append(None)
            self.cols += 1

        self.matrix[row][col] = value  

    def replace_value(self, row, col, value):
        self.set_value(row, col, value)

    def get_rows_count(self):
        return self.rows

    def get_cols_count(self):
        return self.cols

    def __str__(self):
        return '\n'.join([str(row) for row in self.matrix])

matri = Matrix(10, 10)

print("Созданная матрица:")
print(matri)
print("Количество строк:", matri.get_rows_count(), "Количество столбцов:", matri.get_cols_count())

matri.set_value(5, 4, None)
matri.set_value(2, 2, None)
matri.set_value(4, 4, None)
matri.replace_value(5, 6, None)
matri.replace_value(6, 3, None)
matri.replace_value(3, 8, None)

print("Матрица после использования методов добавления и замены:")
print(matri)

print("Количество строк:", matri.get_rows_count(), "Количество столбцов:", matri.get_cols_count())