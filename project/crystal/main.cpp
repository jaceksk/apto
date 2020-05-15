#include <iostream>
#include <fstream>
#include <string>
#include "Logger.h"
#include "Map.h"
#include <stdio.h>

using namespace std;

int main(int argc, char *argv[]) {

    string fileName;

    if (argc == 1) {
        fileName = "trivial.in";
    } else {
        fileName = argv[1];
    }

    Map map("trivial.in");
    map.printLabirynt();
    map.convertToGraph();
    map.floydWarshall();
    map.sortResult();

    return 0;
}





