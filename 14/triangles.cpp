#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;
std::string line(int l, std::string c){
//Return int letters of the string c 
//  string newstring=c.substr(0,l);

  return c.substr(0,l);
}

std::string rect(int w, int h) {
//print triangle width and height
//Make the line then print the line h times
/* Does not work because I am returning newstring but if the height of
    a rectangle is 0 then there should be no line but there is a line
  string newstring=std::string(w,'*');
  for (int x=0 ; x<h ; x++)
  {
    cout<<newstring<<endl;
  }
*/  
  
  string rectangle=""; //Empty string

  if (h==0){  //If the height is 0
    return ""; //Return empty string no rectangle for you
  }
  else { //Other cases
  
    for (int x=0 ; x<h ; x++)  //For if integer x=0, if x is less than h
    //and x++ means x=x+1 add one to each increment
      {
        rectangle=rectangle+std::string(w,'*')+"\n"; 
        //new rectangle=(previous rectanlge)+the line of the rectangle+new line
      }
  
  }
  
    return rectangle;
}


/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
// Print triangle so space space asterik
 string tri="";  //Empty string
 for (int x=0;x<h;x++){ //for int x=0, if x is less than h, x=x+1
   string star='*'+std::string(x,'*'); //star=*and x times *
   tri=tri+star+"\n"; //add the stars to the empty string 
 }

  return tri; //return the string
}

 
/*
123*
12***
1*****
 */

std::string tri2(int h) {
  string tri=""; //Empty string
  int q=h;
  for (int x=0;x<h;x++){ //Cant put q in there rip
    string space=std::string(h-x,' '); //h-x if is 3 then 3-0,3*" "=3 spaces
    string star='*'+std::string(x*2,'*'); //2 times * + *
    tri=tri+space+star+"\n";
  }

  return tri;
}

/*
  *
 **
***
 */
std::string tri3(int h) {
  string tri=""; //Empty string
  int q=h;
  for (int x=0;x<h;x++){ //Cant put q in there rip
    string space=std::string(h-x,' '); // h-x if is 3 then 3-0,3*" "=3 spaces
    string star='*'+std::string(x,'*'); // *+*
    tri=tri+space+star+"\n";
  }

  return tri;


}

int main(){
  string s="hello";
  cout<<s<<endl;
  cout<<line(0,s)<<endl;
  cout<<line(1,s)<<endl;
  cout<<line(2,s)<<endl;
  
  cout<<rect(1,0)<<endl;
  cout<<rect(5,0)<<endl;
  cout<<rect(4,2)<<endl;
  cout<<rect(1,4)<<endl;
  
  cout<<tri1(1)<<endl;
  cout<<tri1(3)<<endl;
  cout<<tri1(5)<<endl;

  cout<<tri2(3)<<endl;
  cout<<tri2(5)<<endl;

  cout<<tri3(1)<<endl;
  cout<<tri3(3)<<endl;
  cout<<tri3(5)<<endl;


//Put testing in here
}
