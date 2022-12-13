#include "Model.h"
using namespace std;

Model::Model(){
    Items* VL1 = new Items[3];
    cout << "Model V1" << endl;
    for (int i = 0; i < 3; i++){
        char name[50];
        sprintf(name, "Screw %d", i)+1;
        VL1[i].setAll(name, i+3, i+2, i+1);
        //cout << (VL1+i)->getName();
        cout << VL1[i].getName() << endl;
        cout << "   Price: " << VL1[i].getPrice() << endl;
        cout << "   Rating: " << VL1[i].getRating() << endl;
        cout << "   Quantity: " << VL1[i].getQty() << endl;
    }

    Items* VL2 = new Items[3];
    cout << "Model V2" << endl;
    for (int i = 0; i < 3; i++){
        char name[50];
        sprintf(name, "Nail %d", i+1);
        VL2[i].setAll(name, i+3, i+2, i+1);
        cout << VL2[i].getName() << endl;
        cout << "   Price: " << VL2[i].getPrice() << endl;
        cout << "   Rating: " << VL2[i].getRating() << endl;
        cout << "   Quantity: " <<VL2[i].getQty() << endl;
    }

}

Model::~Model(){
    cout << "Model destructed" << endl;
}


