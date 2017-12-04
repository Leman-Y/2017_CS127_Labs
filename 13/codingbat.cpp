#include <iostream>
/*
int lone_sum(int a, int b, int c)
{

int sum=0;
{
if (a==b);{
sum=c;}

if (a==c);{
sum=b;}

if (b==c);{
sum=a;}

if (a==b && b==c);{
sum=0;}


else 
{
	return a+b+c;
}
}
return sum;

}
*/

int lone_sum(int a, int b, int c){
  int ret_sum = 0;
  if ( a != b && a != c){
    ret_sum += a;
  }
  if ( b != a && b != c){
    ret_sum += b;
  }
  if ( c != b && c != a){
    ret_sum += c;
  }
  return ret_sum;}


/* I do not know how the syntax works so I copied the code from Shariar
*/

int speeding(int speed, bool answer){
  int add;
  if (answer == true){
    add = 5;
  }
  else{
    add = 0;
  }
  int totalspeed = speed + add;
  if (totalspeed < 60){
    return 0;
  }
  else if (totalspeed >= 61 && totalspeed <= 80 ){
    return 1;
  }
  else{
    return 2;
  }
}

bool cigar_party(int amount, bool isWeekend){
  if (amount < 40 ){
    return false;
  }
  if (isWeekend == true && amount >= 40){
    return true;
  }
  else if (amount >= 40 && amount <= 60){
    return true;
  }
  else{
    return false;
  }}


int main()
{
  int speed = speeding(66, true);
  bool c1 = cigar_party(30, false);
  bool c2 = cigar_party(50, false);
  bool c3 = cigar_party(70, true);
  int l1 = lone_sum(1,2,3);
  int l2 = lone_sum(3,2,3);
  int l3 = lone_sum(3,3,3);
  std::cout << "speeding" << std::endl;
  std::cout << speed << std::endl;
  std::cout << "cigar_party" << std::endl;
  std::cout << c1 << std::endl;
  std::cout << c2 << std::endl;
  std::cout << c3 << std::endl;
  std::cout << "lone_sum" << std::endl;
  std::cout << l1 << std::endl;
  std::cout << l2 << std::endl;
  std::cout << l3 << std::endl;
  return 0;
}
