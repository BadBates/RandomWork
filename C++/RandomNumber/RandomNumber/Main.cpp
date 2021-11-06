#include <iostream>
using namespace std;

float num = 0, random = 0;

float give(float min, float max) {
	min = 1, max = 21351358;
	return give(min, max);
}

float Take() {
	auto g = give(1, 21351358);

	if(random == 0)
		if (min > g.max) {
			num = g.max % min;
			return num;
			cout << num << endl;
		}
}

void main() {
	Take();
	system("puase");
}