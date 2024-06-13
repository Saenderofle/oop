from Solve_of_SBDfunctions import Solver

argu = Solver.from_input_file("input03.txt")

print(f"Solve of the Function with ZERO solutions:", Solver.sort_argu(argu)[0][0])

print(f"Solve of the Function with ONE solutions:", Solver.sort_argu(argu)[0][1])

print(f"Solve of the Function with TWO solutions:", Solver.sort_argu(argu)[0][2])

print(f"Solve of the Function with THREE solutions:", Solver.sort_argu(argu)[0][3])

print(f"Solve of the Function with FOUR solutions:", Solver.sort_argu(argu)[0][4])

print(f"Solve of the Function with INF solutions:", Solver.sort_argu(argu)[0]['infinity'])

print("Minimum number of solutions:", Solver.sort_argu(argu)[1])

print("Maximum number of solutions:", Solver.sort_argu(argu)[2])