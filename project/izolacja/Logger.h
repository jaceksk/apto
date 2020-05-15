//
// Created by jacek on 14.05.2020.
//

#ifndef IZOLACJA_LOGGER_H
#define IZOLACJA_LOGGER_H


#include <string>

#define ANSI_COLOR_RED     "\x1b[31m"
#define ANSI_COLOR_GREEN   "\x1b[32m"
#define ANSI_COLOR_YELLOW  "\x1b[33m"
#define ANSI_COLOR_BLUE    "\x1b[34m"
#define ANSI_COLOR_MAGENTA "\x1b[35m"
#define ANSI_COLOR_CYAN    "\x1b[36m"
#define ANSI_COLOR_RESET   "\x1b[0m"

void logInfo(std::string msg);
void logDebug();
void logDebug(std::string msg);
void logDebug(char msg);
void logDebug(std::string msg, bool enter);
void logError(std::string msg);


#endif //CRYSTAL_LOGGER_H