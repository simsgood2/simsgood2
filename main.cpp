#include <iostream>

using namespace std;

void sort(int &x, int &y, int &z){

    int small=x;
    int big=x;

    if(small>y) small=y;
    if(big<y) big=y;
    if(small>z) small=z;
    if(big<z) big=z;

    int middle;
    if(x>small&&x<big) middle=x;
    if(y>small&&y<big) middle=y;
    if(z>small&&z<big) middle=z;

    x=small;
    y=middle;
    z=big;

}

int main( ) {
    int x, y, z;
    char ans;
    do {
        cout << "Enter three integers: ";
        cin >> x >> y >> z;
        sort(x, y, z);
        cout << x << " " << y << " " << z << endl;
        cout << "Again? (Y/y) or type any others to quit: ";
        cin >> ans;
    } while (ans == 'y' || ans == 'Y');
    return 0;
}