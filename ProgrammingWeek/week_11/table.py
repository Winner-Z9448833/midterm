class Table:
  def __init__(self, m):
    self.m = m

  def show(self):
    for r in self.m:
      print(r)

  def save_file(self, filename):
    with open(filename, "w") as f:
      for r in self.m:
        f.write(str(r) + "\n")

my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

t = Table(my_data)
t.show()
t.save_file("table_data.txt")