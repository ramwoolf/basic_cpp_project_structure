#include <iostream>

#include "sample_class.hpp"

int main() {
    std::cout << "Hello, World!" << std::endl;
    SampleClass sample;
    std::cout << "100 * 100 = " << sample.mult_by_hundred(100) << std::endl;
    return 0;
}