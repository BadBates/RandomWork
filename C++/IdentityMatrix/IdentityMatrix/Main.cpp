#include <iostream>
#include <vector>
using namespace std;

int matrix[4][4];
int num = 0;

int main(){
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (i == 0 && j == 0 || num = 5)
				matrix[i][j] = 1;
			else
				matrix[i][j] = 0;
			num++;
		}
	}

	for (int i = 0; i <= 4; i++)
		for (int j = 0; j <= 4; j++)
			if (i < 3)
				cout << matrix[i][j];
	system("pause");
	return 0;
}