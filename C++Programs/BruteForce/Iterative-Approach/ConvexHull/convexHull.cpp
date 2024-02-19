/*
 * Gift wrapping algorithm for convex hull problem
 * Adapted from: Le Minh Hoang - University of Natural Science, Ho Chi Minh city
 * Author: Mark Phan
 * */

#include <bits/stdc++.h>
#include <iostream>

using namespace std;
const double EPS = 1e-9; // Epsilon

struct Point {
    int x, y;
    Point(int x = 0, int y = 0) : x(x), y(y) {}
    bool operator == (const Point& o) {
        return x == o.x && y == o.y;
    }
    bool operator != (const Point& o) {
        return !(*this == o);
    }

    Point operator - (const Point& o) {
        return Point(x - o.x, y - o.y);
    }

    double length() const {
        return sqrt(1LL * x * x + 1LL * y * y);
    }
};