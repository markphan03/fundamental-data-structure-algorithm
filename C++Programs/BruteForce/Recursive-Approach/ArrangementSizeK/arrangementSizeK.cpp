#include <iostream>
#include <fstream>
#define fill_true(arr, n) {for (int i = 0; i < n; i++) {arr[i] = 1;}}
#define MAX 20
// To run I/O file, you need to add program to working directory.
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;

int x[MAX]; // an arrangement subset size k (MAX size is 20)
bool c[MAX]; // a boolean check variable to check if the element j is already in x or not.
int n, k; // n: size of input, k: size of each arrangement subset
ifstream inputFile;
ofstream outputFile;


void printResult();
void Try(int i); // Try select cho x[i]

void printResult() {
    for (int i = 0; i < k; i++) {
        outputFile << to_string(x[i]);
    }
    outputFile << endl;
}

void Try(int i) {
    for (int j = 0; j < n; j++) {
        if (c[j]) {
            x[i] = j + 1;
            if (i == (k - 1)) { // termination when i = index of last element.
                printResult();
            } else {
                c[j] = false;
                Try(i + 1);
                c[j] = true;
            }
        }
    }
}

int main() {
    // open file input.txt in read mode
    // read file input.txt to save n, k
    // open file output.txt in write mode
    // fill "true" for all element in c
    // call Try(0) to calculate all arrangement subset.
    // close file input.txt
    // close file output.txt

    inputFile.open(INPUT_FILE);
    outputFile.open(OUTPUT_FILE);
    if (inputFile.is_open() && outputFile.is_open()) {
        inputFile >> n >> k;
        fill_true(c, MAX);
        Try(0);
        inputFile.close();
        outputFile.close();

    } else {
        cout << "Error accessing file" << endl;
    }

    return 0;
}







