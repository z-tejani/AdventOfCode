#include <iostream>
#include <fstream>
#include <string>

int rotate(int currentVal, int dist, char direction){
    if(direction == 'L'){
        return ((currentVal - dist) % 100 + 100) % 100;
    }
    else if(direction == 'R'){
        return ((currentVal + dist) % 100 + 100) % 100;
    }
    else{
        throw std::invalid_argument("Invalid direction.");
    }
}

int main() {
    int currentVal = 50;
    int hits = 0;

    std::cout << "Reading input file." << std::endl;
    std::ifstream file("inputValues.txt");
    if (!file.is_open()) {
        std::cerr << "Could not open file\n";
        return 1;
    }

    std::string line;
    while (std::getline(file, line)) {
        //std::cout << line << '\n';
        char dir = line[0];
        //std::cout << "Direction: " << dir << " of type: " << typeid(dir).name() << std::endl;
        int dist = std::stoi(line.substr(1)); 
        if(dir != 'L' && dir != 'R'){
            throw std::invalid_argument("Invalid direction from input file.");
        }
        currentVal = rotate(currentVal, dist, dir);
        if(currentVal == 0){
            hits++;
        }
        //std::cout << "Current Value: " << currentVal << std::endl;
    }
    std::cout << "Amount of times 0 was hit: " << hits << std::endl;

    return 0;
}