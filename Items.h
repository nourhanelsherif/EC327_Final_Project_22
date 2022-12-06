#ifndef ITEMS_H
#define ITEMS_h
    #include <iostream>
    #include <string.h>
    using namespace std;
    class Items{
        private:
            string partName;
            double price, rating;
        public:
            //Constructors
            Items();
            Items(string in_name, double in_price, double in_rating);
            //Getters
            string getName();
            double getPrice();
            double getRating();
            //Setters
            void setName(string in_name);
            void setPrice(double in_price);
            void setRating(double in_rating);
            //Destructor
            ~Items();
    };
#endif