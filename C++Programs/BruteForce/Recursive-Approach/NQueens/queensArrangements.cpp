#include <iostream>
#include <fstream>
#include <map>

using namespace std;

#define MAXN 8
bool C[MAXN+1];
map<int, bool> D1; // Northeast-Southwest diagonal map i+j -> True/False
map<int, bool> D2; // Northwest-Southeast diagonal map i-j -> True/False

int Y[MAXN+1]; // solution maps row - collum

int n;
ifstream inputFile;
ofstream outputFile;

void readInput() {
    if (inputFile.is_open()) {
        inputFile >> n;
        inputFile.close();
    }
}

void initialize() {
    // initialize C to have all true
    for (int i = 1; i <= n; i++) C[i] = true;

    // initialize D1 to have all true - range [2, 2n]
    for (int i = 2; i <= 2*n; i++) D1[i] = true;

    // initialize D2 to have all true - range [1-n, n-1]
    for (int i = 1-n; i <= n-1; i++) D2[i] = true;
}

void printOneArrangement() {
    if (outputFile.is_open()) {
        for (int i = 1; i <= n; i++) {
            outputFile << "( " << i << ", " << Y[i] << " )";
        }
        outputFile << endl;
    }
}

void Try(int i) {
    for(int j = 1; j <= n; j++) {
        if (C[j] && D1.at(i+j) && D2.at(i-j)) {
            Y[i] = j;
            if (i == n) {
               printOneArrangement();
            } else {
                C[j] = false; D1[i+j] = false; D2[i-j] = false;
                Try(i+1);
                C[j] = true; D1[i+j] = true; D2[i-j] = true;
            }
        }
    }
}


int main() {
    inputFile.open("QUEENS.INP");
    readInput();
    initialize();
    outputFile.open("QUEENS.OUT");
    Try(1);
    outputFile.close();
    return 0;
}