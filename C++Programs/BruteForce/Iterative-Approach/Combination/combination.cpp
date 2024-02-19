/*
 * Closest Pair
 * @Adpated from: Le Minh Hoang - Giai Thuat Lap Trinh - University of Science - VNUHCM
 * @Author: Mark Phan - Undergraduate Teaching Assistant at University of Lincoln, NE
 *
 * Problem statement: Generate all number combinations size k from the set of number {1, 2, ... n}
 *
 * Input from "input.txt"
 * n k
 *
 * Output from "output.txt" at n=5, k=3
* 1 2 3
* 1 2 4
* 1 2 5
* 1 3 4
* 1 3 5
* 1 4 5
* 2 3 4
* 2 3 5
* 2 4 5
* 3 4 5
 */
#include<iostream>
#include <fstream>
#define MAX 12
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;

int x[MAX];
int n, k;
ifstream inputFile;
ofstream outputFile;

/*
The technique for generating the next permutation from a given one can be constructed as follows:
    Start from the end of the sequence and move backward until encountering an element x[i] that has not reached the
    upper limit n - k + i.
    - If found:
        * Increase x[i] by 1.
        * Set all elements after x[i] to the lower limit.
    - If not found, it means all elements have reached the upper limit, indicating the final configuration.
 */
void generate_combination();

void printCombination() {
    for (int i = 0; i < k; i++) {
        cout << x[i] << " ";
    }
    cout << endl;
}


void generate_combination() {
    int i;
    for (i = 0; i < k; i++) {
        x[i] = i + 1;
    }
    do {
        printCombination();
        i = k - 1; // {Consider moving backward from the end of the sequence to find x[i] that has not reached the upper limit of n - k + i}
        while (i >=0 && x[i] == (n - k + i + 1)) {
            i--;
        }
        if (i >= 0) { // "If i is not set to be greater than or equal to 0, an error will occur at x[-1]++ in the line below
            x[i]++; // {Increase x[i] by 1, set all elements after x[i] to their lower limit.}
            for (int j = i + 1; j < k; j++) {
                x[j] = x[j-1] + 1;
            }
        }

    } while (i >= 0);
}

int main() {
    inputFile.open(INPUT_FILE);
    outputFile.open(OUTPUT_FILE);
    if (inputFile.is_open() && outputFile.is_open()) {
        inputFile >> n >> k;
        generate_combination();
        inputFile.close();
        outputFile.close();
    }  else {
        cout << "Error accessing file" << endl;
    }
    return 0;
}

