cmake_minimum_required(VERSION 3.14)
project(crystal)

set(CMAKE_CXX_STANDARD 11)

add_executable(crystal main.cpp Logger.cpp Logger.h Map.cpp Map.h)