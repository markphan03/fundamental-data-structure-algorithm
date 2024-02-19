#include <iostream>
#include <vector>
using namespace std;

void QuickSortImp(vector<int>& a, int L, int R);

void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void QuickSort(vector<int>& a, int n) {
    QuickSortImp(a, 0, n-1);
}

void QuickSortImp(vector<int>& a, int L, int R) {
    int i = L, j = R, x = a[L + (R - L)/2]; // x is pivot, L + (R - L)/2 to avoid number overflow
    do {
        while (a[i] < x) i++;
        while (a[j] > x) j--;
        if (i <= j) {
            swap(a[i], a[j]);
            i++; j--;
        }
    } while (i <= j);
    if (L < j)
        QuickSortImp(a, L, j);
    if (i < R)
        QuickSortImp(a, i, R);
}

int main() {

    vector<int> a = {2, 1, 4, 5};
    int n = a.size();
    QuickSort(a, n);
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

}