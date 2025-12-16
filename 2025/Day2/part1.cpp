#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main() {
  std::cout << "Reading input file." << std::endl;
  std::ifstream file("input.txt");
  if (!file.is_open()) {
    std::cerr << "Could not open file" << std::endl;
    return 1;
  }
  std::string inputValue;
  long long total = 0;
  while (std::getline(file, inputValue, ',')) {
    std::cout << inputValue << std::endl;
    std::string x;
    std::stringstream ss(inputValue);
    std::getline(ss, x, '-');
    long long firstNum = std::stoll(x);
    // std::cout << "First Num: " << firstNum << std::endl;
    std::string y;
    std::getline(ss, y, '-');
    long long secondNum = std::stoll(y);
    // std::cout << "Second Num: " << secondNum << std::endl;

    for (long long i = firstNum; i <= secondNum; i++) {
      std::string s = std::to_string(i);
      int length = s.length();
      std::string firstPart = s.substr(0, length / 2);
      std::string secondPart = s.substr(length / 2);
      if (firstPart == secondPart) {
        std::cout << "Found: " << i << std::endl;
        total += i;
      }
    }
    std::cout << "Total: " << total << std::endl;
  }
  return 0;
}