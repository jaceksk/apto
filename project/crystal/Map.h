//
// Created by jacek on 07.05.20.
//

#ifndef CRYSTAL_MAP_H
#define CRYSTAL_MAP_H

#include <iostream>
#include <fstream>
#include <string>
#include "Logger.h"
#include "Map.h"

using namespace std;


class Map {

    struct Position
    {
        int x;
        int y;
    };

    int x;
    int y;
    int crystal;
    char *map;
    int *graph;
    int *graphDiamond;
    int numberFreePosition;
    int numberCrystals;
    Position *positions;
    Position *crystalPositions;

    public:
    Map(const string& fileName);


    char get(int x, int y);
    void set(int x, int y, char val);
    void readFile(const std::string &fileName);
    bool isCrystal(int x, int y);
    bool isRock(int x, int y);
    bool isRoad(int x, int y);
    void printLabirynt();

    int numberOfFreeAreaX(int x, int y);

    int numberOfFreeAreaY(int x, int y);

    void convertToGraph();

    void setGraph(int x, int y, int val);

    int getGraph(int x, int y);

    void printGraph();

    void floydWarshall();

    void printCrystalPosition();

    void sortResult();

    Position getGraphDiamond(int x, int y);

    void setGraphDiamond(int x, int y, struct Position val);

    int getGraphDiamondRoad(int x, int y);

    void setGraphDiamondRoad(int x, int y, int val);

    void printDiamondMap();
};


#endif //CRYSTAL_MAP_H
