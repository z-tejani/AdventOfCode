#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <regex>


bool isRepeatingRegex(long long num) {
    std::string s = std::to_string(num);
    std::regex pattern(R"(^(.+)\1+$)");
    return std::regex_match(s, pattern);
}

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
    std::string x;
    std::stringstream ss(inputValue);
    std::getline(ss, x, '-');
    long long firstNum = std::stoll(x);
    std::string y;
    std::getline(ss, y, '-');
    long long secondNum = std::stoll(y);

    for (long long i = firstNum; i <= secondNum; i++) {
      std::string s = std::to_string(i);
      // Drop things with leading 0s
      if(s[0] == '0'){
        continue;
      }
      if( isRepeatingRegex(i)) {
        total += i;
      }
    }
  }

  std::cout << "Total: " << total << std::endl;
  return 0;
}