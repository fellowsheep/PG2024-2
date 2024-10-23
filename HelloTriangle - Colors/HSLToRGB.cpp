#include <iostream>
#include <tuple>
#include <cmath>

using namespace std;

// Função para converter HSL em RGB (da explicação anterior)
std::tuple<int, int, int> hslToRGB(float h, float s, float l) {
    float c = (1 - fabs(2 * l - 1)) * s;
    float x = c * (1 - fabs(fmod(h / 60.0, 2) - 1));
    float m = l - c / 2;
    float r, g, b;

    if (h >= 0 && h < 60) {
        r = c, g = x, b = 0;
    } else if (h >= 60 && h < 120) {
        r = x, g = c, b = 0;
    } else if (h >= 120 && h < 180) {
        r = 0, g = c, b = x;
    } else if (h >= 180 && h < 240) {
        r = 0, g = x, b = c;
    } else if (h >= 240 && h < 300) {
        r = x, g = 0, b = c;
    } else {
        r = c, g = 0, b = x;
    }

    int R = (r + m) * 255;
    int G = (g + m) * 255;
    int B = (b + m) * 255;

    return std::make_tuple(R, G, B);
}

int main()
 {
    float s = 1.0;  // Saturação
    float l = 0.5;  // Luminosidade

    cout << "teste" << endl;

    for (int h = 0; h <= 360; h += 10) {  // Variando o ângulo de matiz de 0 a 360, pulando 10 graus
        auto [r, g, b] = hslToRGB(h, s, l);  // Usando a função HSL -> RGB

        std::cout << "HSL(" << h << ", " << s << ", " << l << ") -> "
                  << "RGB(" << r << ", " << g << ", " << b << ")\n";
    }

    return 0;
}
