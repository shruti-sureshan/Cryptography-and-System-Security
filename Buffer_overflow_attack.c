
#include "stdio.h"
int main(void){
    char secret[10], pwd[10];
    
    char actual_pwd[10] = "0123456789";
    actual_pwd[10] = '\0'; // to remove any random not null char after last element.
    
    char *is_valid;
    int tries = 3;

    // storing pwd in the location just next to pwd array such that, 
    // overflow of one character will overwrite the is_valid character.
    is_valid = pwd;
    is_valid += sizeof(pwd)/sizeof(pwd[0]);

    // user is not authenticated initially.
    *is_valid = 'f';
    
    // taking password from user giving three chances to enter correct one.
    while(tries-- != 0){
        printf("Enter your password: ");
        gets(pwd);

        // checking if entered password matches the actual one.
        if(strcmp(actual_pwd, pwd) == 0){
            *is_valid = 't';         // setting validation flag to true.
            break;
        } else{
            printf("Invalid password Entered.\n\n");
        }
    }

    // checking if the is_valid was set to 't' if password was correct.
    if(*is_valid == 't'){
        printf("Valid User found.\n");
    } else{
        printf("Invalid user.\n");
    }
    return 0;
}
