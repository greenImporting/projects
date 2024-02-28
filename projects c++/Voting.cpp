#include <iostream>

int main() {
   int myAge;
   std::cout << "Enter age: ";
   std::cin >> myAge;
   int votingAge = 18;
   if (myAge >= votingAge){
       std::cout << "Old enough to vote!.";
   }
   else {
    std::cout << "Not old enough to vote buddy!";
   }
   return 0;
}
