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
        getline(cin >> ws, partName); // FIXED
        cout << "Price: "; // TEST PRICE INPUT
        cin >> price;
        cout << "Rating: "; // TEST RATING INPUT
        cin >> rating;

        itemPtr[i].setName(partName);   //INITIALIZE LIKE THIS
        itemPtr[i].setPrice(price);    //DO NOT DO itemPtr[i] = Items("name", price, rating);
        itemPtr[i].setRating(rating);
    }
    //TESTING print out
    /*
    for (int i = 0; i < numParts; i++){
        cout << itemPtr[i].getName() << endl;
        cout << itemPtr[i].getPrice() << endl;
        cout << itemPtr[i].getRating() << endl;
    }
    */

    delete [] itemPtr;
    return 0;
}