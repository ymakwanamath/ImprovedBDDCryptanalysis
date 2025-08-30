import random

def generate_equation(k, d, m, min_m):
  """Generates a single binary equation with given parameters."""
  num_terms = random.randint(min_m, m)
  terms = []
  for _ in range(num_terms):
    term = ""
    var_count = random.randint(1, d)
    for _ in range(var_count):
      var_index = random.randint(0, k-1)
      term += f"x{var_index}*"
    term = term[:-1]  # Remove the trailing '*'
    terms.append(term)
  return " + ".join(terms)

def generate_equations(n, k, d, m, min_m):
  """Generates a list of 'n' binary equations."""
  file=open('random_equations_generated.txt', 'w')
  equations = []
  for i in range(n):
    equation = f"{generate_equation(k, d, m, min_m)}"
    equations.append(equation)
  file.write(str(equations))
  

def main():
  n = int(input("Enter the number of equations: "))
  k = int(input("Enter the number of variables: "))
  d = int(input("Enter the maximum degree: "))
  m = int(input("Enter the maximum number of terms: "))
  min_m = int(input("Enter the minimum number of terms: "))

  equations = generate_equations(n, k, d, m, min_m)
  print(equations)

if __name__ == "__main__":
  main()