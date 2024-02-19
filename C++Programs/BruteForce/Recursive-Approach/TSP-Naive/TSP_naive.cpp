/*
 * TSP-naive
 * @Author: Mark Phan - Undergraduate Teaching Assistant at University of Lincoln, NE
 *
 * TSP-naive using exhaustive search (brute-force) has 2 steps
 *  1. Generate all permutation of cities (except the first city)
 *  2. Find the permutation has minimum distance
 */

#include <bits/stdc++.h>
using namespace std;

#define initializeFree(arr, n) {for(int i=0; i<=n;i++) arr[i] = true;}
#define MAX_CITY 10

int n, m; // n: total vertex, m: total edges
int minDistance; // min distance from 1 to all nodes, then back to 1.
int BestTrip[MAX_CITY+1]; // best trip
int Free[MAX_CITY+1]; // check array
int W[MAX_CITY+1][MAX_CITY+1]; // input weighted matrix

vector<vector<int>> all_trips;
vector<int> trip (MAX_CITY+1, 0);


ifstream inputfile;
ofstream outputfile;

void generate_trips(int i) {
    for (int j = 1; j <= n; j++) {
        if (Free[j]) {
            trip[i] = j;
            if (i == n) {
                all_trips.push_back(trip);
            } else {
                Free[j] = false;
                generate_trips(i+1);
                Free[j] = true;
            }
        }
    }
}

void find_best_trip() {
    minDistance = INT_MAX;
    int best_trip_idx = 0;
    for (int i = 0; i < all_trips.size(); i++) { // all_trips is a vector, has index starting from 0
        vector<int> atrip = all_trips[i]; atrip[n+1] = 1; // add the first city to atrip
        int tripDistance = 0;
        for (int j = 1; j <= n; j++) {
            tripDistance += W[atrip[j]][atrip[j+1]];
        }
        if (minDistance > tripDistance) {
            best_trip_idx = i;
            minDistance = tripDistance;
        }
    }
    for (int k = 1; k <= n; k++) {
        BestTrip[k] = all_trips[best_trip_idx][k];
    }
    BestTrip[n+1] = 1;
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

void printResult() {
    outputfile << "Min Distance: " << minDistance << endl;
    outputfile << "Trip: ";
    for (int i = 1; i <= n; i++) {
        outputfile << BestTrip[i] << "-> ";
    }
    outputfile << BestTrip[n+1] << endl;
    outputfile.close();
}


void Init() {
    initializeFree(Free, n);
    Free[1] = false;
    trip[1] = 1;
}

int main() {
    inputfile.open("TSP.INP");
    outputfile.open("TSP.OUT");
    if (inputfile.is_open() && outputfile.is_open()) {
        readInput();
        Init();
        generate_trips(2);
        find_best_trip();
        printResult();
    }
    return 0;
}
