#include <iostream>
using namespace std;

int primenums; // Prime Numbers
int AON; // Any Other Number
bool Prime = false;

void Prime100() {
	for (int i = 0; i < 50; i++)
		for (int j = 50; j < 100; j++) {
			AON = j;
			if (primenums = i % AON) {
				if (primenums / 1 == 1 || primenums / primenums == 1)
					Prime = true;
				while (AON != 1 || AON != primenums) {
					if (AON / AON == primenums)
						Prime = false;
				}
			}
			if (Prime == true)
				cout << primenums << endl;
			else
				cout << AON << endl;
		}
}

int main() {
	Prime100();
	system("pause");
	return 0;
}