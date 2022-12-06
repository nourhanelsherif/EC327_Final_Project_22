#include "Items.h"

int main(){
    int numParts;
    Items* itemPtr;

    cout << " Welcome to AutoBOM 2022 " << endl;    //Welcome and user prompt
    cout << "*************************" << endl;    //Replace this input with GUI system
    cout << "Enter number of parts: ";
    cin >> numParts;
    itemPtr = new Items[numParts];
    string partName;
    double price, rating;
    for (int i = 0; i < numParts; i++){
        cout << "Name: ";   //FIX TO HANDLE INPUT WITH SPACES I.E. STRINGS
        cin >> partName;
        cout << "Price: ";
        cin >> price;
        cout << "Rating: ";
        cin >> rating;

        itemPtr[i].setName(partName);   //INITIALIZE LIKE THIS
        itemPtr[i].setPrice(rating);    //DO NOT DO itemPtr[i] = Items("name", price, rating);
        itemPtr[i].setRating(rating);   //Will override, reinitialize, and destruct for some reason
    }

    // cout << itemPtr[1].getName() << endl; //Test array initialization, just picked a random object with a random member var

    delete [] itemPtr;
    return 0;
}