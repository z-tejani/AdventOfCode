#include <fstream>
#include <iostream>
#include <string>

int rotate(int currentVal, int dist, char direction) {
  if (direction == 'L') {
    return ((currentVal - dist) % 100 + 100) % 100;
  } else if (direction == 'R') {
    return ((currentVal + dist) % 100 + 100) % 100;
  } else {
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
    // std::cout << line << '\n';
    char dir = line[0];
    // std::cout << "Direction: " << dir << " of type: " << typeid(dir).name()
    // << std::endl;
    int dist = std::stoi(line.substr(1));
    if (dir != 'L' && dir != 'R') {
      throw std::invalid_argument("Invalid direction from input file.");
    }
    if (dir == 'R') {
      hits += (dist) / 100;
      hits += (dist % 100 + currentVal) >= 100 ? 1 : 0;
    } else {
      hits += (dist) / 100;
      if (currentVal != 0) {
        hits += currentVal - (std::abs(dist % 100)) <= 0 ? 1 : 0;
      }
    }
    currentVal = rotate(currentVal, dist, dir);
    // std::cout << "Current Value: " << currentVal << std::endl;
  }
  std::cout << "Amount of times 0 was hit or passed: " << hits << std::endl;
  std::cout << "Hex Value: " << std::hex << hits << std::endl;

  return 0;
}