#include <iostream>
using namespace std;

int Matrix[4][4];
int matrix[] = { 5,4,2,1 };

void main()
{
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++) {
			Matrix[i][j] = Matrix[i][j] * matrix[5,4,2,1];
			cout << Matrix[i][j];
		}

	system("pause");
}