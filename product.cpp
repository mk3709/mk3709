#include <iostream> 
using namespace std; 
int main() 
{     int num;     cin >> num;     int arr[num];     long long int a=1;     for(int i=0; i<num; i++)     {         cin>>arr[i];     }     for(int i=0; i<num; i++)     {         a = ((a*arr[i])%1000000007);     }     cout<<a; }
