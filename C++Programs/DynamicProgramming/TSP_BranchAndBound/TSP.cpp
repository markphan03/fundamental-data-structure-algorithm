/*
 * TSP - Branch And Bound (Dynamic Programming)
 * @Author: Mark Phan - Undergraduate Teaching Assistant at University of Lincoln, NE
 * Adapted from: Le Minh Hoang - University of Science, VNUHCM
 *
 */

#include <bits/stdc++.h>
using namespace std;

#define initializeFree(arr, n) {for(int i=0; i<=n;i++) arr[i] = true;}
#define MAX_CITY 10

int n, m; // n: total vertex, m: total edges
int minDistance; // min distance from 1 to all nodes, then back to 1.
int BestTrip[MAX_CITY+2]; // best trip
int Free[MAX_CITY+1]; // check array
int X[MAX_CITY+1]; // candidate trip
int D[MAX_CITY+1]; // distance array
int W[MAX_CITY+1][MAX_CITY+1]; // input weighted matrix

ifstream inputfile;
ofstream outputfile;

void TSP(int i) {
    for (int j = 2; j <= n; j++) {
        if (Free[j]) {
            X[i] = j;
            D[i] = D[i-1] + W[X[i-1]][j];
            if (D[i] < minDistance) {
                if (i < n) {
                    Free[j] = false;
                    TSP(i+1);
                    Free[j] = true;
                } else {
                    if (D[n] + W[X[n]][1] < minDistance) {
                        for (int k = 1; k <= n; k++) {
                            BestTrip[k] = X[k];
                        }
                        BestTrip[n+1] = 1; // set last element of trip to the first city.
                        minDistance = D[n] + W[X[n]][1];
                    }
                }
            }
        }
    }
}

// void TSP_textbook(int i)

void printResult() {
    outputfile << "Min Distance: " << minDistance << endl;
    outputfile << "Trip: ";
    for (int i = 1; i <= n; i++) {
        outputfile << BestTrip[i] << "-> ";
    }
    outputfile << BestTrip[n+1] << endl;
    outputfile.close();
}

void readInput() {
    inputfile >> n >> m;
    for (int i = 1; i <= n; i++) { // create weighted matrix filled with positive infinity
        for (int j = 1; j <= n; j++) {
            if (i == j) W[i][j] = 0;
            else W[i][j] = INT_MAX;
        }
    }
    for (int i = 1; i <= m; i++) {
        int from, to;
        inputfile >> from >> to;
        inputfile >> W[from][to];
        W[to][from] = W[from][to];
    }
    inputfile.close();
}

void Init() {
    initializeFree(Free, n);
    minDistance = INT_MAX;
    Free[1] = false;
    X[1] = 1;
    D[1] = 0;
}

int main() {
    inputfile.open("TSP.INP");
    if (inputfile.is_open()) {
        readInput();
        Init();
        TSP(2);
        outputfile.open("TSP.OUT");
        if (outputfile.is_open()) {
            printResult();
        } else {
            cout << "Error opening output file!" << endl;
        }
    } else {
        cout << "Error opening input file!" << endl;
    }
    return 0;
}











//int TSP_textbook(int i, set<int> S) {
//    if (S.size() == 0) {
//        return W[i][0];
//    } else {
//        int value = INT_MAX;
//        for (auto j: S) {  // j is remaining city
//            val = TSP_nmtp(j, S.erase(j));
//            val = W[i][j] + val;
//            if (value > val) {
//                value = val;
//            }
//        }
//        return value;
//    }
//
//}