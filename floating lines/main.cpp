#include <SDL2/SDL.h>
#include <SDL2/SDL_render.h>
#include <random>

using namespace std;

// definse how many points will be computed
#define COUNT 100
#define RADIUS 5
#define STEP 1
#define MAX 200
#define OFFSET 0
#define DELAY 10

#define WIDTH 1920
#define HEIGHT 1080


int32_t distance(int32_t x1, int32_t y1, int32_t x2, int32_t y2) {
	double d = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));

	return d;
}
/*
int32_t thickness(int32_t d) {
	//SDL_LOG("%i\n", (int32_t)(MAX-d)/(float)300*RADIUS);
	return (MAX-d+1)/(float)300*RADIUS;
}
*/
int main(int argc, char const *argv[])
{
	// define important variables

	int32_t w=WIDTH, h=HEIGHT;
	int8_t l_red = 255, l_green = 0, l_blue = 0;
	int8_t l_r=1, l_g=1, l_b=0;
	int8_t p_red = 0, p_green = 0, p_blue = 255;
	int8_t p_r=1, p_g=1, p_b=0;

	// initialize window and renderer

	SDL_Window* window = NULL;
	SDL_Renderer* renderer = NULL;

	if (SDL_Init(SDL_INIT_VIDEO)) {
		SDL_Log("Unable to initialize SDL: %s", SDL_GetError());
		return 1;
	}

	if (SDL_CreateWindowAndRenderer(w, h, 0, &window, &renderer)) {
		SDL_Log("Unable to initialize window and renderer: %s", SDL_GetError());
		return 1;
	}

	// initialize random points

	SDL_Point points[COUNT] = {};
	int32_t velocity[COUNT][2] = {};

	for (int i = 0; i<COUNT; i++) {
		// setup of the random number generator
		random_device rd;
		mt19937 gen(rd());

		// initializes point coordinates
		uniform_int_distribution<> distrib(RADIUS, w-RADIUS);//-0.9*w);
		int x = distrib(gen);

		uniform_int_distribution<> distrib2(RADIUS, h-RADIUS);//-0.9*h);
		int y = distrib2(gen);

		//SDL_Log("%i %i %i\n", i, x, y);

		points[i] = {x,y};

		// initializes point velocities
		uniform_int_distribution<> distrib3(1,5);
		int v_x = distrib3(gen);
		int v_y = distrib3(gen);

		velocity[i][0] = v_x;
		velocity[i][1] = v_y;
	}


	// mainloop

	bool isRunning = true;
	SDL_Event event;

	while (isRunning) {
		SDL_Delay(DELAY);

		// game functions

		for (int i = 0; i<COUNT; i++) {
			points[i].x += velocity[i][0] * STEP;
			points[i].y += velocity[i][1] * STEP;

			if (points[i].x<=OFFSET || points[i].x>=w-OFFSET) {
				velocity[i][0] *= -1;
			}
			if (points[i].y<=OFFSET || points[i].y>=h-OFFSET) {
				velocity[i][1] *= -1;
			}
		}



		// rendering

		// change color

		if (l_r==1 && l_g==1){
			if (l_red) {
				l_red--; l_green++;
			} else {
				l_r = 0; l_b = 1;
			}
		}
		if (l_g==1 && l_b==1) {
			if (l_green) {
				l_green--; l_blue++;
			} else {
				l_g = 0; l_r = 1;
			}
		}
		if (l_b==1 && l_r==1) {
			if (l_blue) {
				l_blue--; l_red++;
			} else {
				l_b = 0; l_g = 1;
			}
		}

		if (p_r==1 && p_g==1){
			if (p_red) {
				p_red--; p_green++;
			} else {
				p_r = 0; p_b = 1;
			}
		}
		if (p_g==1 && p_b==1) {
			if (p_green) {
				p_green--; p_blue++;
			} else {
				p_g = 0; p_r = 1;
			}
		}
		if (p_b==1 && p_r==1) {
			if (p_blue) {
				p_blue--; p_red++;
			} else {
				p_b = 0; p_g = 1;
			}
		}

		// background

		SDL_SetRenderDrawColor(renderer, 0, 0, 0, SDL_ALPHA_OPAQUE);
		SDL_RenderClear(renderer);

		// foreground

		SDL_SetRenderDrawColor(renderer, l_red, l_green, l_blue, SDL_ALPHA_OPAQUE);

		for (int a = 0; a<COUNT-1; a++) {
			for (int b = 0; b<COUNT-a; b++) {
				if (points[a].x!=points[a+b].x && points[a].y!=points[a+b].y) {
					if (distance(points[a].x, points[a].y, points[a+b].x, points[a+b].y)<=MAX) {
						// thickLineRGBA(renderer, points[a].x, points[a].y, points[a+b].x, points[a+b].y, thickness(distance(points[a].x, points[a].y, points[a+b].x, points[a+b].y)), l_red, l_green, l_blue, SDL_ALPHA_OPAQUE);
						SDL_RenderDrawLine(renderer, points[a].x, points[a].y, points[a+b].x, points[a+b].y);
					}
				}
			}
		}

		// points

		SDL_SetRenderDrawColor(renderer, p_red, p_green, p_blue, SDL_ALPHA_OPAQUE);

		// for (int i = 0; i<COUNT; i++) {
		// 	// filledCircleRGBA(renderer, points[i].x, points[i].y, RADIUS, p_red, p_green, p_blue, SDL_ALPHA_OPAQUE);
		// 	SDL_RenderDrawPoint(renderer, points[i].x, points[i].y);
		// }

		SDL_RenderDrawPoints(renderer, points, COUNT);

		// update screen

		SDL_RenderPresent(renderer);

		while (SDL_PollEvent(&event)) {
			if (event.type == SDL_QUIT) {
				isRunning = false;
			}
		}

		// shader


	}

	if (renderer) {
		SDL_DestroyRenderer(renderer);
	}

	if (window) {
		SDL_DestroyWindow(window);
	}

	SDL_Quit();

	return 0;
}