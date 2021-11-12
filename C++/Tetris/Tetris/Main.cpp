#pragma once
#include <iostream>
#include <Graphics.hpp>
#include <time.h>
#include <Window.hpp>
using namespace std;
using namespace sf;

namespace Ryan {


	int main() {
		RenderWindow window(VideoMode(320, 480), "Start the Game....");

		while (window.isOpen()) {
			Event e;
			while (window.pollEvent(e)) {
				if (e.type == Event::Closed)
					window.close();

			}

			window.clear(Color::Black);
			window.display();
		}


		system("puase");
		return 0;
	}
}