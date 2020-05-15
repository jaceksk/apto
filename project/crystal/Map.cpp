//
// Created by jacek on 07.05.20.
//

#include "Map.h"
#include <string>
#include <stdio.h>
#include <iomanip>
#include <iostream>
#include <boost/format.hpp>
#include <sstream>

Map::Map(const string& fileName) {
    readFile(fileName);
}

char Map::get(int x, int y) {
    return this->map[y * this->y + x];
}

void Map::set(int x, int y, char val) {
    this->map[y * this->y + x] = val;
}

int Map::getGraph(int x, int y) {
    return this->graph[y * this->numberFreePosition + x];
}

void Map::setGraph(int x, int y, int val) {
    this->graph[y * this->numberFreePosition + x] = val;
}

Map::Position Map::getGraphDiamond(int x, int y) {
    return this->crystalPositions[y * this->numberCrystals + x];
}

void Map::setGraphDiamond(int x, int y, struct Position val) {
    this->crystalPositions[y * this->numberCrystals + x] = val;
}

int Map::getGraphDiamondRoad(int x, int y) {
    return this->graphDiamond[y * this->numberCrystals + x];
}

void Map::setGraphDiamondRoad(int x, int y, int val) {
    this->graphDiamond[y * this->numberCrystals + x] = val;
}

void Map::readFile(const std::string &fileName) {
    std::ifstream infile("/home/jacek/studia/semestr_6/apto/project/crystal/maps/" + fileName, std::ios_base::in);
    infile >> this->x >> this->y >> this->crystal;

    std::string line;
    this->map = new char[this->x * this->y];

    if (!infile.is_open()) {
        perror("Error open");
        exit(EXIT_FAILURE);
    }

    int a = 0;
    while (getline(infile, line)) {
        if (!line.empty()) {
            for (int i = 0; i < line.size(); i++) {
                set(a, i, line[i]);
            }
            a++;
        }
    }
}

bool Map::isCrystal(int x, int y) {
    return  (get(x, y) == '*');
}

bool Map::isRock(int x, int y) {
    return  (get(x, y) == '#');
}

bool Map::isRoad(int x, int y) {
    return  (get(x, y) == ' ');
}

int Map::numberOfFreeAreaX(int x, int y) {
    int a = y;

    while(!isRock(x, a)){
        a++;
    }

    return a;
}

int Map::numberOfFreeAreaY(int x, int y) {
    int a = x;

    while(!isRock(a, y)){
        a++;
    }

    return a;
}

void Map::convertToGraph(){
    int s =0;
    int crystals=0;

    for(int i = 0; i < this->x; i++){
        for(int j = 0; j< this->y;j++){
            if (!isRock(i, j)){
                s++;
            }

            if (isCrystal(i, j)) {
                crystals++;
            }
        }
    }

    crystals++;
    numberFreePosition = s;
    numberCrystals = crystals;

    this->positions = new Position[numberFreePosition];
    this->crystalPositions = new Position[numberCrystals];
    s=0;
    crystals=0;

    for(int i = 0; i < this->x; i++){
        for(int j = 0; j< this->y;j++){
            if (!isRock(i, j)){
                positions[s].x = i;
                positions[s].y = j;
                s++;
            }

            if (isCrystal(i, j)){
                crystalPositions[crystals].x = i;
                crystalPositions[crystals].y = j;

                crystals++;
            }
        }
    }

    logInfo("Map free position " + to_string(s));

    for(int i = 0; i < numberFreePosition; i++){
        logDebug(to_string(i) + " positionReal x: " + to_string(positions[i].x) + ", y: " + to_string(positions[i].y));
    }

    this->graph = new int[numberFreePosition * numberFreePosition];

    for (int i = 0; i< numberFreePosition * numberFreePosition; i++){
        this->graph[i] = -1;
    }

    s =0;
    int h;
    int w;
    for(int i = 0; i < this->x; i++){
        for(int j = 0; j< this->y;j++){
            if (!isRock(i, j)){
                Position position = positions[s];
                h = numberOfFreeAreaX(i, j);
                w = numberOfFreeAreaY(i, j);

                for(int p = 0; p<numberFreePosition; p++){
                    if(positions[p].x == position.x && positions[p].y == position.y){
                        setGraph(s, s, 0);
                        continue;
                    }

                    if (positions[p].y - position.y < w-1 && positions[p].x == position.x){
                        setGraph(s, p, 1);
                        setGraph(p, s, 1);
                    }

                    if (positions[p].x - position.x < h-1 && positions[p].y == position.y){
                        setGraph(s, p, 1);
                        setGraph(p, s, 1);
                    }
                }

                s++;
            }
        }
    }


    printGraph();
    printCrystalPosition();

}

void Map::floydWarshall(){
    int k, i, j, w;

    for( k = 0; k < numberFreePosition; k++ )
        for( i = 0; i < numberFreePosition; i++ )
            for( j = 0; j < numberFreePosition; j++ ) {
                if( ( getGraph(i, k) == -1 ) || ( getGraph(k, j)  == -1 ) ) {
                    continue;
                }

                w = getGraph(i, k) + getGraph(k, j);

                if( getGraph(i, j) > w || getGraph(i, j) == -1) {
                    setGraph(i, j, w);
                }
            }

    printGraph();
}


void Map::sortResult(){
    this->graphDiamond = new int[numberCrystals * numberCrystals];
    int g = 0;
    int a =0;
    for (int i = 0; i< numberFreePosition; i++){
        if (isCrystal(positions[i].x, positions[i].y) || (positions[i].x == 1 && positions[i].y == 0 )){
            for (int j = 0; j< numberFreePosition; j++) {
                if (isCrystal(positions[j].x, positions[j].y) || (positions[j].x == 1 && positions[j].y == 0 )) {
                    graphDiamond[g] = getGraph(i, j);
                    g++;
                }
            }
        }
    }
    printDiamondMap();
}

void Map::printLabirynt() {
    logDebug((boost::format("Height: %d") % this->x).str());
    logDebug((boost::format("Width: %d") % this->y).str());
    logDebug((boost::format("Number od Crystal: %d") % this->crystal).str());

    for (int i = 0; i < this->x; i++) {
        logDebug(to_string(i) + ": ", true);
        for (int j = 0; j < this->y; j++) {
            logDebug(get(i, j));
        }
    }

    logDebug();
}

void Map::printGraph() {
    logDebug((boost::format("Free Position: %d") % this->numberFreePosition).str());

    for (int i = 0; i < this->numberFreePosition; i++) {
        logDebug("(" + to_string(positions[i].x) + ", " + to_string(positions[i].y) + "): ", true);
        for (int j = 0; j < this->numberFreePosition; j++) {
            string s = (boost::format("%s") % boost::io::group(setw(2), setprecision(2), to_string(getGraph(i, j)))).str();
            logDebug(s, false);
        }
    }

    logDebug();
}

void Map::printCrystalPosition() {
    logDebug((boost::format("Number of crystal: %d") % this->numberCrystals).str());

    for (int i = 0; i < this->numberCrystals; i++) {
        logDebug(to_string(i) + ": " + "(" + to_string(crystalPositions[i].x) + ", " + to_string(crystalPositions[i].y) + "): ", true);
    }

    logDebug();
}

void Map::printDiamondMap() {

    int a =0;
    for (int i = 0; i < this->numberCrystals; i++) {
        logDebug(to_string(i)  + ": ", true);
        for (int j = 0; j < this->numberCrystals; j++) {
            string s = (boost::format("%s") % boost::io::group(setw(2), setprecision(2), to_string(graphDiamond[a]))).str();
            logDebug(s, false);
            a++;
        }
    }

    logDebug();
}