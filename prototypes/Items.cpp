#include "Items.h"

Items::Items(){
    partName = "Placeholder";
    price = 0.0;
    rating = 0.0;
    cout << "Item " << partName << " initialized" << endl; 
}

Items::Items(string in_name, double in_price, double in_rating){
    partName = in_name;
    price = in_price;
    rating = in_rating;
    cout << "Item " << partName << " initialized" << endl;
}

Items::~Items(){
    cout << "Item " << partName <<" deleted" << endl;
}

//Getters
string Items::getName(){
    return partName;
}
double Items::getPrice(){
    return price;
}
double Items::getRating(){
    return rating;
}
int Items::getQty(){
    return quantity;
}
//Setters
void Items::setAll(string in_name, double in_price, double in_rating, int in_qty){
    partName = in_name;
    price = in_price;
    rating = in_rating;
    quantity = in_qty;
    return;
}
void Items::setName(string in_name){
    partName = in_name;
    return;
}
void Items::setPrice(double in_price){
    price = in_price;
    return;
}
void Items::setRating(double in_rating){
    rating = in_rating;
    return;
}
void Items::setQty(int qty){
    quantity = qty;
    return;
}