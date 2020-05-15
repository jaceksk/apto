//
// Created by jacek on 07.05.20.
//

#include "Logger.h"

void logInfo(std::string msg){
    printf(ANSI_COLOR_CYAN "[INFO]" ANSI_COLOR_RESET " %s \n", msg.c_str());
}

void logDebug(std::string msg){
    printf(ANSI_COLOR_GREEN "[DEBBUG]" ANSI_COLOR_RESET " %s \n", msg.c_str());
}

void logError(std::string msg){
    printf("[ERROR] %s", msg.c_str());
}



/*
 * logger to print Map
*/


void logDebug(){
    printf("\n");
}

void logDebug(char msg){
    printf("%c", msg);
}

void logDebug(std::string msg, bool enter){
    if (enter){
        printf(ANSI_COLOR_GREEN "\n[DEBBUG]" ANSI_COLOR_RESET " %s", msg.c_str());
    } else {
        printf(" %s", msg.c_str());
    }
}


