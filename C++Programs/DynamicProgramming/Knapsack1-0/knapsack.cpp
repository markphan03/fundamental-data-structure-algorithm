#include <iostream>

#include <fstream>

#define nMAX 100

using namespace std;
int w[nMAX], v[nMAX], F[nMAX + 1][nMAX + 1];

void ReadData(ifstream& inputFile, int& n, int& W); // Hàm đọc dữ liệu từ tập tin
void BuildSolutionTable(int n, int W); // Hàm xây dựng bản phương án
void TraceAndWriteResult(ofstream& outputFile, int n, int W); // Truy vết và xuất kết quả

void printMatrix(int n, int W) {
    cout << "Matrix truy vet " << endl;
    for (int i = 0; i <= n; i++) {
        for(int j = 0; j <= W; j++) {
            cout << F[i][j] << " ";
        }
        cout << endl;
    }
}

void ReadData(ifstream& inputFile, int& n, int& W) {
    if (inputFile.is_open()) {
        inputFile >> n >> W;
        for(int i = 0; i < n; i++) {
            inputFile >> w[i] >> v[i];
        }
        // print.
        cout << "Weight: ";
        for (int i = 0; i < n; i++) {
            cout << w[i] << " ";
        }
        cout << endl;
        cout << "Value: ";
        for (int i = 0; i < n; i++) {
            cout << v[i] << " ";
        }
        cout << endl;
        inputFile.close();
    }
}

void BuildSolutionTable(int n, int W) {
    /*
     * Gọi F(i, j) là giá trị lớn nhất có thể có bằng cách chọn trong các món {1, 2, .., i} có giới hạn trọng lượng là j
     * Ta lần lượt thử trọng lượng j trong khoảng 1 đến W (giới hạn trọng lượng) để tìm ra giá trị lớn nhất tương đương
     * với i.
     */
    // Thiết lập cơ sở quy hoạch động.
    // Dòng dưới có nghĩa là lúc không chọn gì cả thì giá trị là 0, với bất kể cân nặng nào.
    for (int j = 0; j <= W; j++) {
        F[0][j] = 0;
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            F[i][j] = F[i-1][j]; // nếu không chọn lấy đồ vật thứ i tại cân nặng giới hạn j thì giá trị tương đương với trước đó
            if (j >= w[i-1] && (F[i-1][j-w[i-1]] + v[i-1]) > F[i][j]) { // nếu chọn lấy vật i với cân nặng wi thì sẽ có giá trị (Value) tốt hơn (với điều kiện trọng lượng giới hạn j đủ cân cho wi)
                F[i][j] = F[i-1][j-w[i-1]] + v[i-1];
            }
        }
    }
}

void TraceAndWriteResult(ofstream& outputFile, int n, int W) {
    if (outputFile.is_open()) {
        outputFile << F[n][W] << endl;
        while (n != 0) {
           if (F[n][W] != F[n-1][W]) {
               outputFile << n;
               W = W - w[n-1]; // w[n-1] hoạt động như w[i]
           }
            n--;
        }
    }
}

int main() {
    int n, W;
    ifstream inputFile("BALO.INP");
    ofstream  outputFile("BALO.OUT");
    ReadData(inputFile, n, W);
    BuildSolutionTable(n, W);
    TraceAndWriteResult(outputFile, n, W);
    printMatrix(n, W);
    return 0;
}



