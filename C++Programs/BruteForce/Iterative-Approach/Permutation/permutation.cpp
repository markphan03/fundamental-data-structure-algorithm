#include<iostream>
#include <fstream>
#define MAX 12
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;

int x[MAX];
int n;
ifstream inputFile;
ofstream outputFile;

/*The technique for generating the next permutation from the current permutation can be constructed as follows:

 + Identify the longest decreasing suffix, find the index i of the element x[i] standing just before that suffix.
    This is equivalent to finding from the position just before the end of the sequence upwards, encountering the first
index i satisfying x[i] < x[i+1].

 + If such an index i is found:
        - Within the decreasing suffix, find the smallest element x[k] satisfying the condition x[k] > x[i]. Since the suffix is
    decreasing, this is done by finding from the end of the sequence upwards, encountering the first index k satisfying
    x[k] > x[i] (binary search can be used). Swap the values of x[k] and x[i].
        - Reverse the order of the decreasing suffix (from x[i+1] to x[k]) to make it increasing.
 + If no such index i is found, meaning the entire sequence is sorted in decreasing order, this is the last configuration.

 */
void generate_permutation();

void printPermutation() {
    for (int i = 0; i < n; i++) {
        outputFile << x[i] << " ";
    }
    outputFile << endl;
}

void swap(int& value1, int& value2) {
    int temp = value1;
    value1 = value2;
    value2 = temp;
}

void generate_permutation() {
    int i, k, a, b;
    // create first config (solution): x[1] := 1; x[2] := 2; ...; x[n] := n;
    for (i = 0; i < n; i++) {
        x[i] = i + 1;
    }

    do {
        printPermutation();
        i = n - 2;
        while (i >= 0 && x[i] > x[i+1]) {
            i--;
        }
        if (i >= 0) { // {Not yet the last permutation (n, n-1, …, 1)}
            k = n - 1;
            while (x[k] < x[i]) {
                k--; // {When found k, we know for sure the last sequence is decreasing.}
            }
            swap(x[k], x[i]);
            a = i + 1; b = n - 1; // {Flip the last decreasing sequence. a: head, b: tail}
            while (a < b) {
                swap(x[a], x[b]);
                a++; // {Move a forward, move b backward. Stop when a passes b.}
                b--;
            }
        }
    } while (i >= 0);
}

int main() {
    inputFile.open(INPUT_FILE);
    outputFile.open(OUTPUT_FILE);
    if (inputFile.is_open() && outputFile.is_open()) {
        inputFile >> n;
        generate_permutation();
        inputFile.close();
        outputFile.close();
    }  else {
        cout << "Error accessing file" << endl;
    }
    return 0;
}




