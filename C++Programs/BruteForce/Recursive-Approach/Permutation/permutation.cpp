#include<iostream>
#include <fstream>
#define MAX 20
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"
#define fill_true(arr, n) {for (int i = 0; i < n; i++) {arr[i] = 1;}}
using namespace std;

int x[MAX], c[MAX];
int n; // total element to select, size of each combination
ifstream inputFile;
ofstream outputFile;

void printResult();
void Try(int i); // Enumerate x[i] in lexicographic order

void printResult() {
    for (int i = 0; i < n; i++) {
        outputFile << x[i] << " ";
    }
    outputFile << endl;
}

void Try(int i) {
    for (int j = 0; j < n; j++) {
        if (c[j]) {
            x[i] = j + 1;
            if (i == (n - 1)) {
                printResult();
            } else {
                c[j]= false;
                Try(i+1);
                c[j] = true;
            }
        }
    }
}

int main() {
    inputFile.open(INPUT_FILE);
    outputFile.open(OUTPUT_FILE);
    if (inputFile.is_open() && outputFile.is_open()) {
        inputFile >> n;
        outputFile << n << endl;
        fill_true(c, MAX);
        Try(0);
        inputFile.close();
        outputFile.close();
    }  else {
        cout << "Error accessing file" << endl;
    }
    return 0;
}





