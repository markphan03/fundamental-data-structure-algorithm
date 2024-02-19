#include <iostream>
#include <fstream>
using namespace std;

#define nMAX 10000
int a[nMAX + 2], L[nMAX + 2], T[nMAX + 2];

void ReadData(ifstream& inputFile, int& n);
void BuildSolutionTable(int n);
void TraceAndWriteResult(ofstream& outputFile, int n);

void ReadData(ifstream& inputFile, int& n) {
    if (inputFile.is_open()) {
        inputFile >> n;
        for(int i = 1; i <= n; i++)
            inputFile >> a[i];
        inputFile.close();
    }
}

void TraceAndWriteResult(ofstream& outputFile, int n) {
    outputFile << "Number of element in LIS " << L[0] - 2 << endl;
    int i = T[0];
    while (i != n+1) {
        outputFile << a[i] << " ";
        i = T[i];
    }
}

void BuildSolutionTable(int n) {
    /*
        S1: Declare Dynamic Programming base case
        B2: Create DP table by the Recurrance Relation formula
        B3: Trace backward
     */
    int jmax;
    a[0] = INT_MIN; a[n+1] = INT_MAX;
    L[n+1] = 1; // DP base case
    for (int i = n; i >= 0; i--) {
        jmax = n + 1;
        for (int j = i + 1; j <= n+1; j++) {
            if (a[j] > a[i] && L[j] > L[jmax]) { // We assume each L[j] we choose is the optimal solution - by Mathematical Induction.
                jmax = j;
            }
        }
        L[i] = L[jmax] + 1; // assign the optimal solution to L[ith]
        T[i] = jmax;
    }
}

int main(){
    ifstream inputFile("INCSEQ.INP");
    ofstream outputFile("INCSEQ.OUT");
    int n;
    ReadData(inputFile, n);
    BuildSolutionTable(n);
    TraceAndWriteResult(outputFile, n);
    return 0;
}
