/*
 * Closest Pair
 * @Author: Mark Phan - Undergraduate Teaching Assistant at University of Lincoln, NE
 *
 * Problem statement: Given n points, each point has d features (vector d x 1). Find the distance between two closest
 * point, and print those two points.
 *
 *Input in CLOSEST_PAIR.INP:
 * number of points: n [SPACE] number of dimension: d
 * Point 0: f1 f2 f3 f4 ... fd
 * Point 1: f1 f2 f3 f4 ... fd
 * .....
 * Point n-1: f1 f2 f3 f4 ... fd
 */
#include <bits/stdc++.h> // This library store cmath, iostream, fstream, vector, etc.
using namespace std;

ifstream inputfile;

struct Point{
    int dimension;
    vector<double> features;
    Point(int dim): dimension(dim), features(dim, 0.0) {} // initialize Point.features as a vector length dim and all elements are 0.0

    void setFeatures() {
        for (int i = 0; i < dimension; i++) {
            inputfile >> features[i];
        }
    }

    void displayFeatures() { // mostly for visualizing, debugging
        cout << "Point (Vector) with dimension " << dimension << ": [";
        for(int i = 0; i < dimension; i++) {
            cout << features[i] << " ";
            if (i < dimension - 1) {
                cout << ", ";
            }
        }
        cout << "]" << endl;
    }

    double operator -(const Point& point) {
        double sumSquaredDifference = 0;
        for (int i = 0; i < dimension; i++) {
            double difference = (features[i] - point.features[i]);
            sumSquaredDifference += difference * difference;
        }
        return sqrt(sumSquaredDifference);
    }
};


int n; // total points
int d; // total dimensions per point

vector<Point> points;
vector<Point> closest_pair = {Point(d), Point(d)};

double closestPair() {
    double minDist = FLT_MAX;
    int imin = 0, jmin = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j) {
                double dist = points[i] - points[j];
                if (dist < minDist) {
                    minDist = dist; imin = i; jmin = j;
                }
            }
        }
    }
    closest_pair[0] = points[imin];
    closest_pair[1] = points[jmin];
    return minDist;
}

void readInput() {
    inputfile >> n >> d;
    for (int p = 0; p < n; p++) {
        Point point(d);
        point.setFeatures();
        points.push_back(point);
    }
}

int main() {
    inputfile.open("CLOSEST_PAIR.INP");
    if (inputfile.is_open()) {
        readInput();
        cout << "The minimum distance is " << closestPair() << endl;
        cout << "The source point is ";
        closest_pair[0].displayFeatures();
        cout << "The destination point is ";
        closest_pair[1].displayFeatures();
    } else {
        cout << "Input file does not open!" << endl;
    }
    return 0;
}
