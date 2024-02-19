#include<iostream>
#include <fstream>
#define MAX 20
#define INPUT_FILE "input.txt"
#define OUTPUT_FILE "output.txt"

using namespace std;

int x[MAX];
int n, k; // total element to select, size of each combination
ifstream inputFile;
ofstream outputFile;

void printResult();
void Try(int i); // Enumerate x[i] in lexicographic order

void printResult() {
    outputFile << "{ ";
    for (int i = 1; i <= k; i++) {
        outputFile << x[i] << " ";
    }
    outputFile << "}" << endl;
}

void Try(int i) {
    for (auto j = x[i-1] + 1; j <= n - k + i; j++) {
        x[i] = j;
        if (i == k) printResult();
        else Try(i+1);
    }
}

int main() {
    inputFile.open(INPUT_FILE);
    outputFile.open(OUTPUT_FILE);
    if (inputFile.is_open() && outputFile.is_open()) {
        inputFile >> n >> k;
        x[0] = 0;
        Try(1);
        inputFile.close();
        outputFile.close();
    }  else {
        cout << "Error accessing file" << endl;
    }
    return 0;
}




