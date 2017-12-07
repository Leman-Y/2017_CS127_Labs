#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;

//Pig latin
/*
Notes:
-c++ does not use True but lowercase true
-1 is true
-0 is false
*/

bool is_vowel(char c) { //I copied this code from online
    c = tolower(c);
    if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
      return true;
    }
    else; {
      return false; }
}

std::string piglatin(std::string a){ 
// a=anystring
   string first_letter=a.substr(0,1); // a[0] doesnt work for some reason

/*
This doesnt work IDK WHY
  if (is_vowel(first_letter)){
    return a+"ay";
  }
*/
  
  if (is_vowel(a[0])){
    return a+"ay";
  }
  else{
    return a.substr(1)+a[0]+"ay";  
  }

  
}

int main(){
  cout<<is_vowel('a')<<endl;
  cout<<is_vowel('b')<<endl;
  cout<<is_vowel('i')<<endl;
  
  cout<<piglatin("apple")<<endl;
  cout<<piglatin("bib")<<endl;
  cout<<piglatin("latin")<<endl;

}

