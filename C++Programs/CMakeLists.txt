cmake_minimum_required(VERSION 3.27)
cmake_minimum_required(VERSION 3.24)

# Brute Force Recursive
project(arrangement_size_k)
project(combination)
project(permutation)
project(nqueens)
project(tsp_bnb)
project(tsp_naive)

# Brute Force Iterative
project(closest_pair)
project(generate_permutation)
project(generate_combination)

# Dynamic Programming
project(knapsack1-0)
project(lis)

# others
project(gcd)

set(CMAKE_CXX_STANDARD 17)


# Brute Force Recursive
add_executable(arrangement_size_k BruteForce/Recursive-Approach/ArrangementSizeK/arrangementSizeK.cpp)
add_executable(combination BruteForce/Recursive-Approach/Combination/combination.cpp)
add_executable(permutation BruteForce/Recursive-Approach/Permutation/permutation.cpp)
add_executable(nqueens BruteForce/Recursive-Approach/NQueens/queensArrangements.cpp)
add_executable(tsp_naive BruteForce/Recursive-Approach/TSP-Naive/TSP_naive.cpp)
add_executable(tsp_bnb DynamicProgramming/TSP_BranchAndBound/TSP.cpp)


# Brute Force Iterative
add_executable(generate_permutation BruteForce/Iterative-Approach/Permutation/permutation.cpp)
add_executable(generate_combination BruteForce/Iterative-Approach/Combination/combination.cpp)
add_executable(closest_pair BruteForce/Iterative-Approach/ClosestPair/closestPair.cpp)

# Dynamic Programming
add_executable(knapsack1-0 DynamicProgramming/Knapsack1-0/knapsack.cpp)
add_executable(lis DynamicProgramming/LIS/lis.cpp)

add_executable(gcd main.cpp)
